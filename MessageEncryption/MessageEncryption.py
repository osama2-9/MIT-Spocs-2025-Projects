
# دوال فرعية نحتاجها في فنكشن المرسل ==>


table_key1 = {
    'a': 42, 'b': 57, 'c': 13, 'd': 68, 'e': 24, 'f': 71, 'g': 36, 'h': 90,
    'i': 51, 'j': 27, 'k': 64, 'l': 14, 'm': 83, 'n': 49, 'o': 72, 'p': 18,
    'q': 55, 'r': 67, 's': 21, 't': 85, 'u': 39, 'v': 46, 'w': 29, 'x': 11,
    'y': 92, 'z': 34, '0': 88, '1': 44, '2': 91, '3': 73, '4': 63, '5': 54,
    '6': 37, '7': 26, '8': 15, '9': 84, ' ': 99, '.': 17, ',': 25, '!': 19,
    '?': 31, ':': 48, ';': 41, '-': 65, '_': 53, '(': 12, ')': 22, '[': 33,
    ']': 28, '{': 32, '}': 38, "'": 16, '"': 59, '@': 75, '#': 45, '$': 97,
    '%': 62, '^': 43, '&': 52, '*': 93, '+': 47, '=': 40, '/': 50, '\\': 60
} #يحتوي على كل الحروف و الارقام و الرموز المشهورة 

reverse_table_key1={} # بدنا نعكس الجدول عشان حنستخدمه في فك التشفير
for key,value in table_key1.items():
    reverse_table_key1[str(value)]=key

def key1_sender():

    sender_message= input("enter the message you want to encrypt \n ==> ")
    sender_message=sender_message.lower()
 
    # 1. لتخزين الارقام الخاصة بكل عنصر في مسج المرسل
    numbers=[] 
    for i in sender_message:
        if i in table_key1:
            numbers.append(table_key1[i])
        else: # لو في اشي من الي دخله المستخدم غير موجود في الجدول بنحط بداله علامة استفهام
            numbers.append("?")
    
    # 2. قلب كل رقمين مع بعض 
    for i in range(0,len(numbers)-1,2): # السالب 1 هادي عشان احنا بنقلب كل رقمين ف ما بدنا نوصل لاخر النص و يصير ايرور
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    # 3.  جمع كل اندكس بارقام معينة
    x=2
    for i in range(len(numbers)):
        if isinstance(numbers[i],int): # نتاكد انه رقم مش علمة استفهام
            numbers[i] += x # i+2   i+5     i+8     i+11    i+14
        x += 3  # 2+3=5    5+3=8   8+3=11    11+3=14    14+3=17

    # 4. نضيف 00 في البداية و النهاية عشان نميز طريقة التشفير
    numbers.insert(0,"1")
    numbers.append("1")

    # 5. نفصل بين كل اندكس و التاني ب ( )
    str_numbers=[] # قائمة الناتج النهائي كنصوص
    for i in numbers:
        str_numbers.append(str(i)) # حولناها لنص و ضفناها ل الليست الفاضية
    encrypted = ' '.join(str_numbers) # نجمع كل العناصر بفاصل 

    print(f"Encrypted message: {encrypted}") # طباعة النص المشفر النهائي

#--------------------------------------------------------------------------

table_key2 = {
    'a': 41, 'b': 56, 'c': 12, 'd': 69, 'e': 23, 'f': 70, 'g': 35, 'h': 91,
    'i': 52, 'j': 26, 'k': 65, 'l': 10, 'm': 82, 'n': 48, 'o': 74, 'p': 19,
    'q': 58, 'r': 66, 's': 20, 't': 86, 'u': 38, 'v': 47, 'w': 30, 'x': 14,
    'y': 94, 'z': 33,'0': 87, '1': 43, '2': 95, '3': 72, '4': 61, '5': 55,
    '6': 36, '7': 27, '8': 16, '9': 83,' ': 98, '.': 18, ',': 25, '!': 29,
    '?': 32, '-': 63, '_': 54
}
reverse_table_key2={} 
for key,value in table_key2.items():
    reverse_table_key2[str(value)]=key

code_to_symbol = {
    '41': '%^','56': '&@','12': '!~','69': '$*','23': '^%','70': '/!','35': '~#',
    '91': '*+','52': '{<','26': '|?','65': '+}','10': ']=','82': '#@','48': '[&',
    '74': '>%','19': '?/','58': '-$','66': '@_','20': '><','86': '^=','38': '$!',
    '47': '!*','30': '{#','14': '_[','94': ')%','33': '#^','87': '/$','43': ']_',
    '95': '+@','72': '=@','61': '!&','55': '(#','36': '%}','27': '_@','16': '}!',
    '98': '|+','18': '#%','25': '{=','29': '~%','32': '*>','63': '/=','54': '^#','83': '(@'}
symbol_to_code={}
for key,value in code_to_symbol.items():
    symbol_to_code[value]=key

KEY2_START = "<<"
KEY2_END   = ">>"

def key2_sender():
    sender_message= input("enter the message you want to encrypt \n ==> ").lower()

    if not sender_message:
        raise ValueError("Key2: empty message cannot be encrypted.")

    number_code=[] 
    for i in sender_message:
        if i in table_key2:
            number_code.append(str(table_key2[i]))
        else:
            number_code.append('??')
    
    symbol_code=[]
    for i in number_code:
        if i in code_to_symbol:
            symbol_code.append(code_to_symbol[i])
        else:
            symbol_code.append('??')

    symbol_str = ''.join(symbol_code)
    rev_symbol_str= symbol_str[::-1]

    final_encrypted = KEY2_START+rev_symbol_str+KEY2_END
    print(f"Encrypted message: {final_encrypted}")

