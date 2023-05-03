# -*- coding: utf-8 -*-
"""Calculadora
Este proyecto tiene la finalidad de mostrar una calculadora basica
con el modulo de interfaces graficas de Python Tkinter. 

Mas informacion: https://docs.python.org/es/3/library/tkinter.html
"""
from tkinter import Button, Entry, Tk, END
from os.path import join, dirname


ICO_PATH : str = join(dirname(__file__), "style", "ico", "main.ico")


class Calculadora:
    """La clase que contiene la estructura
    de la calculadora
    """

    def __init__(self, master : Tk):
        """define la configuracion de la intefaz grafica

        Args:
            master (tkinter): la ventana que sera modificada
        """
        self.master = master
        master.title("Calculadora")

        # Obtiene las medidas iniciales de la ventana creada
        ancho_pantalla : int = self.master.winfo_screenwidth()
        alto_pantalla : int = self.master.winfo_screenheight()

        # Establecer las dimensiones de la ventana
        ancho_ventana : int = 320
        alto_ventana : int = 340

        # Calcular las coordenadas para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Establecer las coordenadas de la ventana
        self.master.geometry(
            '{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))

        # Se establece que no se puede modificar el tamanio
        self.master.resizable(False, False)

        # Se agrega icono a la ventana
        self.master.iconbitmap(ICO_PATH)

        self.display = Entry(master, width=50, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Creamos los botones
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("/", 4, 3)
        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1, padx=10, pady=10):
        """crea la instancia de un boton con las configuracion
        para la calculadora

        Args:
            text (str): el texto que mostrara el boton
            row (int): la fila donde se posicionara
            column (int): la columna donde se posicionara
            columnspan (int, optional):Defaults to 1.
            padx (int, optional): Defaults to 10.
            pady (int, optional): Defaults to 10.
        """
        button = Button(
            self.master,
            text=text,
            width=5, height=2,
            command=lambda: self.press_key(text)
        )
        button.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx,
            pady=pady
        )

    def press_key(self, key):
        """evalua la operacion y/o agrega el valor a la cola de la operacion

        Args:
            key (str): el caracter que sera agregado
        """
        if key == "C":
            self.display.delete(0, END)
        elif key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(END, key)


if __name__ == "__main__":
    root = Tk()
    calculadora = Calculadora(root)
    root.mainloop()
