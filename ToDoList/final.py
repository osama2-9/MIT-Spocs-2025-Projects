import tkinter as tk  # عشان نعمل واجهة رسومية ونعمل الازرار و القوائم
from tkinter import messagebox, filedialog  # الاولى لعرض رسائل تحذير والتانية لفتح نافذة اختيار الملفات
from datetime import datetime  # عشان نستخدم التاريخ والوقت
from plyer import notification  # هاي للتنبيهات والمسج يلي بطلع ع الشاشة

import json  # لحفظ وقراءة البيانات بصيغة JSON
import pygame  # لتشغيل ملفات الصوت
import os  # للتأكد من وجود الملفات
import threading  # عشان نشغل بعض الاوامر بدون م نعلق الواجهة
import time  # للوقت
import webbrowser  # عشان نفتح اي رابط أو ملف من المتصفح

# بنجهز مكتبة الصوت عشان يشتغلوا الاصوات لو ضفناهم ومهم لانه بدونه مش رح يشتغل
pygame.mixer.init()

# هنا بنخزن المهام بصيغة جاسون
DATA_FILE = "tasks.json"

# تحميل المهام من الملف
def load():
    if os.path.exists(DATA_FILE):  # لو الملف موجود
        try:
            return json.load(open(DATA_FILE))  # رح يقرا المهام ويحولها لقائمة بايثون
        except:
            return []  # لو صار خطأ بالقراءة، بنرجع قائمة فاضية
    return []

# حفظ المهام داخل الملف
def save():
    json.dump(tasks, open(DATA_FILE, "w"), indent=4)  # json.dump رح يحفظ البيانات في ملف بصيغة
    # w و indent=4 يعني رح يكون التنسيق مرتب

# تحديث القائمة المعروضة في الواجهة
def update_list():
    listbox.delete(0, tk.END)  # بتمسح كل العناصر من الواجهة
    global view  # يعني بنقدر نستخدم view في كل مكان

    view = []  # قائمة جديدة لتخزين المهام المعروضة حاليًا

    # بنرتب المهام حسب وقتها
    for t in sorted(tasks, key=lambda x: x['time']):
        txt = f"{t['title']} @ {t['time']}"  # بننسق نص المهمة

        # هنا بنفلتر المهام حسب نص البحث
        if search_var.get().lower() in txt.lower():
            listbox.insert(tk.END, txt)  # بنعرض المهمة في الواجهة
            view.append(t)  # بنضيف المهمة لقائمة فيو

# اختيار فيديو
def browse_video():
    path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])  # هنا طبعا الفيديو بصيغة ام بي 4
    if path:
        video_v.set(path)  # لو ضفنا فيديو، بنحفظ مساره في المتغير

# اختيار صوت
def browse_sound():
    path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])  # نختار ملف صوت بصيغة mp3
    if path:
        sound_v.set(path)  # نحفظ المسار في المتغير الخاص بالصوت

# إضافة مهمة جديدة
def add():
    title = title_e.get().strip()  # بناخد عنوان المهمة من خانة الادخال
    time_str = time_e.get().strip()  # بناخد الوقت من خانة الادخال

    # لو العنوان او الوقت فاضيين بنطلع من الدالة وم بنضيفهم
    if not title or not time_str:
        return

    # بنتاكد انه الوقت مكتوب بشكل صحيح
    try:
        datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    except:
        return

    # هنا بنضيف المهمة
    tasks.append({
        "title": title,
        "time": time_str,
        "video": video_v.get(),
        "sound": sound_v.get(),
        "reminded": False
    })

    save()           # بنحفظ المهام
    update_list()    # بنحدث القائمة ع الواجهة

    # بنمسح القيم من واجهة المستخدم بعد إضافة المهمة
    title_e.delete(0, tk.END)  # هنا بنمسح خانة العنوان
    time_e.delete(0, tk.END)   # وهنا الوقت
    video_v.set("")            # وهنا الفيديو
    sound_v.set("")            # وهنا الصوت
###########################################################
#####حذف مهمة ######
#تعريف الدالة بعدها بتجيب موقع العنصر الي تم اختياره بعدها التاكد من انو المستخدم اختار هاد العنصر بعدها بنحذفه وبنحفظ التغيرات الي صارت#

