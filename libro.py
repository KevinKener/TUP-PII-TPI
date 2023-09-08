from cod_generator import generar

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def generar_codigo():
    codigo_generado = generar()
    return codigo_generado

def nuevo_libro(autor, titulo, cant_ej_adquiridos):
    #Creacion del diccionario para el nuevo libro y sus respectivos datos.
    codigo = generar_codigo()  
    libro_nuevo = {
        'cod': codigo,
        'autor': autor,
        'titulo': titulo,
        'cant_ej_ad': cant_ej_adquiridos,
        'cant_ej_pr': 0
        }  

    
    print(f"""
          Titulo: {titulo}
          Autor: {autor}
          Código: {codigo}
          Cantidad de ejemplares adquiridos: {cant_ej_adquiridos}
          """)    

    return libro_nuevo