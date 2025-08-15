import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import *
from encryption import encryption, decryption 

# server settings
SERVER_IP = "192.168.1.10"  
SERVER_PORT = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
current_receiver = None
username = ""

# server connection function
def connect_to_server(name):
    global username
    username = name
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.send(username.encode())
    except Exception as e:
        messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
        return False
    return True

# sending message function 
def send_message():
    message = message_entry.get().strip()
    if not current_receiver:
        messagebox.showerror("Error", "Please select a contact first")
        return
    if not message:
        return
    encrypted = encryption(message, key=username)
    try:
        full_msg = f"{username}|{current_receiver}|{encrypted}"
        client_socket.send(full_msg.encode())
        message_entry.delete(0, tk.END)
        display_message(username, message)
    except Exception as e:
        messagebox.showerror("Error", f"Send failed: {str(e)}")

# receving messages
def receive_messages():
    while True:
        try:
            data = client_socket.recv(4096).decode()
            if not data:
                break

            if data.startswith("__USERS__|"):
                update_contacts(data.replace("__USERS__|", ""))
                continue

            sender, encrypted = data.split("|", 1)
            decrypted = decryption(encrypted, key=sender)
            if sender == current_receiver:
                display_message(sender, decrypted)
        except:
            break

# display messages with bubbles
def display_message(sender, message):
    msg_text.config(state="normal")
    bubble = f"\n{sender}:\n{message}\n"
    msg_text.insert(tk.END, bubble)
    msg_text.tag_add("bubble", "end-3l", "end-1l")
    msg_text.tag_config("bubble", background="#dcedc8", foreground="#1b5e20", font=("Arial", 12), spacing1=5)
    msg_text.config(state="disabled")
    msg_text.see(tk.END)

# update th users list 
def update_contacts(users_str):
    global contacts_list, username
    users = users_str.split("|")
    contacts_list.delete(0, tk.END)
    for u in users:
        if u != username:
            contacts_list.insert(tk.END, u)

# sets who the receiving user is when a contact is clicked and clears the old window
def on_select(event):
    global current_receiver
    selection = contacts_list.curselection()
    if selection:
        current_receiver = contacts_list.get(selection[0])
        chat_title.config(text=f"Chat with {current_receiver}")
        msg_text.config(state="normal")
        msg_text.delete("1.0", tk.END)
        msg_text.config(state="disabled")

# welcome window GUI
def welcome_window():
    welcome = tk.Tk()
    welcome.title("Chat Application")
    # size of window
    welcome.geometry("350x220")
    welcome.configure(bg="#f9f9f9")

    tk.Label(welcome, text="Welcome to Chat App", font=("Arial", 16, "bold"), fg="#1b5e20", bg="#f9f9f9").pack(pady=40)

    tk.Button(welcome, text="Login", bg="#2e7d32", fg="white", font=("Arial", 12, "bold"),
               width=15, command=lambda: [welcome.destroy(), show_login_window()]).pack(pady=10)

    welcome.mainloop()

# login window  
def show_login_window():
    login = tk.Tk()
    login.title("Login")
    login.geometry("350x220")
    login.configure(bg="#ffffff")

    tk.Label(login, text="Welcome Back", font=("Arial", 16, "bold"),
             fg="#1b5e20", bg="#ffffff").pack(pady=20)

    tk.Label(login, text="Username", font=("Arial", 12), bg="#ffffff").pack()
    username_entry = tk.Entry(login, font=("Arial", 12))
    username_entry.pack(pady=5)

    def handle_login():
        username = username_entry.get().strip()
        if username:
            success = connect_to_server(username)
            if success:
                login.destroy()
                open_chat_window(username)

    tk.Button(login, text="Login", bg="#2e7d32", fg="white", font=("Arial", 12, "bold"), width=12, command=handle_login).pack(pady=15)

    tk.Button(login, text="Back", bg="#cccccc", font=("Arial", 10), command=lambda: [login.destroy(), welcome_window()]).pack()

    login.mainloop()

#  chat window
def open_chat_window(username):
    global contacts_list, chat_title, message_entry, msg_text, current_receiver

    root = tk.Tk()
    root.title("Chat App - " + username)
    root.geometry("1000x600")
    root.configure(bg="#ffffff")

    # side bar
    sidebar = tk.Frame(root, width=200, bg="#e0f2f1")
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="Chats", bg="#e0f2f1", font=("Arial", 14, "bold"), fg="#004d40").pack(pady=10)

    contacts_list = tk.Listbox(sidebar, font=("Arial", 12), bg="#ffffff", fg="#000000")
    contacts_list.pack(fill="both", expand=True, padx=10)
    contacts_list.bind("<<ListboxSelect>>", on_select)

    tk.Button(sidebar, text="Logout", font=("Arial", 11, "bold"), bg="#00897b", fg="white",
              command=lambda: [root.destroy(), welcome_window()]).pack(pady=10)

    #  chat bar
    chat_frame = tk.Frame(root, bg="#ffffff")
    chat_frame.pack(side="right", fill="both", expand=True)

    chat_title = tk.Label(chat_frame, text="Chat with ...", font=("Arial", 14, "bold"), bg="#ffffff", fg="#1b5e20")
    chat_title.pack(pady=10)

    msg_text = scrolledtext.ScrolledText(chat_frame, font=("Arial", 12), state="disabled", bg="#f1f8e9", wrap="word")
    msg_text.pack(fill="both", expand=True, padx=10)

    # Insert
    bottom_frame = tk.Frame(chat_frame, bg="#ffffff")
    bottom_frame.pack(fill="x", padx=10, pady=10)

    message_entry = tk.Entry(bottom_frame, font=("Arial", 12))
    message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=6)

    send_btn = tk.Button(bottom_frame, text="Send", bg="#43a047", fg="white", font=("Arial", 12, "bold"),
                         command=send_message)
    send_btn.pack(side="right")

    threading.Thread(target=receive_messages, daemon=True).start()
    # to keep the window open until the user close it
    root.mainloop()

# start the app
if __name__ == "__main__":
    welcome_window()