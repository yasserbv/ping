import customtkinter as ctk
from database import database
from tkinter import ttk


class menu_popup:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(self):

        if self._instance is None:
            self._instance = super().__new__(self)
            self._instance.show_menu()  # Crear la ventana en el primer uso
        else:

            self._instance.añadir_texto()  # Llamar para actualizar el contenido
        return self._instance  # Devuelve la instancia única

    def show_menu(self):
        selecdata = database()
        data, _ = selecdata.read_data()
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

        host = ctk.CTkButton(
            self.button_frame, text="Listado de los hosts", command=lambda: self.update_frame(data))
        host.pack(side="left", padx=5)

        opcion_2 = ctk.CTkButton(self.button_frame, text="Opción 2",
                                 command=self.show_frame_2)
        opcion_2.pack(side="left", padx=5)

        opcion_3 = ctk.CTkButton(self.button_frame, text="Opción 3",
                                 command=self.show_frame_3)
        opcion_3.pack(side="left", padx=5)

        search_data = ctk.CTkEntry(self.button_frame, font=("sans serif", 12), placeholder_text="IP",
                                   text_color=color_orange_2, fg_color=color_white, width=220, height=40)
        search_data.pack(side="left", padx=5)

        bt_search = ctk.CTkButton(self.button_frame, text="Search",
                                  command=lambda: self.update_frame(selecdata.search(search_data.get())), width=10, height=30)
        bt_search.pack(side="left", padx=5)

        # Crear Frames secundarios
        self.frame_1 = self.create_frame_1(data)

        self.frame_2 = self.create_frame(
            "Contenido de la Opción 2", "Este es el contenido de la opción 2.")
        self.frame_3 = self.create_frame(
            "Contenido de la Opción 3", "Este es el contenido de la opción 3.")

        # Mostrar la primera vista por defecto
        self.show_frame(self.frame_1)

    def update_frame(self, search_query):

        if hasattr(self, 'frame_1') and self.frame_1.winfo_exists():
            self.frame_1.destroy()

    # Crea un nuevo frame con los datos filtrados
        self.frame_1 = self.create_frame_1(search_query)
        self.show_frame(self.frame_1)

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

    # Agregar filas
        for fila in host_listing:
            tabla.insert("", "end", values=fila)

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
