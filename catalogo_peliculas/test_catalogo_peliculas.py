from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp

print('Catalogo de peliculas'.center(50,'='))
opcion = None
while opcion != 4:
    try:
        print(f'''
        1) Agregar pelicula
        2) Listar peliculas
        3) Eliminar archivo de peliculas
        4) Salir
        ''')
        opcion = int(input('Eliga una opción: '))

        if opcion == 1:
            entrada = input('Ingresa el nombre de la pelicula a agregar: ')
            pelicula_obj = Pelicula(entrada)
            cp.agregar_pelicula(pelicula_obj)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Salimos del programa!')


    