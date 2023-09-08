
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

def nuevo_libro():
  
  nuevo_libro_info = registrar_nuevo_libro() 
  return None



def eliminar_ejemplar_libro():
    codigoIngresado = input("Ingrese el código del libro: ")
   
    libro = buscar_libro_por_codigo(codigoIngresado)

    if libro is not None:
        if libro['cantEjemplares'] > 0:
            libro['cantEjemplares'] -= 1
            print("Se eliminó un ejemplar del libro")
        else:
            print("No hay ejemplares disponibles para eliminar")
    else:
        print("No se encontró el libro con el código ingresado")

    return None



def prestar_ejemplar_libro():

    codigoIngresado = input("Ingrese el código del libro: ")
    libro = buscar_libro_por_codigo(codigoIngresado)
    if libro is not None:
        if libro['cantEjPrestados'] < libro['cantEjemplares']:
       
            print(f"Autor: {libro['autor']}")
            print(f"Título: {libro['titulo']}")
            print(f"Cantidad de ejemplares disponibles: {libro['cantEjemplares'] - libro['cantEjPrestados']}")
              
            confirmacion = input("¿Confirmar préstamo? (S/N): ")
            if confirmacion.lower() == "s":
                libro['cantEjPrestados'] += 1 
                print("Préstamo confirmado.")
            else:
                print("Préstamo cancelado")
        else:
            print("No quedan ejemplares para prestar")
    else:
        print("Error: el libro no existe")

    return None








