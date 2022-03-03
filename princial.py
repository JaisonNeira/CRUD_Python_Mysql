from ast import Try
from Conexion.BDconexion import DAO
import funciones

def menu():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("::::::::::::MENU PRINCIPAL::::::::::::")
            print("1- Lista usuarios")
            print("2- Registrar usuario")
            print("5- Salir")
            print("::::::::::::::::::::::::::::::::::::::")
            
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion<1 or opcion>5:
                print("Opcion incorrecta, intentelo nuevamente")
            elif opcion ==5:
                continuar = False
                print("Gracias por usar :)")
                break
            else: 
                opcionCorrecta = True
                ejecutarOpcion(opcion)
            
def ejecutarOpcion(opcion):
    dao = DAO()     
    
    if opcion == 1:
        try:
            usuarios = dao.llamarUser()
            if len(usuarios) > 0:
                funciones.ConsultaUsers(usuarios)
            else:
                print("No se encontraron usuarios...")
        except:
            print("Error 001:try")    
    elif opcion ==2:
        user = funciones.pedirDatosRegistro()
        try:
            dao.registrarUser(user)
        except:
            print("Error 002:try")
    
    elif opcion ==3:
        print("3")
    elif opcion ==4:
        print("4")
    else:
        print("Opcion no valida")
       


menu()