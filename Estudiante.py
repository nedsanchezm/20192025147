
from db import db

class Estudiante (db.Model):
    
    #Nombre de la tabla
    
    __tablename_="estudiante"
    
    #conjunto de atributos  qe van a ser los campos de la tabla
    #Llave primaria
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.string(50))
    email=db.Column(db.string(70))
    codigo=db.Column(db.string(15))
    
    #Metodo constructor para mapear  datos a los campos definidos
    
    def __init__(self, nombre, email, codigo):
        
        self.nombre=nombre
        self.email=email
        self.codigo=codigo