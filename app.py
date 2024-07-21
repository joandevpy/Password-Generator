import os  # Importa el módulo os para interactuar con el sistema operativo.
from sendgrid import SendGridAPIClient  # Importa la clase SendGridAPIClient para interactuar con la API de SendGrid.
from sendgrid.helpers.mail import Mail  # Importa la clase Mail para crear correos electrónicos.
import streamlit as st  # Importa Streamlit y la asigna al alias 'st' para crear aplicaciones web interactivas.
from dotenv import load_dotenv  # Importa la función load_dotenv para cargar variables de entorno desde un archivo .env.
from src.password_generator import generar_password  # Importa la función generar_password desde el módulo password_generator.

# Asegura que el módulo src está en el PATH
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def enviar_mail(password, destinatario):
    # Define una función para enviar correos electrónicos utilizando SendGrid.
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")  # Obtiene la API key de SendGrid de las variables de entorno.
    SENDER_EMAIL = os.environ.get("SENDER_EMAIL")  # Obtiene el correo electrónico del remitente de las variables de entorno.
   
    # Crea un objeto Mail con los detalles del correo electrónico.
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=destinatario,
        subject='Password generado',
        html_content=f'<strong>Tu nuevo Password es: {password}</strong>')

    try:
        # Intenta enviar el correo electrónico utilizando la API de SendGrid.
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        if response.status_code == 202:
            # Verifica si el correo se envió con éxito.
            st.success(f"Password enviado a {destinatario}")
        else:
            # Muestra un mensaje de error si hubo un problema al enviar el correo.
            st.error(f"Error al enviar el correo. Código de estado: {response.status_code}")
            print(f"Respuesta de SendGrid: {response.body}")

    except Exception as e:
        # Captura cualquier excepción y muestra un mensaje de error.
        st.error(f"Error al enviar el correo: {str(e)}")
        print(f"Error detallado: {e}")

def main():
    # Define la función principal de la aplicación Streamlit.
    st.title("Password Generator")  # Establece el título de la aplicación.

    # Añade campos de entrada y casillas de verificación para los parámetros del password.
    longitud = st.number_input("Ingrese la longitud", min_value=1, value=10)
    incluir_mayusculas = st.checkbox("Incluir letras MAYÚSCULAS", value=True)
    incluir_simbolos = st.checkbox("Incluir SÍMBOLOS", value=True)
    incluir_numeros = st.checkbox("Incluir NÚMEROS", value=True)

    destinatario = st.text_input("Ingrese el correo electrónico de destino")

    if st.button("Generar y Enviar PASSWORD"):
        # Genera el password y lo envía por correo cuando se presiona el botón.
        password = generar_password(longitud, incluir_mayusculas, incluir_simbolos, incluir_numeros)
        st.success(f"Su nuevo Password es: {password}")
        
        if destinatario:
            enviar_mail(password, destinatario)
        else:
            st.warning("Por favor, ingrese un correo electrónico válido.")

if __name__ == "__main__":
    main()  # Ejecuta la función principal si este archivo es ejecutado como el script principal.
