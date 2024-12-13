import customtkinter as ctk


class popup:
    _instance = None  # Variable de clase para almacenar la instancia única

    text = ""

    def __new__(cls, text=""):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.text = text  # Iniciar el texto con lo que se pase al crear la instancia
            cls._instance.show_popup()  # Crear la ventana en el primer uso
        else:
            cls._instance.text = text  # Actualizar el texto si ya existe la instancia
            cls._instance.añadir_texto()  # Llamar para actualizar el contenido
        return cls._instance  # Devuelve la instancia única

    def show_popup(self):
        # Crear ventana principal solo si no existe
        ctk.set_appearance_mode("light")
        self.app = ctk.CTk()
        self.app.title("Popup")
        self.app.geometry("300x300+500+150")
        self.app.minsize(300, 300)
        self.app.maxsize(300, 300)

        # Crear cuadro de texto
        self.textbox = ctk.CTkTextbox(self.app, width=300, height=400)
        self.textbox.pack(pady=20)
        self.añadir_texto()  # Añadir el texto al abrir el popup

    def añadir_texto(self):
        self.textbox.delete(1.0, "end")  # Limpiar cualquier texto previo
        self.textbox.insert("end", self.text)  # Añadir el nuevo texto

    # Mostrar ventana
    def run(self):
        self.app.mainloop()
