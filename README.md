# 23680049_CALCULADORA_TAP

## Guía Completa: Calculadora Interactiva con Flet y Programación Orientada a Objetos

En esta guía aprenderás paso a paso cómo construir una calculadora funcional usando Python, el framework Flet y principios de Programación Orientada a Objetos (POO). A diferencia de una interfaz simple, esta calculadora implementa clases personalizadas para los botones, manejo de estado interno y lógica completa de operaciones matemáticas.

## 1. Configuración del entorno de trabajo

Antes de comenzar, necesitamos tener instalado Python y Flet.

### Instalación de Python

Descarga Python desde su página oficial y durante la instalación marca la opción: y ejecuta el siguiente comando:

 Add Python to PATH

 Verifica la instalación:
```
python --version
```

Instalación de Flet
```
pip install flet
```
### Configuración de Git Bash

Debido a que la consola CMD puede quedarse corta con ciertos comandos más avanzados, utilizaremos Git Bash como alternativa. Durante su instalación, solo debes avanzar con el asistente presionando “Next” en cada paso. Al abrirlo, notarás una ventana parecida a la terminal de Linux, con colores que ayudan a identificar fácilmente las rutas y directorios.

## 2. Estructura General del Proyecto

Tu aplicación no está hecha con funciones sueltas, sino con una clase principal llamada Calculator que se encarga de:

1. Guardar el estado de la operación
2. Controlar qué número se está escribiendo
3. Recordar el operador
4. Realizar el cálculo cuando se presiona =
5. Actualizar el display

Esto es un claro uso de Programación Orientada a Objetos.

## 3. La Clase Calculator (El Cerebro de la App)

```
class Calculator:
```

Esta clase administra toda la lógica de la calculadora.

### Variables importantes dentro del constructor


Variable       →   Función

self.result	   →  Es el display donde se muestran los números

self.current   →  Guarda el número que el usuario está escribiendo

self.operator  →  Guarda el operador seleccionado (+, -, *, /)

self.operand   →   Guarda el primer número antes del operador


Esto permite que la calculadora recuerde el estado de la operación, como una calculadora real.

## 4. Función Principal: button_clicked
```
def button_clicked(self, e):
```
Aquí se identifica qué botón fue presionado leyendo:

```
data = e.control.content
```
### Comportamientos que evalúa:


1. Botón AC → Reinicia toda la operación y limpia la pantalla.
2. Botones numéricos → Concatena los números que el usuario va presionando.
3. Operadores (+, -, *, /) → Guarda el número actual como primer operando y el operador.
4. Botón = → Realiza la operación matemática usando los valores guardados.
   

Este diseño evita usar variables globales y concentra toda la lógica dentro de la clase.

## 5. Creación de Botones Personalizados con @ft.control

Aquí tu código se vuelve más avanzado que el ejemplo.

En lugar de usar botones genéricos, creaste clases de botones:

```
@ft.control
class CalcButton(ft.Button):
```
Y a partir de ella heredan:

1. DigitButton → Botones numéricos
2. ActionButton → Operadores
3. ExtraActionButton → Botones especiales (AC, %, +/-)

Esto es herencia aplicada a la interfaz gráfica.
Cada tipo de botón tiene su propio color y estilo sin repetir código.

## 6. Construcción Visual de la Calculadora

La interfaz está dentro de un ft.Container con estilo moderno:

```
ft.Container(
    width=350,
    bgcolor=ft.Colors.BLACK,
    border_radius=ft.BorderRadius.all(20),
    padding=20,
```
Dentro se organiza con:

1. ft.Column → Organiza todo verticalmente
2. ft.Row → Organiza los botones en filas como una calculadora real

## 7. El Display de Resultados

```
ft.Row(controls=[calc.result], alignment=ft.MainAxisAlignment.END)
```
Aquí se muestra el resultado alineado a la derecha, simulando una calculadora real.

## 8. Organización de los Botones por Filas

Cada fila representa la disposición clásica de una calculadora:

