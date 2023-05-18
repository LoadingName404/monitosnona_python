import mysql.connector
print('Conectando con la base de datos...')

noterminado = "Opcion aun no hecha"
# i para los ciclos
iniciar_sesion = True #Ciclo inicio de secion
iConectarseDB = True #Ciclo para intentar conectarse a la base de datos
iPreguntarConectarseDB = True #Ciclo para preguntar si intentar otra vez conectarse a la base de datos


while iConectarseDB == True:
    try:
        conexion = mysql.connector.connect(
        host="sql.chukman.online",
        user="monitosnona",
        password="Inacap.2022",
        database="monitosnona",
        )
        print('Conexion exitosa')
        iConectarseDB = False
    except:
        print('No se pudo conectar con la base de datos')
        iPreguntarConectarseDB = True
        while iPreguntarConectarseDB == True:
            opcion = input('Intentar denuevo?(S/N)').lower()
            if opcion == 's' or opcion == 'si':
                print('Intentado otra vez...')
                iPreguntarConectarseDB = False
            elif opcion == 'n' or opcion == 'no':
                print('Adios')
                iConectarseDB = False
                iPreguntarConectarseDB = False
                iniciar_sesion = False
            elif opcion == 'local':
                try:
                    conexion = mysql.connector.connect(
                    host="192.168.1.141",
                    user="monitosnona",
                    password="Inacap.2022",
                    database="monitosnona",
                    )
                    print('Conexion exitosa')
                    iConectarseDB = False
                    iPreguntarConectarseDB = False
                except:
                    print('tampoco funciono')
            else:
                print('Opcion no valida.')

class Acciones:
    def show_tables():
        cursor = conexion.cursor()
        cursor.execute("show tables")
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(resultado)

    def select_table():
        tabla = input("Que tabla desea ver?: ")
        cursor = conexion.cursor()
        try:
            cursor.execute("select * from {}".format(tabla))
            resultados = cursor.fetchall()
            for resultado in resultados:
                if resultado == "":
                    print("la tabla esta vacia")
                else:
                    print(resultado)
        except mysql.connector.Error as e:
            if e.errno == 1146:
                print("La tabla {} no existe.".format(tabla))
            else:
                raise e
            
    def buscar_usuario(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = '{}'".format(self))
        resultados = cursor.fetchall()
        resultados = str(resultados)
        if resultados == "[]":
            print("Usuario no encontrado.")
        else:
            print(resultados)
            print("Errores: ")

    def insertar_usuario():
        usuario = input("Ingrese el nombre del usuario: ")
        contra = input("Ingrese la contraseña que va a tener el usuario: ")
        i = True
        while i == True:
            cargo = input("""
1.- Jefe de ventas
2.- Vendedor
Ingrese el cargo del usuario: """)
            if cargo == "1":
                i = False
            elif cargo == "2":
                i = False
            elif cargo == "11":
                print("Chupalo entonces")
            else:
                print("Opcion no valida")
        cursor = conexion.cursor()
        cursor.execute("insert into usuario(nombre_usuario,contraseña,cargo) values('{}','{}','{}')".format(usuario,contra,cargo))
        conexion.commit()
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(resultado)
    
    def borrar_usuario():
        usuario = input("Ingrese el nombre del usuario que desea borrar: ")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuario WHERE nombre_usuario = '{}'".format(usuario))
        conexion.commit()
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(resultado)

    def iniciar_secion():
        i1 = True
        usuario = input("Ingrese el nombre de usuario: ")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = '{}'".format(usuario))
        resultados = cursor.fetchall()
        resultados = str(resultados)
        if resultados == "[]":
            print("Usuario no encontrado.")
            i1 = False
        while i1 == True:
            contra = input("Ingresa la contraseña: ")
            cursor = conexion.cursor()
            cursor.execute("SELECT contraseña FROM usuario WHERE nombre_usuario = '{}'".format(usuario,contra))
            resultados = cursor.fetchall()
            resultados = str(resultados)
            if "[('{}',)]".format(contra) != resultados:
                print("Contraseña incorrecta.")
                salir = False
                while salir == False:
                    salir = input("Intenarlo otra vez?(S/N): ").lower()
                    if salir == "s" or salir == "si":
                        salir = True
                    elif salir == "n" or salir == "no":
                        salir = True
                        i1 = False
                    else:
                        print("Opcion no valida")
                        salir = False
            else:
                i1 = False
                print("Contraseña correcta.")
                cursor = conexion.cursor()
                cursor.execute("SELECT cargo FROM usuario WHERE nombre_usuario = '{}'".format(usuario))
                resultados = cursor.fetchall()
                resultados = str(resultados)
                if resultados == "[(1,)]":
                    Menus.menu_jefe()
                else:
                    Menus.menu_vendedor()

class Menus:
    def menu_vendedor():
        i = True
        while i == True:
            opcion = input("""
#######
#
# Menu de vendedor
#
#######
#
# 1.- Agregar productos a ser adquiridos por un potencial cliente
# 2.- 
# 3.-
#
# 0.- Cerrar sesion
#
#######
Opcion: """)
            if opcion == "1":
                pass
            elif opcion == "0":
                i = False
            else:
                print("Opcion no valida.")

    def menu_jefe():
        i = True
        while i == True:
            opcion = input("""
#######################################
#                                     #
# Menu de jefe de ventas              #
#                                     #
#######################################
#                                     #
# Que desea hacer?                    #
# 1.- Agregar productos al inventario #
# 2.- Obtener las ventas del día      #
# 3.- Cerrar dia de ventas            #
# 4.- Abrir dia de ventas             #
#                                     #
# 0.- Cerrar sesion                   #
#                                     #
#######################################
Opcion: """)
            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "0":
                i = False
            else:
                print("Opcion no valida")

    def menu_desarrollador():
        i = True
        while i == True:
            opcion = input("""
1.- Mostrar tablas existentes
2.- Ver contenido de una tabla
3.- Buscar usuario
4.- Insertar usuario
5.- Borrar usuario

0.- Volver
: """)
            if opcion == "1":
                Acciones.show_tables()
            elif opcion == "2":
                Acciones.select_table()
            elif opcion == "3":
                usuario = input("Ingrese nombre de usuario: ")
                Acciones.buscar_usuario(usuario)
            elif opcion == "4":
                Acciones.insertar_usuario()
            elif opcion == "5":
                Acciones.borrar_usuario()
            elif opcion == "0":
                i = False
            else:
                print("Opcion no valida")
            

while iniciar_sesion == True:
    opcion = input("""
###################################
#                                 #
# Bienvenido al sistema de ventas #
#                                 #
###################################
#                                 #
# 1.- Iniciar secion              #
#                                 #
# 0.- Cerrar Programa             #
#                                 #
###################################
Opcion: """)

    if opcion == "comando":
        Menus.menu_desarrollador()
    elif opcion == "1":
        Acciones.iniciar_secion()
    elif opcion == "0":
        print("Adios.")
        iniciar_sesion = False
        conexion.close()
    else:
        print("Opcion no valida.")
