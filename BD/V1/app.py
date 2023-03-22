from flask import Flask

app=Flask(__name__)

@app.route('/',methods=["GET"])
def init():

    return "sexoooo"

@app.route('/Docentes')
def listadoDocentes():
    respuesta={"nombre":"Juan","Apelidos":"De la garza"}
    return respuesta

@app.route('/Docentes/TrayectoriaProfesional')
def TrayectoriaProfesional():
    respuesta={"nombre":"Juan","Apelidos":"De la garza"}
    return respuesta

@app.route('/Docentes/TrayectoriaProfesional/<int:id>')
def TrayectoriaProfesionalEditar(id):
    respuesta={"nombre":"Fackiu","Apelidos":"De la garza", "mensaje": "editando trayectoria del id: "+ str(id)}
    return respuesta

@app.route('/Docentes/TrayectoriaProfesional/<string:nc>')
def TrayectoriaProfesionalEliminar(nc):
    respuesta={"nombre":"Fackiu","Apelidos":"De la garza", "mensaje": "Eliminando trayectoria del Docente: "+ str(nc)}
    return respuesta

if __name__=='__main__':
    app.run(debug=True)

