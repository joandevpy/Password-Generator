import string  # Importa el módulo string que contiene varias constantes de cadena útiles.
import random  # Importa el módulo random que permite realizar operaciones aleatorias.

def generar_password(longitud, incluir_mayusculas, incluir_simbolos, incluir_numeros):
    # Define una función para generar una contraseña con los parámetros especificados.
    caracteres = string.ascii_lowercase  # Siempre incluye letras en minúsculas.

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Añade letras mayúsculas si se selecciona.

    if incluir_simbolos:
        caracteres += string.punctuation  # Añade símbolos si se selecciona.

    if incluir_numeros:
        caracteres += string.digits  # Añade números si se selecciona.

    # Genera la contraseña seleccionando aleatoriamente caracteres del conjunto permitido.
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password  # Retorna la contraseña generada.
