# class relacion directa con un objeto (entidad o objeto)
# def   -acciones o funciones del objeto

class Personas():
    def __init__(self):
        # atributos del objeto
       self.nombre = "leonel" # variable de tipo texto "" ''
       self.edad =  54 # variable de tipo numerico
       self.estatura = 100.0 # variable de tipo decimal
       self. Peso   = 35.6 # variable de tipo decimal

persona =Personas()
persona.edad =  54
persona.estatura =  170
print("nombre: ",persona.nombre," edad: ",persona.edad, " cms: ", persona.estatura)
