import bcrypt
import sqlite3

# Función para almacenar usuario y contraseña hasheada en la base de datos
def almacenar_usuario_contrasena(usuario, contrasena):
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    
    # Conectar a la base de datos (en este caso SQLite para fines demostrativos)
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (usuario TEXT PRIMARY KEY, contrasena TEXT)''')
    
    # Insertar usuario y contraseña hasheada en la base de datos
    cursor.execute('INSERT INTO usuarios VALUES (?, ?)', (usuario, hashed_password.decode('utf-8')))
    
    conn.commit()
    conn.close()

# Creación de Usuarios
usuario = 'jvicencio'
contrasena = 'password123'
almacenar_usuario_contrasena(usuario, contrasena)
