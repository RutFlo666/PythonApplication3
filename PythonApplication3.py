import hashlib
import os
import tkinter as tk
from tkinter import messagebox

def init_file():
    """Создает файл пользователей, если его нет."""
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass

def add_user(login: str, password: str) -> bool:
    """Добавляет пользователя в файл."""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0]:
            return False

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')
    return True

def get_user(login: str, password: str) -> bool:
    """Проверяет логин и пароль пользователя."""
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:
            return True
    return False

def login_user():
    """Функция входа пользователя."""
    login = entry_login_username.get()
    password = entry_login_password.get()

    result = get_user(login, hashlib.sha256(password.encode()).hexdigest())

    if result:
        messagebox.showinfo("Успешный вход", "Вы вошли в систему!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль!")

def register_user():
    """Функция регистрации пользователя."""
    login = entry_register_username.get()
    password = entry_register_password.get()
    password_repeat = entry_register_password_repeat.get()

    if password != password_repeat:
        messagebox.showerror("Ошибка", "Пароли не совпадают!")
        return

    result = add_user(login, hashlib.sha256(password.encode()).hexdigest())

    if not result:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
    else:
        messagebox.showinfo("Успешная регистрация", "Регистрация прошла успешно!")

root = tk.Tk()
root.title("Система авторизации")

label_login_username = tk.Label(root, text="Логин:")
label_login_username.grid(row=0, column=0, padx=10, pady=5)
entry_login_username = tk.Entry(root)
entry_login_username.grid(row=0, column=1, padx=10, pady=5)

label_login_password = tk.Label(root, text="Пароль:")
label_login_password.grid(row=1, column=0, padx=10, pady=5)
entry_login_password = tk.Entry(root, show="*")
entry_login_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Вход", command=login_user)
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

label_register_username = tk.Label(root, text="Логин:")
label_register_username.grid(row=3, column=0, padx=10, pady=5)
entry_register_username = tk.Entry(root)
entry_register_username.grid(row=3, column=1, padx=10, pady=5)

label_register_password = tk.Label(root, text="Пароль:")
label_register_password.grid(row=4, column=0, padx=10, pady=5)
entry_register_password = tk.Entry(root, show="*")
entry_register_password.grid(row=4, column=1, padx=10, pady=5)

label_register_password_repeat = tk.Label(root, text="Повторите пароль:")
label_register_password_repeat.grid(row=5, column=0, padx=10, pady=5)
entry_register_password_repeat = tk.Entry(root, show="*")
entry_register_password_repeat.grid(row=5, column=1, padx=10, pady=5)

button_register = tk.Button(root, text="Зарегистрироваться", command=register_user)
button_register.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()


