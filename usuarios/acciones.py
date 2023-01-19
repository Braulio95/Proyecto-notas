#Se importan los modulos usuario del paquete usuarios y las acciones del paquete de notas
import usuarios.usuario as modelo #El modulo usuario se aloja en la variable "modelo"
import notas.acciones

#Se crea la clase acciones que realizará los funciones principales de usuarios del programa
class Acciones:
    #Función registro: realiza las acciones relacionadas al registro de usuarios.
    def registro(self):
        #Se ejecuta el bloque de instrucciones que pide datos al usuario.
        print("\nOk! Vamos a registrarte en el sistema...")
        nombre = input("Ingresa un tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Ingresa tu eMail: ")
        password = input("Ingresa tu contraseña: ")
        # Se llama a la clase Usuario y se toman como parametros los datos ingresados por el usuario
        # y se alojan en la variable usuario
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        #Se ejecuta el metodo registrar de la clase Usuario y se aloja en la variable registro:
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto! Bienvenido {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("Ok! Indentificate en el sistema...")
        try: 
            email = input("Ingresa tu eMail: ")
            password = input("Ingresa tu contraseña: ")
            
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\nBienvenido {login[1]} te has registrado en el sistema el día {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Los datos no coinciden, vuelve a intentarlo :(")

    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles:
        - Crear nota(crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir(salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion.lower() == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion.lower() == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion.lower() == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion.lower() == "salir":
            print(f"¡Hasta pronto! {usuario[1]}")
            exit()