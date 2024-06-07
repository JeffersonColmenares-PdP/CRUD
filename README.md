# CRUD

# crear el entorno v
python -m venv .venv

# verificar instalacion python
python --version  

# configutracion para que permita ejecutar comandos en terminal vs
Get-ExecutionPolicy -list
Set-ExecutionPolicy RemoteSigned -Force

# activar entorno v
.venv\Scripts\activate  

# instalacion flask
pip install Flask      

# ejecutar programa
flask --app app run    

# sycopg2 es un adaptador entre python y postgres
pip install Flask psycopg2-binary

# creacion de la conexion con DB con un nuevo archivo
config.py

# configurar app.py - import -funciones
    import flask
    import funciones get y close de config.py

    creacion de funciones
        consulta
        eliminar
        crear
        actualizar

# crear formularios en html
    archivo crear.html
    archivo actualizar.html

# comando para crear el requirements con lo que instale
pip freeze > requirements.txt