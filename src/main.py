import customtkinter as ctk
import tkinter as tk
import os
import threading
from poppu import popup
from data_in import data
from ping import connected_hosts
from select_file import file
from send_data import data_ping


# Cambiar el modo de apariencia
ctk.set_appearance_mode("light")
data_1 = data()
file_1 = file()

# Paleta de colores
color_blue = "#104C64"
color_orenge = "#B6410F"
color_white = "#FFFFFF"
color_orange_2 = "#f37f40"

# Configuración de la ventana principal
app = ctk.CTk()
app.title("PING")
app.geometry("400x400+500+150")
app.minsize(400, 400)
app.maxsize(400, 400)

# Creación del marco
frame = ctk.CTkFrame(app, fg_color=color_blue)
frame.grid(column=0, stick="nsew", padx=20, pady=20)
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Colocar la imagen del logo
base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, 'img', 'icono_ping.png')
icon = tk.PhotoImage(file=image_path)
ctk.CTkLabel(frame, image=icon).grid(columnspan=2, row=0, pady=10)

# Entradas de texto
ip_entry = ctk.CTkEntry(frame, font=("sans serif", 12), placeholder_text="IP",
                        text_color=color_orange_2, fg_color=color_white, width=220, height=40)
ip_entry.grid(columnspan=2, row=1, padx=80, pady=7)

ip_name_entry = ctk.CTkEntry(frame, font=("sans serif", 12), placeholder_text="IP NAME",
                             text_color=color_orange_2, fg_color=color_white, width=220, height=40)
ip_name_entry.grid(columnspan=2, row=2, padx=50, pady=7)

# Botones
bt_add = ctk.CTkButton(frame, font=("sans serif", 12), fg_color=color_orenge, hover_color=color_orange_2,
                       corner_radius=12, border_width=2, text="ADD IP", height=40, width=200, command=lambda: take_data())
bt_add.grid(columnspan=2, row=4, padx=50, pady=10)

bt_start = ctk.CTkButton(frame, font=("sans serif", 12), fg_color=color_orenge, hover_color=color_orange_2,
                         corner_radius=12, border_width=2, text="START", height=40, width=100, command=lambda: start())
bt_start.grid(column=0, row=5, padx=40, pady=0)

bt_search_file = ctk.CTkButton(frame, font=("sans serif", 12), fg_color=color_orenge, hover_color=color_orange_2,
                               corner_radius=12, border_width=2, text="SEARCH FILE", height=40, width=100, command=lambda: open_file())
bt_search_file.grid(column=1, row=5, padx=40, pady=0)


def poppu(dato):
    popup_1 = popup(dato)
    popup_1.run()


def take_data():
    ip = ip_entry.get()
    ip_name = ip_name_entry.get()
    poppu(data_1.data_analysis(ip, ip_name))


def sending_information():
    token, chatID = file_1.get_data()
    print(f"token and id {token},{chatID}")
    hosts = connected_hosts(data_1.retun_data(), token, chatID)
    hosts.ping_hosts()


def sending_information_periodically():
    token, chatID = file_1.get_data()
    hosts = connected_hosts(data_1.retun_data(), token, chatID)
    while True:
        hosts.ping_hosts()
        threading.Event().wait(5)  # Espera 5 segundos antes de volver a ejecutar


def start_sending_thread():
    # Crea un hilo separado para la ejecución de `sending_information_periodically`
    hilo = threading.Thread(target=sending_information_periodically)
    hilo.daemon = True
    hilo.start()


def open_file():
    file_txt = file()
    file_txt.open_file()


def start():
    token, chatID = file_1.get_data()
    if token == "" or chatID == "":
        popup_1 = popup("seleccione el archivo config.txt")
        popup_1.run()
    else:
        sending_info = data_ping(token, chatID)
        sending_info.sending_data("proceso iniciado")
        start_sending_thread()


app.mainloop()
