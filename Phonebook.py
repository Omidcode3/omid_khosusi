# omid_khosusi 

from tkinter import messagebox
#مازول برای نمایش کادر برنامه استفادهمیشهmassagebox
from tkinter import*
#کتابخونه تیک اینتر رو فرا میخونیم برای اینکه میخایم محیط نرم افزاری بسازیم
import webbrowser
#چون میخایم از تودفتر چه بره توی فایل 
import pyperclip
#کتابخونه ی غیر استاندارد هست و باید دانلود بشه و برای کپی وتوابع کلیپ بورد مورد استفاده هست
import random
#کتابخونه رندوم رو صدا میزنیم
import os
#(امکان تعامل را باسیستم فراهم میکنه)کتابخونه ا س  رو خم صدا میزنیم

root=Tk()
#عنوان رو به بنجره اصلی میدهد
root.title("cpntakt book")
#(برچسب چیزی است که خروجی رو میده)باز کنه فایل کانتکت بوک ما رو 
root.geometry("700x350")
 #طول وعرض دفترچه ما350به700 باشه
backgrond ='#121212'
# یمتغیر با بکگراند درست میکنیم
root.config(bg=backgrond)
#از کانفیگ استفاده میکنیم برای دسترسی ب ویزگی ها(همون, appand,..... )

   
#contak farst name labal      برچسب   انجام شد
#contak farst name entry      ورودی   انجام شد

#contak last name labal     انجام شد
#contak last name entry     انجام شد

#contak numbar labal        انجام شد
#contak numbar entry        انجام شد

#contak address labal       انجام شد
#contak address entry       انجام شد

#contak e_mail address labal انجام شد
#contak e_mail address entry انجام شد

#add contak buttan          انجام شد
#save contak buttan         انجام شد

#copy phone numbar buttan   انجام شد
#opan saved file buttan     انجام شد

#delit contak buttan        انجام شد
#exit app buttan            انجام شد
#list box for contaks       انجام شد
 


#functions
def add_contak():
 #یمتغیر میسازیم و داخل حلقه دییف میزاریم
    contak_str= farst_name_entry.get()+":    " + last_name_entry.get()+":   "+ numbar_entry.get()+":  "+ address_entry.get()+":   "+ email_entry.get()
 #ی متغیر میسازیم و میگیم اسم کوچیگ و بزرگ وغیره رو با مازول گت به ما بده
    list_box.insert(END,contak_str)
#از تابع انزرت استفاده میگنیم که برای نمایش یک عنصرجدید در لیسته وعناصر بعدی رواز عنصر درج شده  با یک شاخص به سمت راست منتقل میکنه
# رو ببر داخل لیستتcontact str هم ینی اطلاعاتی که به ما داده بودendینی به ایتم اخریش اضافه کن
def delit_contak():
    list_box.delete(ANCHOR)
#ی حلقه میسازیم و یمتغیر توش قرار میدیم و از ایتم دیلیت استفاده میگنیم و میگیم انگر ما یا همون اطلا عات مون رو پاک کن
def save_list():
    #ی متغیر میسازیم و داخل حلقه قرار میدیم
    with open("E:\contakt book\saveds.txt","w") as f:
        # از ویت برای مدیریت اثنسنا استفاده میشه و با استفاده از ویجت اپن ادرسمون رو کپی میکنیم و میگیم برابر با اف
        list_omid= list_box.get(0,END)
        #ی متغیر میسازیم و میگیم برابر با داده ی لیست باکس از صفرمی تا اخری
        for item in list_omid:
            #از فور استفاده میکنیم و میگیم اتم برابر با همون متغیری که ساختیم
            if item.endswith("\n"):
                f.write(item) 
        #بعد شرط گذاری میکنیم و از مازول اندسویت چون موقعیت اخری که باید /در ان پسوند اجرا بشه و از استفاده میکنیم چون  بره خط بعد و اف بنویسه اون اطلاعاتشو #ز (\n)
        else:
            f.write(item+"\n")      
        # بنویس اطلاعات+\ان) در غیر این صورت
