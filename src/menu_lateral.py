import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menú Lateral Desplegable")
        self.geometry("800x600")

        # Creamos el contenedor del menú lateral
        self.menu_frame = tk.Frame(self, bg="#2C3E50", width=250, height=600)
        # No permitir que se redimensione automáticamente
        self.menu_frame.pack_propagate(False)
        self.menu_frame.pack(side="left", fill="y")

        # Botones del menú lateral
        self.button_home = tk.Button(
            self.menu_frame, text="Inicio", command=self.show_home, bg="#34495E", fg="white", relief="flat")
        self.button_home.pack(fill="x")

        self.button_about = tk.Button(self.menu_frame, text="Acerca de",
                                      command=self.show_about, bg="#34495E", fg="white", relief="flat")
        self.button_about.pack(fill="x")

        self.button_contact = tk.Button(
            self.menu_frame, text="Contacto", command=self.show_contact, bg="#34495E", fg="white", relief="flat")
        self.button_contact.pack(fill="x")

        # Contenedor para el contenido principal
        self.content_frame = tk.Frame(self, bg="white", width=550, height=600)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Contenido inicial
        self.show_home()

    def show_home(self):
        self.clear_content()
        label = tk.Label(
            self.content_frame, text="Bienvenido a la página de inicio", font=("Arial", 20))
        label.pack(pady=50)

    def show_about(self):
        self.clear_content()
        label = tk.Label(self.content_frame,
                         text="Acerca de mí", font=("Arial", 20))
        label.pack(pady=50)

    def show_contact(self):
        self.clear_content()
        label = tk.Label(self.content_frame,
                         text="Formulario de contacto", font=("Arial", 20))
        label.pack(pady=50)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
