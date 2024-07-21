# Generador de Contraseñas Seguras

Esta aplicación genera contraseñas seguras y las envía por correo electrónico utilizando SendGrid. La interfaz de usuario está construida con Streamlit.

## Características

- Generación de contraseñas con longitud personalizada.
- Inclusión opcional de letras mayúsculas, símbolos y números.
- Envío de la contraseña generada por correo electrónico.

## Requisitos

- Python 3.x
- Cuenta de SendGrid con una API Key
- Las siguientes bibliotecas de Python:

  - `streamlit`
  - `sendgrid`
  - `python-dotenv`

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

## Estructura del Proyecto

├── src
│   └── password_generator.py
├── app.py
├── .env
├── requirements.txt
└── README.md
