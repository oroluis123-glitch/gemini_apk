import flet as ft
from google import genai

def main(page: ft.Page):
    page.title = "Asistente Gemini"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    api_key_field = ft.TextField(label="Ingresa tu API Key de Gemini", password=True, can_reveal_password=True, width=300)
    status_text = ft.Text(value="", color=ft.colors.GREEN)

    def conectar_gemini(e):
        if not api_key_field.value:
            status_text.value = "Por favor ingresa una API Key válida."
            status_text.color = ft.colors.RED
            page.update()
            return

        try:
            client = genai.Client(api_key=api_key_field.value)
            status_text.value = "¡Conectado exitosamente con Gemini!"
            status_text.color = ft.colors.GREEN
        except Exception as ex:
            status_text.value = f"Error: {str(ex)}"
            status_text.color = ft.colors.RED
        page.update()

    btn_conectar = ft.ElevatedButton(text="Conectar Asistente", on_click=conectar_gemini)

    page.add(
        api_key_field,
        btn_conectar,
        status_text
    )

ft.app(target=main)
