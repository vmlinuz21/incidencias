import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os
import pdfplumber
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
import re

CARPETA = "/sdcard/tickets"  # 📂 carpeta en Android donde pondrás los PDFs

# --- tus regex y funciones de procesado van aquí ---
# (reutilizas lo que ya tienes de procesar_pdf, extraer_texto_usuario, etc.)
# simplifico por espacio, pero copias el mismo código que ya usamos para
# extraer datos y generar el PDF.

def generar_pdf_de_incidencias():
    salida = "/sdcard/incidencias_extraidas.pdf"
    c = canvas.Canvas(salida, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.red)
    c.drawString(2*cm, 27*cm, "Informe de incidencias")
    c.save()
    return salida

class IncidenciasApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.label = Label(text="Pulsa para generar PDF")
        boton = Button(text="Generar incidencias.pdf")
        boton.bind(on_press=self.generar_pdf)
        layout.add_widget(self.label)
        layout.add_widget(boton)
        return layout

    def generar_pdf(self, instance):
        archivo = generar_pdf_de_incidencias()
        self.label.text = f"✅ PDF generado: {archivo}"

if __name__ == "__main__":
    IncidenciasApp().run()
