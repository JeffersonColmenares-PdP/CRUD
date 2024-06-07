from flask import Flask, request
from config import get_db, close_db

app = Flask(__name__)

@app.route('/consulta')
def consultar():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM elementos_tecnologicos')
    elementos = cur.fetchall()
    cur.close()

    html = '<h1> Elementos Tecnologicos</h1>'
    html += '<table border="1">'
    html += '<tr><th>Numero de serie</th><th>Ciudad</th><th>Precio</th><th>Fecha de fabricacion</th><th>Vendedor</th></tr>'
    for elemento in elementos:
        html += '<tr>'
        for atributo in elemento:
            html += f'<td>{atributo}</td>'
        html += '</tr>'
    html += '</table>'

    return html


@app.route('/elimina', methods=['POST']) # post para solicitar un dato
def eliminar():
    # Obtener el código del elemento tecnologico a eliminar enviado desde el formulario
    numero_serie = request.form['numero_serie']
    
    # Eliminar el registro de la base de datos
    conn = get_db()
    cur = conn.cursor()
    cur.execute(f'DELETE FROM elementos_tecnologicos WHERE numero_serie = {numero_serie}')
    conn.commit()
    cur.close()
    close_db(conn)
    
    return 'Elemento tecnologico' + numero_serie + 'eliminado correctamente'


@app.route('/crear', methods=['POST'])
def crear_elemento():
    # Obtener los datos del formulario
    numero_serie = request.form['numero_serie']
    ciudad = request.form['ciudad']
    precio = request.form['precio']
    fecha_fabricacion = request.form['fecha_fabricacion']
    vendedor = request.form['vendedor']
    
    # Insertar un nuevo registro en la base de datos
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO elementos_tecnologicos (numero_serie, ciudad, precio, fecha_fabricacion, vendedor) VALUES (%s, %s, %s, %s, %s)',
                (numero_serie, ciudad, precio, fecha_fabricacion, vendedor))
    conn.commit()
    return 'Elemento tecnologico' + numero_serie + 'creado correctamente'


@app.route('/actualizar', methods=['POST'])
def actualizar():
    # Obtener datos enviados desde el formulario
    numero_serie = request.form['numero_serie']
    ciudad = request.form['ciudad']
    precio = request.form['precio']
    fecha_fabricacion = request.form['fecha_fabricacion']
    vendedor = request.form['vendedor']
    
    # Actualizar el registro en la base de datos
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE elementos_tecnologicos SET ciudad = %s, precio = %s, fecha_fabricacion = %s, vendedor = %s WHERE numero_serie = %s",
                (ciudad, precio, fecha_fabricacion, vendedor, f"{numero_serie}"))
    conn.commit()
    cur.close()
    close_db(conn)
    
    return 'Registro actualizado correctamente'


if __name__ == '__main__':
    app.run(debug=True)