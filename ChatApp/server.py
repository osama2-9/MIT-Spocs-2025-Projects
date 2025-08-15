import socket
import threading

# "0.0.0.0" -> Accept connections from any IP address on the server device
HOST = "0.0.0.0" 
PORT = 5555
# get the server IPv4 address automaticly
# SERVER = socket.gethostbyname(socket.gethostname())

# creat a new socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server to socket
# server_socket.bind((SERVER, PORT))
server_socket.bind((HOST, PORT))

# server start listing to clients connection requests
server_socket.listen()

# username -> conn
clients = {}  
# lock -> to make sure no problems happen if more than one user connection at the same time
lock = threading.Lock()

# send a list of connected users to all clients
def broadcast_user_list():
    with lock:
        users = list(clients.keys())
    user_list_message = "__USERS__|" + "|".join(users)
    # send the message to all users 
    for conn in clients.values():
        try:
            # encode() -> str to bytes
            conn.send(user_list_message.encode())
        except:
            continue

# handle all of the comunication between the client and betwen the server
def handle_client(conn, addr):
    # try if the connection was failed
    try:
        # 1024 -> كم يقرا من حجم الرسالة (if the message is bigger the server reads only one kilo byte)
        # بس هنا اسم المستخدم ما بكون اكثر من واحد كيلو بايت 
        username = conn.recv(1024).decode().strip()
        # if the username not receved close the connection
        if not username:
            conn.close()
            return

        with lock:
            clients[username] = conn
        print(f"[+] {username} connected from {addr}")
        broadcast_user_list()

        while True:
            data = conn.recv(4096)
            if not data:
                break

            message = data.decode()
            parts = message.split("|", 2)
            if len(parts) != 3:
                continue

            sender, receiver, encrypted = parts
            with lock:
                receiver_conn = clients.get(receiver)

            if receiver_conn:
                try:
                    receiver_conn.send(f"{sender}|{encrypted}".encode())
                except:
                    pass

    except Exception as e:
        print(f"[!] Error: {e}")

    # delete the username from the clients list if he logged out
    finally:
        with lock:
            for user, c in list(clients.items()):
                if c == conn:
                    print(f"[-] {user} disconnected")
                    del clients[user]
                    break
        conn.close()
        broadcast_user_list()


def start_server():
    print(f"[*] Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server_socket.accept()
        # start a new thread to every client 
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# starting server when the file is running
if __name__ == "__main__":
    start_server()
