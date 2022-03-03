import datetime

def ConsultaUsers(usuarios):
    print("\nUsuarios: \n")
    contador = 1
    for user in usuarios:
         datos = "{0}. C.C.: {1} | Nombre: {2} | Fecha Ingreso: {3} | Rango: {4}"
         print(datos.format(contador, user[0], user[1], user[2], user[3]))
         contador = contador + 1
    print(" ")
    
def pedirDatosRegistro():
     documentocorrecto = False
     while(not documentocorrecto):
          documento = input("Ingrese codigo: ")
          if len(documento) == 6:
               documentocorrecto = True
          else:
               print("Codigo incorrecto: Debe tener 6 digitos")
               
     nombre = input("Ingrese nombre: ")
     
     fecha = datetime.datetime.now()
     
     rangocorrecto = False
     while(not rangocorrecto):
          rango = input("Ingrese el rango: ")
          if rango=="Estudiante":
               rangocorrecto = True
          elif rango=="Profesor":
               rangocorrecto = True
          elif rango=="Empleado":
               rangocorrecto = True
          else:
               print(f"El rango ingresado {rango} no es un rango valido")
     
     usuario = (documento, nombre, fecha, rango)
     return usuario
          