def delete():
    selected = listbox.curselection()
    if selected:
        tasks.remove(view[selected[0]])
        save()
        update_list()

# تعديل مهمة
def edit():
    # أول إشي: نعرف شو اختار المستخدم
    selected = listbox.curselection()       
    # إذا ما اختار إشي نوقف
    if len(selected) == 0:
        return
    # نجيب المهمة اللي بدنا نعدلها من قائمة العرض view
    selected_task = view[selected[0]]
    # نحدث بيانات المهمة من الخانات اللي كتبها المستخدم
    selected_task["title"] = title_e.get()
    selected_task["time"] = time_e.get()
    selected_task["video"] = video_v.get()
    selected_task["sound"] = sound_v.get()
    selected_task["reminded"] = False  # لازم نرجعه False عشان يتفعل التذكير من جديد
    save()
    update_list()

    # نفرّغ الخانات
    title_e.delete(0, tk.END)#الصفر الي هي اول حرف لحد النهاية 
    time_e.delete(0, tk.END)
    video_v.set("")
    sound_v.set("")

#حذف كل المهام 
def clear():#تعريف الدالة بعدها بعرض رسالة لتاكيد الحذف 
    user_answer = messagebox.askyesno("Confirm", "Delete all?")
    if user_answer:
        tasks.clear()
        save()
        update_list()

# تفعيل البحث
#عملنا دالة اسمها search، الهدف منها إنه كل ما يصير تغيير في مربع البحث يتم استدعاء الدالة.
#كتبنا *args لأنه لما نربط الدالة بحدث في tkinter، النظام بيبعث معلومات إضافية عن الحدث، وإحنا مش بنستخدمها لكن لازم نستقبلها حتى ما يصير خطأ.
#داخل الدالة استدعينا update_list() لتحديث القائمة حسب النص المكتوب في البحث.
def search(*args):
    update_list()

# التذكير بالخلفية
def reminder():
    while True:
        now = datetime.now()#هاي بتجيب الوقت الحالي من الجهاز 
        for task in tasks:
            try: # حاول تقارن الوقت
                # بحول وقت المهمة من نص الى وقت
                task_time = datetime.strptime(task['time'], "%Y-%m-%d %H:%M")
                # احسب الفرق بالثواني بين الآن ووقت المهمة
                time_difference = (task_time - now).total_seconds()
                # لو المهمة ما تذكرت قبل وكان باقي أقل من 5 دقائق
                if task['reminded'] == False and time_difference >= 0 and time_difference <= 300:
                    #هنا بتاكد من انو في صوت يتشغل و مكتبة osبتتاكد من انو الصوت هاد موجود في الجهاز فعلا 
                    if task['sound'] != "" and os.path.exists(task['sound']):
                        pygame.mixer.Sound(task['sound']).play()#مكتبة تشغيل الاصوات -
                    # لو في فيديو موجود افتحه
                    if task['video'] != "" and os.path.exists(task['video']):
                        webbrowser.open(task['video'])#وظيفتها تفتح الرابط او الملف في المتصفح
                    # اعرض إشعار للمستخدم
                    notification.notify(
                        title="Reminder",
                        message=f"{task['title']} is starting soon!",
                        timeout=5
                    )

                    # حدد إن التذكير صار وخزن التغيير
                    task['reminded'] = True
                    save()

            except:
                # لو صار خطأ تجاهل المهمة
                continue

        # عشان يستنى 30 ثانية بين كل مرة والتانية 
        time.sleep(30)

#########################################################
# إعداد الواجهة
root = tk.Tk()  #ينشئ النافذة الرئيسية لتطبيق Tkinter. 
root.title("Task Manager") # يغير اسم النافذة الذي يظهر في الشريط العلوي  (تاسك مانجر )
root.geometry("550x640") #   نحددارتفاع وعرض النافذة  
root.resizable(False, False) # المستخدم لايسطيع تكبير او تصغير النافذة (يمنع تغيير الحجم ) 
root.configure(bg="#f0f0f0") # نعطي  لون النافذة رمادي الفاتح 

