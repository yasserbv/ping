import tkinter as tk
from tkinter import filedialog


class file:
    _instance = None  # Atributo de clase para guardar la instancia única
    _initialized = False

    def __new__(cls):
        if cls._instance is None:  # Verifica si ya existe una instancia
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._token = ""
        self._chatID = ""
        # Evitar reinicializar si ya existe una instancia
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True  # Bandera para evitar reinicialización

    def open_file(self):
        # Abrir el explorador de archivos
        archivo_path = filedialog.askopenfilename(
            title="Selecciona el archivo config.txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if archivo_path:
            # Leer el archivo y obtener el token y chatID
            with open(archivo_path, 'r') as file:
                config = file.readlines()
                self._token = config[0].strip().split(
                    '=')[1]  # Extraer el token
                self._chatID = config[1].strip().split(
                    '=')[1]  # Extraer el chatID
                return self._token, self._chatID
                # Aquí puedes usar el token y el chatID
                # print(f"Token: {token}, Chat ID: {chatID}")

    def get_data(self):
        return self._token, self._chatID
