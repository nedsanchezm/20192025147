from flask import Flask, render_template, request, redirect, url_for
from db import db
from Estudiante import Estudiante
class Programa:
    def __init__(self):
        
        self.app=Flask (__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///estudiantes.sqlite3"
        
        #Agregar la db a nuestra aplicación 
        db.init_app(self.app)
        
        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods = ["GET",  "POST"])
        
        #iniciar el servidor
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)    
       
    def buscarTodos(self):
        return render_template('mostrarTodos.html', estudiantes=Estudiante.query.all())
         
    def agregar (self):
        
        #Verificar si debe enviar los datos o procesar los datos

        if request.method=="POST":
            
            #Crear un objeto con los valores que vengan del formulario
            nombre=request.form ['nombre']
            email=request.form ['email']
            codigo=request.form ['codigo']  
            miEstudiante=Estudiante(nombre, codigo, email)
            
            #Guardar el objeto en la db 
            db.session.add(miEstudiante)
            db.session.commit()
            
            return redirect(url_for('buscarTodos'))   
                     
        return render_template('nuevoEstudiante.html')   
    
miPrograma= Programa()    