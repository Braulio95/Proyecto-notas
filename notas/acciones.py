import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}. Vamos a crear una nueva nota...")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto. Se ha guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota :(")
    
    def mostrar(self,usuario):
        print(f"\nOk {usuario[1]}. Aquí tienes tus notas:")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n*******************************************")
            print(nota[2])
            print(nota[3])
            print("*******************************************")
    def borrar(self, usuario):
        print(f"\nEntendido {usuario[1]}, vamos a eliminar notas")

        titulo = input("Introduce el título de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        print(eliminar)

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota {nota.titulo}")
        else:
            print("No se ha podido borrar la nota. Intente de nuevo...")

