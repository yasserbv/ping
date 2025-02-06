import customtkinter as ctk


class popup_update:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, text=""):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(text)  # Inicializar la instancia
        return cls._instance  # Devuelve la instancia única

    def __init__(self, text=""):
        self.text = text  # Texto que se mostrará en el popup
        self.app = None  # Ventana principal (inicialmente no existe)
        self.textbox = None  # Cuadro de texto (inicialmente no existe)
        # Referencia al botón en la ventana principal (inicialmente no existe)
        self.boton = None

    def show_popup(self):
        # Guardar la referencia al botón

        # Verificar si la ventana ya está abierta
        if self.app is not None and self.app.winfo_exists():
            self.app.lift()  # Traer la ventana al frente si ya está abierta
            return  # Salir del método sin crear una nueva ventana

        # Crear ventana principal
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

        # Manejar el cierre de la ventana
        self.app.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

    def añadir_texto(self):
        if self.textbox:  # Verificar si self.textbox existe
            self.textbox.delete(1.0, "end")  # Limpiar cualquier texto previo
            self.textbox.insert("end", self.text)  # Añadir el nuevo texto

    # Método para cerrar la ventana
    def cerrar_ventana(self):
        if self.app:
            self.app.destroy()  # Cerrar la ventana
            self.app = None  # Restablecer self.app a None

    # Mostrar ventana
    def run(self):
        if self.app:  # Verificar si self.app existe
            self.app.mainloop()