def opan_list(): 
    #ی متغیر میسازیم و داخل دیف قرار میدیم
    with open("E:\contakt book\saveds.txt","r") as f:
        #از وییت برای مدیریت اثنسنا استفاده میشه و با استفاده از ویجت اپن ادرسمون رو کپی میکنیم ومیگیم که بخون اونو و مقابل اف قرار میده
        for line in f :
            list_box.insert(END,line)
        #از فورر استفاده میکنیم واف که ادرسمون هست بره تو متغیر لاین
        #از اینزرت برای نمایش یک عنصر استفاده میکنیم و میگیم نمایش بده اخرین رو و ولیابل  لاین رو
        
def delit_contak():
    list_box.delete(ANCHOR)
        #ی حلقه ساختیم و ی متغیر قرار دادیم
        #از دیلیت استفاده کردیم و گفتیمااون ورودی انکر ما رو پاک کنه  
def opan_dir():
    webbrowser.open("E:\contakt book")
     #باز ی حتقه ساختیم با فوور و از وب برادرظ استفاده کرده و گفتیم برو توی ادرسی که بش دادیم
def copy_numbar():
    #ی متغیر میسازیم و داخل حتقه فوور قرار میدیم
    selected_contact= list_box.get(ANCHOR)
    #ی متغیر میسازیم و میگیم داخل لیست باکس انکر شو بهمون بده
    numbare = selected_contact.split(":")
    #شماره برابر بامتغیری که ساختیم و مازول اسپیلیت که جدا سازی میکنه با کوتیشن
    pyperclip.copy(numbare)
    # از اون کتابخونه که دانلود کردیم برای کپی شماره استفاده میکنیم

def exit():
    antaskob=messagebox.askquestion("Exit aplictaion","Do you want to exit program  ?")
    if antaskob=="yas":
        root.destroy()
    else:
        return

#ی حلقه میسازیم با فوور وداخل یک متغیر میزاریم
#انتخابمون برابر با ی جعبه سوال که درست کردیم و عنوانش میشه اولی و سواتش میشه دومی
#بعد شرط میذاریم اگ برابر بود با یسس دیستوری گنه و بره بیرون از دفتر چه و در غیر این صورت برگرده


 #contact farst name labal and entry
farst_name_labal =Label(root,text="contact farst name:",bg=backgrond ,fg="white",font=("calabri" ,12) , justify=LEFT)
# ,  ی  ولیعبل ساختیم وداخل  برچسبش گفتیم رووت (تیک اینتر)و اسمشو گذاشتیم فرست نیم و بکگراندشو مساوی قرار دادیم با بی گی  که بالا ساختیم و فور گرانشو دادیم سفید وفنت شو دادیم کالیبر 12 و جاستیفای هم مازولی است گه سمت برنامه مون رو مشخس میکنه که من سمت چب دادم
farst_name_labal.place(relx=0.1,rely=0.1,anchor="c")
#چون میخایم روی صفحه قرار از مازول پلییس استفاده میکنیم و مختصات طول و عرض روهم وارد میکنیم و انکر هم ی موقیت چند جانبه هست که بین 0و1 هست

farst_name_entry= Entry(root,bg="white", fg=backgrond, width=30, borderwidth=2)
#برای ورودی مون همتقریبا شبیه بالا و
farst_name_entry.place(relx=0.4 ,rely=0.1,anchor="c")
#برای موقیت ورودی مون هم مثل بالا مینویسیم اما عدد شو تغییر میدیم

#contakt  last name labal nad entry
last_name_labal =Label(root,text="contact last name:",bg=backgrond ,fg="white",font=("calabri" ,12)  , justify=LEFT)
 #برای برچسب اسم کوچیکمون هم مثل بالا فقط اسمشو تغیر میدیم
last_name_labal.place(relx=0.1,rely=0.2,anchor="c")
#مثل بالا فقط عدد مختصات رو تغییر میدیم
last_name_entry= Entry(root,bg="white", fg=backgrond, width=30, borderwidth=2)
last_name_entry.place(relx=0.4 ,rely=0.2,anchor="c")
#برای ورودی هم مثل بالا فقط عدد تغیر میکنه

