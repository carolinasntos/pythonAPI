from flask import request, jsonify
from src.db import get_db_connection, release_db_connection

def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM usuario')
        usuarios = cursor.fetchall()
        result = [
            {'id': usuario[0], 'nombre': usuario[1], 'apellido': usuario[2], 'email': usuario[3]}
            for usuario in usuarios
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        release_db_connection(conn)

def get_usuario_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM usuario WHERE idusuario = %s', (id,))
        usuario = cursor.fetchone()
        if usuario is None:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        result = {'id': usuario[0], 'nombre': usuario[1], 'apellido': usuario[2], 'email': usuario[3]}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        release_db_connection(conn)

def create_usuario():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    contraseña = data.get('contraseña')

    # Validar que todos los campos obligatorios estén presentes
    if not nombre or not apellido or not email or not contraseña:
        return jsonify({'message': 'Todos los campos son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Insertar el nuevo usuario en la base de datos
        cursor.execute('INSERT INTO usuario (nombre, apellido, email, contraseña) VALUES (%s, %s, %s, %s) RETURNING idusuario',
                       (nombre, apellido, email, contraseña))
        new_id = cursor.fetchone()[0]
        conn.commit()
        return jsonify({'id': new_id, 'nombre': nombre, 'apellido': apellido, 'email': email})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        release_db_connection(conn)

def update_usuario(id):
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    contraseña = data.get('contraseña')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE usuario SET nombre = %s, apellido = %s, email = %s, contraseña = %s WHERE idusuario = %s',
                       (nombre, apellido, email, contraseña, id))
        if cursor.rowcount == 0:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        conn.commit()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        release_db_connection(conn)

def delete_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM usuario WHERE idusuario = %s', (id,))
        if cursor.rowcount == 0:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        conn.commit()
        return jsonify({'message': f'Usuario con id {id} eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        release_db_connection(conn)