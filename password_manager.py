# omid_khosusi


from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
import hashlib

# اتصال به پایگاه داده MySQL
try:
    cnx = mysql.connector.connect(user='root',
                                  password='1234',
                                  host='localhost',
                                  database='yazd')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("عدم دسترسی به پایگاه داده")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("پایگاه داده وجود ندارد")
    else:
        print(err)

# ساخت جدول پسوردها در صورت عدم وجود
TABLES = {}
TABLES['passwords'] = (
    "CREATE TABLE IF NOT EXISTS `passwords` ("
    "  `id` INT AUTO_INCREMENT PRIMARY KEY,"
    "  `username` VARCHAR(255) NOT NULL,"
    "  `password` VARCHAR(255) NOT NULL"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("ایجاد جدول {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("جدول وجود دارد")
        else:
            print(err.msg)
    else:
        print("انجام شد")

# تابع برای ذخیره کردن پسورد جدید
def save_password():
    username = username_entry.get()
    password = password_entry.get()

    # هش کردن پسورد
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # اضافه کردن پسورد جدید به دیتابیس
    add_password_query = "INSERT INTO passwords (username, password) VALUES (%s, %s)"
    add_password_data = (username, hashed_password)
    cursor.execute(add_password_query, add_password_data)
    cnx.commit()

    messagebox.showinfo("ذخیره پسورد", "پسورد با موفقیت ذخیره شد")

# تابع برای نمایش پسوردهای ذخیره شده
def show_passwords():
    password_list.delete(0, END)

    # دریافت پسوردهای ذخیره شده از دیتابیس
    get_passwords_query = "SELECT * FROM passwords"
    cursor.execute(get_passwords_query)

    for (id, username, hashed_password) in cursor:
        password_list.insert(END, "نام کاربری: " + username + " | پسورد: " + hashed_password)

# ایجاد پنجره گرافیکی
root = Tk()
root.title("مدیر رمز عبور")

# عنوان صفحه
title_label = Label(root, text="ذخیره و نمایش رمز عبور")
title_label.pack()

# فرم ذخیره پسورد
username_label = Label(root, text="نام کاربری:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="رمز عبور:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

save_button = Button(root, text="ذخیره", command=save_password)
save_button.pack()

# لیست پسوردها
password_list = Listbox(root)
password_list.pack()

# دکمه نمایش پسوردها
show_button = Button(root, text="نمایش پسوردها", command=show_passwords)
show_button.pack()

# اجرای برنامه
root.mainloop()

# بستن اتصال به دیتابیس
cursor.close()
cnx.close()