# متغيرات
tasks = load() #يستدعي دالة load() لتحميل المهام من ملف أو قاعدة بيانات 
view = [] #قائمة فارغة ستُستخدم لعرض المهام على الشاشة بعد التصفية أو البحث 
video_v, sound_v, search_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
# متغير خاص بـ Tkinter يسمح بربط البيانات بالواجهة
#1لحفظ مسار الفيديو 
#2 لحفظ مسار الصوت 
#3 لحفظ النص المكتوب في مربع البحث


# إدخال العنوان والوقت
tk.Label(root, text="Title").pack() # يضيف نصًا ثابتًا على الواجهة بعنوان
title_e = tk.Entry(root) # حقل إدخال نصي لحفظ عنوان المهمة 
title_e.pack(fill='x', padx=10)  # يجعل عرض النافذة 10 بكسل 

tk.Label(root, text="Time (YYYY-MM-DD HH:MM)").pack() # يوضح للمستخدم الصيغة المطلوبة للوقت 
time_e = tk.Entry(root) # حقل إدخال نصي لكتابة وقت المهمة
time_e.pack(fill='x', padx=10) # فس الفكرة السابقة مع مسافة جانبية 

# اختيار فيديو وصوت
tk.Button(root, text="Choose Video", command=browse_video).pack() 
# زر بعنوان "Choose Video" ينفذ الدالة browse_video عند الضغط عليه (لفتح ملف فيديو

tk.Label(root, textvariable=video_v).pack() #يعرض اسم أو مسار الفيديو المختار

tk.Button(root, text="Choose Sound", command=browse_sound).pack() # نفس الفكرة تعت الفيديو و  لكن للصوت
tk.Label(root, textvariable=sound_v).pack() # يربط التسمية بقيمة المتغير (StringVar) بحيث تتغير تلقائيًا 

# أزرار العمليات
btns = tk.Frame(root) # حاوية لوضع الأزرار بداخلها 
btns.pack(pady=5) # حلقة تمر على قائمة تحتوي اسم الزر والدالة الخاصة به
for txt, cmd in [
    ("Add", add),
    ("Edit", edit),
    ("Delete", delete),
    ("Clear", clear)
]:
    color = {                          # يختار لون الخلفية بناءً على اسم الزر 
        "Add": "#4CAF50",     
        "Edit": "#FF9800",    
        "Delete": "#f44336",  
        "Clear": "#2196F3"   
    }[txt]
    
    tk.Button(btns, text=txt, command=cmd, width=10, bg=color, fg="white").pack(side=tk.LEFT, padx=5)
#ينشئ الزر مع اللون المناسب ويضعه بجانب الآخر (side=tk.LEF


# بحث
search_entry = tk.Entry(root, textvariable=search_var) #حقل إدخال النص للبحث، مرتبط بـ search_var 
search_entry.pack(fill='x', padx=10) # يمتد بعرض النافذة بالكامل.
#يكون بينه وبين الحواف اليمنى واليسرى مسافة 10 بكسل.

search_var.trace_add("write", search) #يراقب أي تغيير في النص ويستدعي الدالة search تلقائيًا.

# قائمة المهام
listbox = tk.Listbox(root, height=15)  #  2يعرض 15 سطرًا قبل ظهور شريط التمرير,  Listbox: عنصر لعرض قائمة من العناصر (المهام)1 
listbox.pack(fill='both', padx=10, pady=10, expand=True)  #2 يتمدد أفقيًا ورأسيًا1  , يسمح بتمدد العنصر لملء المساحة

# **إضافة لتحميل بيانات المهمة المختارة في الخانات عند النقر عليها**
def load_selected_task(event):
    selected = listbox.curselection()
    if not selected:
        return
    task = view[selected[0]]
    title_e.delete(0, tk.END)
    title_e.insert(0, task["title"])
    time_e.delete(0, tk.END)
    time_e.insert(0, task["time"])
    video_v.set(task["video"])
    sound_v.set(task["sound"])

listbox.bind("<<ListboxSelect>>", load_selected_task)

# بدء البرنامج
update_list()

# **تشغيل الريمايندر في الخلفية عشان يطلع التنبيه**
threading.Thread(target=reminder, daemon=True).start()

root.mainloop()