# --------------------------------------------------------------------

# فنكشن المرسل الرئيسية ==>

def sender():

    while True:

        encryption_options=input("Please choose the encryption method you'd like to use ==> \n 1. key1 \n 2. key2 \n 3. Exit \n Write your choice number here : ")

        try:

            encryption_options=int(encryption_options)

            if encryption_options == 1:
                key1_sender()
                break
            elif encryption_options == 2:
                key2_sender()
                break
            elif encryption_options ==3 :
                break
            else:
                print("x "*35)
                print("This number is not available in the options \n Please enter a number 1 , 2 or 3 \n ==>")

        except ValueError:
            print("x "*35)
            print("Please enter only the option number \n ==>")            

# ================================================================================================

# دوال فرعية نحتاجها في فنكشن المستقبل ==>


def key_1_receiver():
    receiver_message= input("enter the message you want to decrypt \n ==> ")

    # 1. فصل الأرقام باستخدام الفاصل 
    parts=receiver_message.split(" ")

    # 2. التأكد من العلامات الخاصة 00
    if parts[0] != "1" or parts[-1] != "1":
        print("This message is not encrypted with Key1 method!")
        return
    # 3. حذف البداية والنهاية
    parts=parts[1:-1]
    
    # 4. طرح كل اندكس من ارقام معينة
    x=2
    for i in range(len(parts)):
        if parts[i].isdigit(): # بنتاكد انه النص عبارة عن رقم لانه ممكن يكون علامة استفهام
            parts[i]= str(int(parts[i]) - x) # طرح بنفس القيمة التصاعدية 
        x += 3
    
     # 5. قلب كل رقمين مع بعض
    for i in range(0, len(parts) - 1, 2):
        parts[i], parts[i+1] = parts[i+1], parts[i]

    # 6. تحويل الأرقام إلى حروف
    message=''
    for i in parts:
        if i in reverse_table_key1:
            message += reverse_table_key1[i]
        else:
            message += "?"
    print(f"Decrypted message: {message}")

#---------------------------------------------------------------------------

def key_2_receiver():
    receiver_message= input("enter the message you want to decrypt \n ==> ")
    if not (receiver_message.startswith(KEY2_START) and receiver_message.endswith(KEY2_END)):
        raise ValueError("Key2: missing or wrong boundary markers.")
    
    remove_borders=receiver_message[len(KEY2_START):-len(KEY2_END)]
    
    symbol_str= remove_borders[::-1]

    if len(symbol_str) % 2 != 0:
        raise ValueError("Key2: invalid symbol length (must be multiple of 2).")
    
    tokens = []  # قائمة فاضية عشان نخزن فيها الرموز
    for i in range(0, len(symbol_str), 2):
        token = symbol_str[i:i+2] #بتاخد كل رمزين مع بعض 
        tokens.append(token)

    numeric_codes = [] # راح نحول الرموز لارقام
    for i in tokens:
        if i in symbol_to_code:
            numeric_codes.append(symbol_to_code[i])
        elif i == '??':
            numeric_codes.append('??')  
        else:
            raise ValueError(f"Key2: unknown symbol token '{i}'.")
        
    num_to_char=[] #تحويل الارقام لاصلها
    for i in numeric_codes:
        if i in reverse_table_key2:
            num_to_char.append(reverse_table_key2[i])
        elif i == '??':
            num_to_char.append('?')
        else:
            # حالة نادرة: كود غير معروف
            num_to_char.append('?')
    
    Decrypted_message= ''.join(num_to_char)
    print(f"Decrypted message: {Decrypted_message}")

# ------------------------------------------------------------------

# فنكشن المستقبل الرئيسية ==>

def receiver ():

    while True:

        decryption_options=input("Please choose the decryption method you'd like to use ==> \n 1. key -1 \n 2. key -2 \n 3. Exit \n Write your choice number here : ")

        try:

            decryption_options=int(decryption_options)

            if decryption_options == 1:
                key_1_receiver()
                break
            elif decryption_options == 2:
                key_2_receiver()
                break
            elif decryption_options == 3:
                break
            else:
                print("x "*35)
                print("This number is not available in the options \n Please enter a number 1 , 2 or 3 \n ==>")

        except ValueError:
            print("x "*35)
            print("Please enter only the option number \n ==>")  


# ===========================================================================================================================

# ما بعد هذا السطر هو الكود الرئيسي >>>>>>>>

while True:

    user_input=input("Are you sender or receiver? \n 1. Sender \n 2. Receiver \n 3. Exit \n Write your choice number here : ")
    
    try:
        user_input=int(user_input) #بنشوف ازا المدخل بتحول لعدد صحيح ؟ 
        if user_input == 1:
            sender()
            # print("sender")
            # break
        elif user_input == 2:
            receiver()
            # print("Receiver")
            # break
        elif user_input == 3:
            print("Thank you for using our program!")
            break
        else:
            print("x "*35)
            print("This number is not available in the options \n Please enter a number from 1 to 3 \n ==>")

    except ValueError: # يعني انه المستخدم دخل اشي غير ارقام صحيحة
        print("x "*35)
        print("Please enter only the option number \n ==>")