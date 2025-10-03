[app]

# Nombre que se muestra en el móvil
title = Incidencias PDF

# Nombre interno del paquete (sin espacios ni caracteres raros)
package.name = incidencias

# Dominio inverso (puede ser inventado)
package.domain = org.vicky

# Versión de la app
version = 1.0.0

# Carpeta del código fuente
source.dir = .

# Archivos a incluir
source.include_exts = py,png,jpg,kv,atlas

# Script principal
main.py = main.py

# Librerías de Python que necesita tu app
requirements = python3,kivy,pdfplumber,reportlab

# Orientación de la app
orientation = portrait

# Permisos necesarios en Android
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
