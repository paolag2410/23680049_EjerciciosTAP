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