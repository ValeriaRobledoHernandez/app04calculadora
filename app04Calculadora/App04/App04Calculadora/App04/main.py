import flet as ft

def calc_suma(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 + num2
        lblResultado.value = f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value = "Error, ingresa valores correctos"

def calc_resta(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 - num2
        lblResultado.value = f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value = "Error, ingresa valores correctos"

def calc_multiplicacion(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 * num2
        lblResultado.value = f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value = "Error, ingresa valores correctos"

def calc_division(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
    
        resultado = num1 / num2
        lblResultado.value = f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value = "Error, ingresa valores correctos"
def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "purple"
    
    txtNum1 = ft.TextField(label="Ingresa el primer numero: ", color="yellow")
    txtNum2 = ft.TextField(label="Ingresa el segundo numero: ", color="yellow")
    lblResultado = ft.Text("Resultado: ", color="yellow")
    
    btnSuma = ft.ElevatedButton(text="+", on_click=lambda e: calc_suma(txtNum1, txtNum2, lblResultado))
    btnResta = ft.ElevatedButton(text="-", on_click=lambda e: calc_resta(txtNum1, txtNum2, lblResultado))
    btnMultiplicacion = ft.ElevatedButton(text="*", on_click=lambda e: calc_multiplicacion(txtNum1, txtNum2, lblResultado))
    btnDivision = ft.ElevatedButton(text="/", on_click=lambda e: calc_division(txtNum1, txtNum2, lblResultado))
    btnLimpiar = ft.ElevatedButton(text="Limpiar", on_click=lambda e: limpiar(txtNum1, txtNum2, lblResultado, page))

    def limpiar(txtNum1, txtNum2, lblResultado, page):
        txtNum1.value = ""
        txtNum2.value = ""
        lblResultado.value = "Resultado: "
        page.update()

    page.add(
        ft.Column(controls=[
            ft.Row(controls=[txtNum1, txtNum2], alignment="center"),
            ft.Row(controls=[lblResultado], alignment="center"),
            ft.Row(controls=[btnSuma, btnResta, btnMultiplicacion, btnDivision], alignment="center"),
            ft.Row(controls=[btnLimpiar], alignment="center")
        ], alignment="center")
    )

ft.app(main)