1. Fila 1: AC, +/-, %, /
2. Fila 2: 7, 8, 9, *
3. Fila 3: 4, 5, 6, -
4. Fila 4: 1, 2, 3, +
5. Fila 5: 0, ., =

El botón 0 ocupa doble espacio gracias a:

```
DigitButton(content="0", expand=2)
```

## 9. Actualización de la Pantalla
Después de cada clic, se ejecuta:

```
self.page.update()
```
Esto refresca la interfaz para mostrar los cambios inmediatamente.

## 10. Ejecución de la Aplicación
```
if __name__ == "__main__":
    ft.run(main)
```

## 11. Conceptos de Programación Aplicados

Tu proyecto aplica varios conceptos importantes:

Concepto	                         →     Dónde se aplica

Programación Orientada a Objetos	 →     Clase Calculator

Encapsulamiento                      →     Variables internas que guardan el estado

Herencia                             →     DigitButton, ActionButton, ExtraActionButton

Eventos	                             →     on_click=calc.button_clicked

Diseño de Interfaces                 →     Uso de Container, Row, Column

Manejo de estado	                 →     current, operator, operand


## 12. Código Completo
```
from dataclasses import field

import flet as ft

class Calculator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
        self.current = "" 
        self.operator = None
        self.operand = None


    def button_clicked(self, e):
     data = e.control.content

     # AC
     if data == "AC":
        self.current = ""
        self.operator = None
        self.operand = None
        self.result.value = "0"

     # Número
     elif isinstance(data, str) and data.isdigit():
        self.current += data
        self.result.value = self.current

     # Operadores
     elif data in ["+", "-", "*", "/"]:
        if self.current:
            self.operand = float(self.current)
            self.operator = data
            self.current = ""

     # Igual
     elif data == "=":
        if self.current and self.operator and self.operand is not None:
            second = float(self.current)

            if self.operator == "+":
                res = self.operand + second
            elif self.operator == "-":
                res = self.operand - second
            elif self.operator == "*":
                res = self.operand * second
            elif self.operator == "/":
                res = self.operand / second

            self.result.value = str(res)
            self.current = str(res)
            self.operator = None
            self.operand = None

     self.page.update()


    


def main(page: ft.Page):
    page.title = "Calc App"
    calc = Calculator(page)
    calc.result= ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    @ft.control
    class CalcButton(ft.Button):
        expand: int = field(default_factory=lambda: 1)

    @ft.control
    class DigitButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.WHITE_24
        color: ft.Colors = ft.Colors.WHITE

    @ft.control
    class ActionButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.ORANGE
        color: ft.Colors = ft.Colors.WHITE

    @ft.control
    class ExtraActionButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
        color: ft.Colors = ft.Colors.BLACK

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[calc.result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(
                        controls=[
                            ExtraActionButton(content="AC",on_click=calc.button_clicked),
                            ExtraActionButton(content="+/-",on_click=calc.button_clicked),
                            ExtraActionButton(content="%",on_click=calc.button_clicked),
                            ActionButton(content="/",on_click=calc.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(content="7",on_click=calc.button_clicked),
                            DigitButton(content="8",on_click=calc.button_clicked),
                            DigitButton(content="9",on_click=calc.button_clicked),
                            ActionButton(content="*",on_click=calc.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(content="4",on_click=calc.button_clicked),
                            DigitButton(content="5",on_click=calc.button_clicked),
                            DigitButton(content="6",on_click=calc.button_clicked),
                            ActionButton(content="-",on_click=calc.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(content="1",on_click=calc.button_clicked),
                            DigitButton(content="2",on_click=calc.button_clicked),
                            DigitButton(content="3",on_click=calc.button_clicked),
                            ActionButton(content="+",on_click=calc.button_clicked),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton(content="0", expand=2,on_click=calc.button_clicked),
                            DigitButton(content=".",on_click=calc.button_clicked),
                            ActionButton(content="=",on_click=calc.button_clicked),
                        ],
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
```
## Resultado del codigo 
<img width="366" height="334" alt="image" src="https://github.com/user-attachments/assets/cde45209-b5e0-429d-81d6-b779d4bbdf91" />

