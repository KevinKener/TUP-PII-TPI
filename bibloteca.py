
import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)



def buscar_libro_por_codigo(codigoIngresado):
    for libro in libros:
        if libro["cod"] == codigoIngresado:
            return libro
    return None


def ejemplares_prestados():
    for libro in libros:
      if libro['cantEjPrestados']>=1:
       
         print(f"Ejemplares Prestados: {libro['cantEjPrestados']} del libro: {libro['titulo']}")
      else:
       print(f"Este libro: {libro['titulo']} no tiene ejemplares prestados")
    return None




from cod_generator import generar

def registrar_nuevo_libro():
    name_nuevo_libro = input("Ingresar nombre del libro: ")
    can_ej_nuevo_libro = int(input("Ingresar cantidad de ejemplares: ")) 
    autor_nuevo_libro = input("Ingresar el autor del libro: ")

    nuevo_cod_libro_nuevo = generar()
   
    nuevo_libro = {"titulo": name_nuevo_libro, "cantEjemplares": can_ej_nuevo_libro,"cantEjPrestados":0 ,"autor":autor_nuevo_libro ,"cod": nuevo_cod_libro_nuevo}

    libros.append(nuevo_libro)
    
    print("Nuevo libro agregado")
    print(f"Nombre del libro: {nuevo_libro['titulo']}")
    print(f"Cantidad de ejemplares: {nuevo_libro['cantEjemplares']}")
    print(f"Autor del libro: {nuevo_libro['autor']}")
    print(f"Codigo: {nuevo_libro['cod']}")
    return None








