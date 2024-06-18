import bcrypt
import sqlite3

# Función para validar usuario y contraseña
def validar_usuario_contrasena(usuario, contrasena):
    # Conectar a la base de datos
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Obtener la contraseña hasheada desde la base de datos
    cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        hashed_password = resultado[0].encode('utf-8')
        if bcrypt.checkpw(contrasena.encode('utf-8'), hashed_password):
            return True
        else:
            return False
    else:
        return False

# Validación de Usuarios
usuario_ingresado = 'jvicencio'
contrasena_ingresada = 'password123'
if validar_usuario_contrasena(usuario_ingresado, contrasena_ingresada):
    print('Usuario validado correctamente.')
else:
    print('Usuario o contraseña incorrectos.')