#contakt numbar labal and entry
numbar_labal =Label(root,text="  contact  numbar:",bg=backgrond ,fg="white",font=("calabri" ,12)  , justify=LEFT)
numbar_labal.place(relx=0.1,rely=0.3,anchor="c")
#برای برچسب شماره هم به همین صورت

numbar_entry= Entry(root,bg="white", fg=backgrond, width=30, borderwidth=2)
numbar_entry.place(relx=0.4 ,rely=0.3,anchor="c")
#برای ورودی شماره هم به همین صورت

#contak address labal and entry

address_labal =Label(root,text=" contact   address:",bg=backgrond ,fg="white",font=("calabri" ,12) , justify=LEFT)
address_labal.place(relx=0.1,rely=0.4,anchor="c")
#به همین صورت که بالا گفته شد برای بقیه کانتک ها هم انجام میشه

address_entry= Entry(root,bg="white", fg=backgrond, width=30, borderwidth=2)
address_entry.place(relx=0.4 ,rely=0.4,anchor="c")

#contak e_mail address labal and entry

email_labal =Label(root,text=" e_mail  address:",bg=backgrond ,fg="white",font=("calabri" ,12)  , justify=LEFT)
 
email_labal.place(relx=0.1,rely=0.5,anchor="c")

email_entry= Entry(root,bg="white", fg=backgrond, width=30, borderwidth=2)
email_entry.place(relx=0.4 ,rely=0.5,anchor="c")

#add contak buttan 

add_but = Button(root, text="Add   Contact",bg=backgrond,fg="white",borderwidth=3,padx=150,command=add_contak)
#ی متغیر ساختیم و از باتن استفاده کردیم چون دسترسی به ویزگی ها رو به ما بدهبعد بردیم داخل اپ ورووت اضافه کردیم و با تکس براش اسم انتخاب کردیم و
#  بکگراند و فور گراند بش دادیم و بردن وییت همبرای پهنای حاشیه هست وپد باگس هم برای اندازه دکمه ها هست که بخاطر کارکتر هایی که داره عدد هاشون متفاوتن
#کامند هم ی مازولی هست که متغیر فاینشن مون رو باهاش مساوی قرار دادیم
add_but.place(relx=0.29,rely=0.70,anchor="c")
#طبق توضیحات بالا صورت میگیره

#save list buttan

save_but= Button(root,text="Save   List", bg=backgrond,fg="white",borderwidth=3,padx=160,command=save_list)

save_but.place(relx=0.29,rely=0.80,anchor="c")

#copy phone numbar buttan

copy_phone= Button(root,text="Copy Phone Numbar",bg=backgrond,fg="white",borderwidth=3,padx=33,command=copy_numbar)

copy_phone.place(relx=0.15,rely=0.88,anchor="c")

#delit contak buttan

delit_contak= Button(root,text="Delit Contact",bg=backgrond,fg="white",borderwidth=3,padx=57,command=delit_contak)

delit_contak.place(relx=0.15,rely=0.96,anchor="c")

#opan saved file buttan

opan_saved_file=Button(root, text="Opan Saved File",bg=backgrond,fg="white",borderwidth=3,padx=49 , command=opan_dir)

opan_saved_file.place(relx=0.43,rely=0.96,anchor="c")

#exit buttan

exit = Button(root, text="  Exit App    ",bg=backgrond,fg="white",borderwidth=3,padx=60,command=exit)

exit.place(relx=0.43,rely=0.88,anchor="c")

#list box for contaks

list_box=Listbox(root,width=48,height=19)
#لیست باکس هم ویجت ی هست که برای نمایش اطلا عات کاربر وطول وعرضش رو نسبت به دفتر چه مون فیت میکنیم
list_box.place(relx=.78,rely=0.50,anchor="c")
#و در اخرمختصاتش رو وارد میکنیم
root.mainloop()
#هرگاه کتابخونه تیکانتر رو صدا زدیم اخر کار از این ویجیت استفاده میکنیم
