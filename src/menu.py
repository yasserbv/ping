import customtkinter as ctk
from database import database
from tkinter import ttk
import threading


class menu_popup:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(self):
        self.stop_thread = False
        self.thread = None
        self.selecdata = database()
        if self._instance is None:
            self._instance = super().__new__(self)
            self._instance.show_menu()  # Crear la ventana en el primer uso
        else:

            self._instance.añadir_texto()  # Llamar para actualizar el contenido
        return self._instance  # Devuelve la instancia única

    def show_menu(self):

        data, _ = self.selecdata.read_data()
        color_orange_2 = "#f37f40"
        color_white = "#FFFFFF"
        # Crear ventana principal solo si no existe
        ctk.set_appearance_mode("light")  # Modo de apariencia
        self.app = ctk.CTk()  # Ventana principal
        self.app.title("Menu Popup")
        self.app.geometry("900x300+300+150")
        self.app.minsize(450, 400)
        # Crear un Frame principal que contendrá los Frames secundarios
        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # frame de los Botones del menú
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(side="top", fill="x", pady=10)

        self.host = ctk.CTkButton(
            self.button_frame, text="Listado de los hosts", command=lambda: self.star_thread_frame())
        self.host.pack(side="left", padx=5)

        self.opcion_2 = ctk.CTkButton(self.button_frame, text="Opción 2",
                                      command=self.show_frame_2)
        self.opcion_2.pack(side="left", padx=5)

        self.opcion_3 = ctk.CTkButton(self.button_frame, text="Opción 3",
                                      command=self.show_frame_3)
        self.opcion_3.pack(side="left", padx=5)

        self.search_data = ctk.CTkEntry(self.button_frame, font=("sans serif", 12), placeholder_text="IP",
                                        text_color=color_orange_2, fg_color=color_white, width=220, height=40)
        self.search_data.pack(side="left", padx=5)

        bt_search = ctk.CTkButton(self.button_frame, text="Search",
                                  command=lambda: self.stop_thread_frame(False), width=10, height=30)
        bt_search.pack(side="left", padx=5)

        # Crear Frames secundarios
        self.frame_1 = self.create_frame_1(data)

        self.frame_2 = self.create_frame(
            "Contenido de la Opción 2", "Este es el contenido de la opción 2.")
        self.frame_3 = self.create_frame(
            "Contenido de la Opción 3", "Este es el contenido de la opción 3.")

        # Mostrar la primera vista por defecto
        self.show_frame(self.frame_1)
        self.star_thread_frame()

    def update_frame(self, query, frame, name_frame):

        if hasattr(self, name_frame) and frame.winfo_exists():
            frame.destroy()

    # Crea un nuevo frame con los datos filtrados
        frame = self.create_frame_1(query)
        self.show_frame(frame)

    def update_frame_periodically(self):
        while not self.stop_thread:
            selecdata = database()
            data, _ = selecdata.read_data()
            self.update_frame(data, self.frame_1, "frame_1")
            threading.Event().wait(2)

    def star_thread_frame(self):
        self.stop_thread = False
        self.thread = threading.Thread(target=self.update_frame_periodically)
        self.thread.daemon = True
        self.thread.start()
        print("hilo iniciado")

    def stop_thread_frame(self, value):
        self.stop_thread = True
        self.update_frame(self.selecdata.search(
            self.search_data.get()), self.frame_1, "frame_1")
        if self.thread:
            self.thread.join()  # Espera a que el hilo finalice
        print("Hilo detenido.")

    def create_frame(self, title, content):
        """Crear un CTkFrame con título y contenido."""
        frame = ctk.CTkFrame(self.main_frame)
        title_label = ctk.CTkLabel(frame, text=title, font=("Arial", 18))
        title_label.pack(pady=10)
        content_label = ctk.CTkLabel(frame, text=content)
        content_label.pack(pady=5)
        return frame

    def create_frame_1(self, host_listing):

        frame = ctk.CTkFrame(self.main_frame)
        columnas = ("ID", "Nombre Host", "IP", "Estado")
        tabla = ttk.Treeview(frame, columns=columnas, show="headings")
        tabla.pack(fill="both", expand=True)

        # Agregar encabezados
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")
            tabla.tag_configure("error", background="#8B0000")
            tabla.tag_configure("default", background="#FFFFFF")

    # Agregar filas
        for fila in host_listing:

            # print(fila)
            state = fila[-1]
            if state == 0:
                tabla.insert("", "end", values=fila, tags=("error",))
            else:
                tabla.insert("", "end", values=fila, tags=("default",))

        return frame

    def show_frame(self, frame):
        """Mostrar el frame seleccionado y ocultar los demás."""
        for child in self.main_frame.winfo_children():
            if isinstance(child, ctk.CTkFrame) and child != self.button_frame:
                child.pack_forget()
        frame.pack(fill="both", expand=True)

    def show_frame_1(self):
        self.show_frame(self.frame_1)

    def show_frame_2(self):
        self.show_frame(self.frame_2)

    def show_frame_3(self):
        self.show_frame(self.frame_3)

    def run(self):
        self.app.mainloop()
