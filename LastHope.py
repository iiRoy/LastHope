#Librerías
import random
import os
import time
import sys

"""
LEYENDA:
  1. "*" = Espacio sin disparar.
  2. "O" = Parte de una nave
  3. "0000" = Una nave.
  4. "X" = Proyectil lanzado que le dio a una parte de una nave.
  5. " " = Proyectil lanzado que no le dio a nada.

  Contraseña: AAJRR.
  
Descripción:
  En una matriz de 10x10 hay 8 naves de una longitud desconocida. El jugador obtendrá 50 
  intentos para derribar las naves. Las naves no se colocan de forma diagonal. De igual 
  forma se marcará cuando se acierte o se falle un tiro. Se ganará el juego cuando         se impacten todas las casillas donde se ubican las naves, en caso contrario se 
  perderá. Para realizar un tiro hará falta ingresar una coordenada. 
"""
#VARIABLES DEL JUEGO
# Variable global para número de naves
num_naves = 0
# Variable global para proyectiles disponibles
proyectiles = 0
# Variedad global para tablero.
tablero = [[]]
# Variable global tamaño del tablero.
tam_tablero = 10
# Variable global para determinar si se ha acabado el juego.
game_over = False
# Variable global para contar cuántas naves han sido destruidas.
puntos = 0
# Variable global para determinar la posición de las naves.
posiciones = [[]]
# Variable para el alfabeto.
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Modo programador
mostrar = False
#Número de intentos
intentos = 0
#Confirmación
confirmacion=0
#Escena modo historia
scene=-1
#Valor del tiempo de proyección de texto
timer=0.05
#Activador de menu de escenas
lockscene=0

#Diálogos Modo Historia
line1="\033[1m[Bitácora del capitán]:\033[0m Eres el capitán \nmilitar de la última flota espacial de la \nhumanidad, despues de que la tierra fuera \nconsiderada inhabitable debido a R̸̛̺̥̪̿̕͠Ḙ̸̦̩̉̃̎̂͝D̵̨͕̍̉̈́̇A̶̢̡̧͚̭̋͌͆̃̈́C̸̙͆͐͂T̷̨̗̫͑A̶͕͛D̷̫͙̬̋́Ǫ̶͍͆͝  \nla humanidad fue en busca de un nuevo hogar. \nA la mitad de la travesía la nave es \natacada por una flota de una raza de \nalienigenas llamada R̸̛̺̥̪̿̕͠Ḙ̸̦̩̉̃̎̂͝D̵̨͕̍̉̈́̇A̶̢̡̧͚̭̋͌͆̃̈́C̸̙͆͐͂T̷̨̗̫͑A̶͕͛D̷̫͙̬̋́Ǫ̶͍͆͝, la \nsupervivencia de la raza humana depende ti. \n\nDestruye a las naves enemigas \nantes de que ellas te destruyan a ti..."

line2="\033[1m[Bitácora del capitán]:\033[0m El teniente \nllamado R̸̛̺̥̪̿̕͠Ḙ̸̦̩̉̃̎̂͝D̵̨͕̍̉̈́̇A̶̢̡̧͚̭̋͌͆̃̈́C̸̙͆͐͂T̷̨̗̫͑A̶͕͛D̷̫͙̬̋́Ǫ̶͍͆͝  te informa que \nexiste la gran posibilidad de \nque los alienigenas por \nquienes han sido atacados \nantes, vivan en un planeta habitable \npara los seres humanos. Al \ntener el conocimiento de esta \ninformación se te dan las ordenes \nde cambiar el curso hacia la \ndirección de los enemigos."

line3="\033[1m[Bitácora del capitán]:\033[0m La nave ha \nllegado hacia el planeta madre \nde la raza R̸̛̺̥̪̿̕͠Ḙ̸̦̩̉̃̎̂͝D̵̨͕̍̉̈́̇A̶̢̡̧͚̭̋͌͆̃̈́C̸̙͆͐͂T̷̨̗̫͑A̶͕͛D̷̫͙̬̋́Ǫ̶͍͆͝  ahora la \núltima eperanza es solo es \nuna lucha por la supervivencia, \nno dejes a ninguno con vida."

line4="\033[1m[Bitácora del capitán]:\033[0m No queda \nrastro de ningun miembro de \nla raza R̸̛̺̥̪̿̕͠Ḙ̸̦̩̉̃̎̂͝D̵̨͕̍̉̈́̇A̶̢̡̧͚̭̋͌͆̃̈́C̸̙͆͐͂T̷̨̗̫͑A̶͕͛D̷̫͙̬̋́Ǫ̶͍͆͝  y parece ser \nque el nuevo mundo es habitable \npara los seres humanos, este \nmundo sera la última esperanza para la \nhumanidad, pero... \n\n\033[1m¿En verdad nos lo merecemos?\033[0m"

#Títulos
def titulo():
    print(
      "\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t     L A S T    H O P E\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n"
    )

def titulop():
        print("\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t\t\tP R O G R A\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °")

def tituloa():
  print("\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t\t\t A R C A D E\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °")

def tituloh():
  print("\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t\t  H I S T O R I A\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °")

def titulom():
  print("\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t\t\t  M E N Ú\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °")

def tituloo():
  print("\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °\n\t\t\t\t   O P C I O N E S\n\t\t\t° ° ° ° ° ° ° ° ° ° ° ° ° °")

def titulomain():
  global scene
  global timer
  print("\n██╗░░░░░░█████╗░░██████╗████████╗ \n██║░░░░░██╔══██╗██╔════╝╚══██╔══╝ \n██║░░░░░███████║╚█████╗░░░░██║░░░ \n██║░░░░░██╔══██║░╚═══██╗░░░██║░░░\n███████╗██║░░██║██████╔╝░░░██║░░░\n╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░\n\n\t██╗░░██╗░█████╗░██████╗░███████╗\n\t██║░░██║██╔══██╗██╔══██╗██╔════╝\n\t███████║██║░░██║██████╔╝█████╗░░\n\t██╔══██║██║░░██║██╔═══╝░██╔══╝░░\n\t██║░░██║╚█████╔╝██║░░░░░███████╗\n\t╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝")
  time.sleep(5)
  os.system('clear')
  scene=-1
  timer=0.05

titulomain()

def creditos():
  titulo()
  print("\tEquipo:\n\t\tJulio César Madrigal John - A01737106.\n\t\tRestituto Lara Larios - A01737216.\n\t\tRodrigo López Guerra - A01737437.\n\t\tAlvaro Alberto Cruz Jiménez - A01737453.\n\t\tAlejandro Kong Montoya - A0173427.\n\n\033[1mDISCLAIMER:\033[0m\n\t\033[1mEste juego se inspiró en el proyecto\033[0m \n\t\033[1m\"Battleships\". Last Hope es un\033[0m \n\t\033[1mproyecto que recrea las bases y\033[0m \n\t\033[1mreglas del mismo juego de mesa.\033[0m \n\n\tSe han adaptado las funciones \n\tdigitales a el ambiente en el cual \n\tse desarrolla el videojuego. \n\tEste proyecto es con fines educativos.\n\n\tEn 30 segundos la pantalla se cambiará...")
  time.sleep(30)

def programador_power():
    global proyectiles
    global mostrar
    global confirmacion
    global scene
    global lockscene
    lock = 1
    while lock == 1:
      def titulocambiante():
        os.system('clear')
        if opcion !=3:
          titulop()
        if opcion ==3:
          tituloo()
      def menuprogra():
        titulocambiante()
        print('\n¡Selecciona una opción! (No introduzca texto).')
        print('\n\t1. Modifica número de proyectiles.')
        if mostrar==False:
          print('\t2. Mostrar barcos.')
        if mostrar==True:
          print('\t2. Ocultar barcos.')
        if confirmacion==0:
          print('\t3. Quitar contraseña de los ajustes.')
        if confirmacion==1:
          print('\t3. Activar contraseña de los ajustes.')
        if lockscene==0:
          print("\t4. Desbloquear selección de escenas.")
        if lockscene==1:
          print("\t4. Bloquear selección de escenas.")
        print("\t5. Seleccionador de escena.")
        print('\t0. Seguir jugando.')
      menuprogra()
      opcion_mod = int(input('\nSelección: '))
      while opcion_mod < 0 or opcion_mod > 5:
        menuprogra()
        print("\nSelección:", opcion_mod, '\n\tOpción no válida.')
        opcion_mod = int(input('\nSelección: '))
      if opcion_mod != 0:
        if opcion_mod == 1:
          #Modificar número de proyectiles
          titulocambiante()
          if opcion !=3:
            proyectiles_show=proyectiles
            print(f"\nActualmente tienes {proyectiles_show} proyectil(es)\n")
            proyectiles = int(input("Ingrese el número de proyectiles deseados: "))
            while proyectiles<=0:
              titulocambiante()
              print(f"\nActualmente tienes {proyectiles_show} proyectil(es)\n")
              print("Ingrese el número de proyectiles deseados:", proyectiles, '\n\tOpción no válida.')
              proyectiles = int(input("\nIngrese el número de proyectiles deseados: "))
            os.system('clear')
          else:
            print("\nEsta opción solo está disponible dentro \ndel modo \"Arcade\" o \"Historia\".\n\n\tRegresando al menú de ajustes en 5 segundos.")
            time.sleep(5)
        elif opcion_mod == 2:
          #Mostrar barcos
          if mostrar == False:
            mostrar=True
            continue
          elif mostrar == True:
            mostrar=False
            continue
        if opcion_mod==3:
          #Quitar la contraseña de opciones
          if confirmacion==0:
            confirmacion=1
            continue
          if confirmacion==1:
            confirmacion=0
            continue
        if opcion_mod==4:
          #Desbloquear el seleccionador de niveles
          if lockscene==0:
            lockscene=1
            continue
          if lockscene==1:
            lockscene=0
            continue
        if opcion_mod==5:
          #Seleccionador de niveles
          if opcion==2:
            scene_show=scene
            titulocambiante()
            print(f"\nActualmente estás en la escena {scene_show+1}\n")
            scene = int(input("\nIngrese el número de escena a la \nque se desea ir [1 - 4]: "))
            scene-=1
            while scene<0 or scene>3:
              titulocambiante()
              print(f"\nActualmente estás en la escena {scene_show+1}\n")
              print("\nIngrese el número de escena a la \nque se desea ir [1 - 4]:", scene+1, '\n\tOpción no válida.')
              scene = int(input("\nIngrese el número de escena a la \nque se desea ir [1 - 4]: "))
              scene-=1
            print(f"\n\nLa próxima escena será la {scene+1}. \nPuedes continuar jugando.\n\n\tRegresando al menú de ajustes en 5 segundos.")
            time.sleep(5)
          else:
            titulocambiante()
            print("\nEsta opción solo está disponible dentro \ndel modo \"Historia\".\n\n\tRegresando al menú de ajustes en 5 segundos...")
            time.sleep(5)
      if opcion_mod == 0:
        lock += 1
        

def juego():
#Revisar: Esta función nos indicará si no se ha colocado una nave en la posición indicada, de esta forma evitando que las naves colisionen entre sí.
  global game_over
  global puntos
  global num_naves
  puntos = 0
  game_over=False
  def revisar(fil_in, fil_fin, col_in, col_fin):
    global tablero
    global posiciones

    todo_valido = True
    for i in range(fil_in, fil_fin):
      for j in range(col_in, col_fin):
        if tablero[i][j] != "*":
          todo_valido = False
          break
    if todo_valido:
      posiciones.append([fil_in, fil_fin, col_in, col_fin])
      for i in range(fil_in, fil_fin):
        for j in range(col_in, col_fin):
          tablero[i][j] = "O"
    return todo_valido

#Poner una nave: Esta función nos permite analizar el tamaño de una nave, así viendo cuál será su dirección y posición dentro del tablero.
  def int_poner_nave_tablero(fila, col, direccion, tamaño):
    global tam_tablero

    fil_in, fil_fin, col_in, col_fin = fila, fila + 1, col, col + 1
    if direccion == "izquierda":
      if col - tamaño < 0:
        return False
      col_in = col - tamaño + 1

    elif direccion == "derecha":
      if col + tamaño >= tam_tablero:
        return False
      col_fin = col + tamaño

    elif direccion == "arriba":
      if fila - tamaño < 0:
        return False
      fil_in = fila - tamaño + 1

    elif direccion == "abajo":
      if fila + tamaño >= tam_tablero:
        return False
      fil_fin = fila + tamaño

    return revisar(fil_in, fil_fin, col_in, col_fin)

#Tablero: Crea el tablero donde se va a jugar. De igual manera, genera las naves las cuales se van a destruir. Se van a ir checando cuantas naves se llevan colocadas para saber la relación entre el tablero y las naves.
  def crear_tablero():
    global tablero
    global tam_tablero
    global num_naves
    global posiciones

    filas, cols = (tam_tablero, tam_tablero)

    tablero = []
    for f in range(filas):
      fila = []
      for c in range(cols):
        fila.append("*")
      tablero.append(fila)

    naves_colocadas = 0

    posiciones = []

    while naves_colocadas != num_naves:
      random_fila = random.randint(0, filas - 1)
      random_col = random.randint(0, cols - 1)
      direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
      tamaño_nave = random.randint(3, 5)
      if int_poner_nave_tablero(random_fila, random_col, direccion,tamaño_nave):
        naves_colocadas += 1

#Imprimir Tablero: Con la matriz ya creada, se va a imprimir la misma con las filas A-J y 0-9, cambiando los O por 0 o por *
  def imprimir_tablero():
    """Imprimira el tablero con filas A-J y Columnas 0-9"""
    global tablero
    global alfabeto
    global mostrar

    alfabeto = alfabeto[0:len(tablero) + 1]

    for fila in range(len(tablero)):
      print(alfabeto[fila], end=") ")
      for col in range(len(tablero[fila])):
        if tablero[fila][col] == "O":
          if mostrar:
            print("0", end=" ")
          else:
            print("*", end=" ")
        else:
          print(tablero[fila][col], end=" ")
      print("")

    print("  ", end=" ")
    for i in range(len(tablero[0])):
      print(str(i), end=" ")
    print("")

#Menú Estadístico: Imprime todos los valores necesarios para tu juego.
  def menua():
    imprimir_tablero()
    print("\n\t◦ - - - - - - Estadísticas - - - - - - ◦\n")
    print("\tNúmero de naves enemigas restantes: " + str(num_naves - puntos))
    print("\tNúmero de proyectiles restantes: " + str(proyectiles))

#Comrpobante de proyectil: Esta función nos ayudará a ver si la posición la cual estamos definiendo cuando tiramos un proyectil tiene una parte de nave o no. 
  def comprobacion_de_posicion_de_proyectil():
    global alfabeto
    global tablero

    es_lugar_valido = False
    fila = -1
    col = -1

    while es_lugar_valido is False:
      lugar = input("\n\tIntroducir fila (A-J) y columna (0-9) \n\tEJEMPLO(A3): ")
      lugar = lugar.upper()
      if lugar == "AAJRR":
        programador_power()
        os.system('clear')
        titulo()
        menua()
        continue
      if len(lugar) <= 1 or len(lugar) > 2:
        os.system('clear')
        titulo()
        menua()
        print("\n\tError: Favor de introducir solo una \n\tfila y una columna.")
        continue
      fila = lugar[0]
      col = lugar[1]
      if not fila.isalpha() or not col.isnumeric():
        os.system('clear')
        titulo()
        menua()
        print("\n\tError: Favor de introducir letras (A-J) \n\tpara fila y números (0-9) para columnas.")
        continue
      fila = alfabeto.find(fila)
      if not (-1 < fila < tam_tablero):
        os.system('clear')
        titulo()
        menua()
        print(
          "\n\tError: Favor de introducir letras (A-J) \n\tpara fila y números (0-9) para columnas."
        )
        continue
      col = int(col)
      if not (-1 < col < tam_tablero):
        os.system('clear')
        titulo()
        menua()
        print(
          "\n\tError: Favor de introducir letras (A-J) \n\tpara fila y números (0-9) para columnas."
        )
        continue
      if tablero[fila][col] == " " or tablero[fila][col] == "X":
        os.system('clear')
        titulo()
        menua()
        print(
          "\n\t¡Ya has disparado un proyectil en ese sistema! \n\tNo malgastes tu munición. >:I"
        )
        continue
      if tablero[fila][col] == "*" or tablero[fila][col] == "O":
        es_lugar_valido = True
    os.system('clear')
    return fila, col

#Verificar Nave Destruida: Nos ayuda a cambiar la estadística de las naves destruidas.
  def verificar_destruccion_nave(fila, col):
    global posiciones
    global tablero

    for position in posiciones:
      fil_in = position[0]
      fil_fin = position[1]
      col_in = position[2]
      col_fin = position[3]
      if fil_in <= fila <= fil_fin and col_in <= col <= col_fin:
        for f in range(fil_in, fil_fin):
          for c in range(col_in, col_fin):
            if tablero[f][c] != "X":
              return False
    return True

#Texto por proyectil: Define el texto que se presentará en base a si se tiró una parte de una nave o no.
  def proyectil_disparado():
    global tablero
    global puntos
    global proyectiles

    fila, col = comprobacion_de_posicion_de_proyectil()

    if tablero[fila][col] == "*":
      titulo()
      print("Has fallado y no le has dado a ninguna nave...\n")
      tablero[fila][col] = " "
    elif tablero[fila][col] == "O":
      titulo()
      print("¡¡Le diste!!", end=" ")
      tablero[fila][col] = "X"
      if verificar_destruccion_nave(fila, col):
        print("Has destruido una nave.\n")
        puntos += 1
      else:
        print("Has dañado a una nave.\n")

    proyectiles -= 1

#Revisar Game Over: Esta función determinará qué texto aparecerá al perder, o ganar el juego.
  def revisar_game_over():
    """Si todas las naves han sido destruidas o nos quedamos sin proyectiles el juego habrá acabado"""
    global puntos
    global num_naves
    global proyectiles
    global game_over

    if num_naves == puntos:
      imprimir_tablero()
      print(
        "\n¡Felicidades has vencido!\n\n\tTeletransportandose en 10 segundos..."
      )
      game_over = True
      time.sleep(10)
      os.system('clear')
      if opcion == 1:
        titulomain()
        creditos()
    elif proyectiles <= 0:
      global mostrar
      mostrar_ant = mostrar
      mostrar = True
      imprimir_tablero()
      mostrar = mostrar_ant
      print(
        "\nHas perdido debido a que te quedaste \nsin proyectiles.\nLa humanidad ha sido condenada 💀\n\n\tTeletransportando al menú en 10 segundos..."
      )
      game_over = True
      time.sleep(10)
      os.system('clear')
      titulomain()
      creditos()

#Main: Función principal del juego que lo tendrá en loop hasta que se pierda.
  def main():
    global game_over
    titulo()
    print(
      f"¡¡Tienes {proyectiles} proyectiles para acabar con {num_naves} naves, que empiece la batalla espacial!!\n"
    )

    crear_tablero()

    while game_over is False:
      menua()
      proyectil_disparado()
      revisar_game_over()

  if __name__ == '__main__':

    main()


def historia():
  global scene
  global timer
  global num_naves
  global proyectiles
  global lockscene
  if scene == 0:
  # Variable global para número de naves
    num_naves = 6
  # Variable global para proyectiles disponibles
    proyectiles = 50
    line = line1
  elif scene == 1:
  # Variable global para número de naves
    num_naves = 4
  # Variable global para proyectiles disponibles
    proyectiles = 40
    line = line2
  elif scene == 2:
  # Variable global para número de naves
    num_naves = 2
  # Variable global para proyectiles disponibles
    proyectiles = 25
    line = line3
  elif scene == 3:
    line = line4

  os.system('clear')
  titulo()
  for i in line:
    print(i, end = '')
    sys.stdout.flush()
    if i =="¿":
      timer=0.2
      scene=-1
    time.sleep(timer)

  if scene == -1:
    if lockscene==0:
      print("\n\n¡Opción para elegir escena desbloqueada!")
      lockscene=1
    print("\n\n\t¡Historia terminada! \n\n\tRegresando al menú en 10 segundos...")
    time.sleep(10)
    os.system('clear')
    titulomain()
    creditos()
    
  if scene !=-1:
    print("\n\n\tLa batalla iniciará en 10 segundos...")
    time.sleep(10)
    os.system('clear')
    scene+=1
    juego()
  
while True:
  def menu():
    os.system('clear')
    titulom()
    print('\n\t1. Modo Arcade.')
    print('\t2. Modo Historia (BETA).')
    print('\t3. Opciones.')
    print('\t4. Créditos.')
    print('\t0. Salir.')
  scene=0
  menu()
  opcion=int(input('\n\nSelección: '))
  
  while opcion<0 or opcion>4: 
    menu()
    print("\n\nSelección: ", opcion, '\n\tOpción no válida.')
    opcion=int(input('\n\tSelección: '))
    
  if opcion == 1:
    #ESPACIO ARCADE
    #ESPACIO PARA ARCADE 1 JUGADOR
    #Menú de dificultad(MODO ARCADE): Este menú a base de "Whiles" va a determinar cuántas naves se deben de destruir, además de cuántos proyectiles se cuentan para hacer esto.
  #NIVEL FÁCIL: 6 naves con 50 proyectiles.
  #NIVEL INTERMEDIO: 4 naves con 40 proyectiles.
  #NIVEL DIFÍCIL: 2 naves con 25 proyectiles.
    def menudif():
      os.system('clear')
      tituloa()
      print('\n¡Selecciona una dificultad!')
      print('\n\t1. Fácil.')
      print('\t2. Normal.')
      print('\t3. Difícil.')
      print('\t0. Salir al menú.')
    menudif()
    opcion_uno = int(input('\n\nSelección: '))
    while opcion_uno < 0 or opcion_uno > 3:
      menudif()
      print("\n\nSelección: ", opcion_uno, '\n\tOpción no válida.')
      opcion_uno = int(input('\n\nSelección: '))
    if opcion_uno != 0:
      if opcion_uno == 1:
        #NIVEL FÁCIL
        # Variable global para número de naves
        num_naves = 6
        # Variable global para proyectiles disponibles
        proyectiles = 50
        os.system('clear')
      elif opcion_uno == 2:
        #NIVEL INTERMEDIO
        # Variable global para número de naves
        num_naves = 4
        # Variable global para proyectiles disponibles
        proyectiles = 40
        os.system('clear')
      elif opcion_uno == 3:
        #NIVEL DIFÍCIL
        # Variable global para número de naves
        num_naves = 2
        # Variable global para proyectiles disponibles
        proyectiles = 25
        os.system('clear')
      juego()
    
  if opcion == 2:
    def menuhistoria():
      os.system('clear')
      tituloh()
      print('\n\t1. Iniciar Historia.')
      print('\t2. Seleccionar Nivel.')
      print('\t0. Regresar al menú.')
    menuhistoria()
    opcion_his=int(input('\n\nSelección: '))
    
    while opcion_his<0 or opcion_his>2: 
      menuhistoria()
      print("\n\nSelección: ", opcion_arc, '\n\tOpción no válida.')
      opcion_his=int(input('\n\tSelección: '))
      
    if opcion_his == 1:
      #INICIO LINEAL DE HISTORIA
      while scene !=-1:
        historia()
    if opcion_his == 2:
      #MENU DE SELECCIÓN DE ESCENAS
      os.system("clear")
      if lockscene != 1:
        tituloh()
        print("\n\t\033[1m¡Esta opción está bloqueada!\033[0m\n\nTermina el modo historia de manera lineal\npara acceder a esta opción.\n\n\tRegresando al menú en 15 segundos...")
        time.sleep(15)
        continue
      def menuhistoriaselec():
        os.system("clear")
        tituloh()
        print('\n¡Selecciona un nivel!')
        print('\n\t\033[1m1. Lvl 1.\033[0m')
        print('\t\033[1m2. Lvl 2.\033[0m')
        print('\t\033[1m3. Lvl 3.\033[0m')
        print('\t0. Salir al menú.')
      menuhistoriaselec()
      opcionhselect = int(input('\nSelección: '))
      while opcionhselect < 0 or opcionhselect > 3:
        menuhistoriaselec()
        print("\nSelección:", opcionhselect, '\n\tOpción no válida.')
        opcionhselect = int(input('\n\nSelección: '))
      scene = opcionhselect - 1
      while scene !=-1:
        historia()

  if opcion == 3:
    os.system('clear')
    titulo()
    if intentos != 5:
      if confirmacion !=1:
        print("\nIngresa la contraseña")
        password="AAJRR"
        passw=input("\n\tContraseña: ")
        passw=passw.upper()
      if confirmacion==1:
        passw=password
      if password==passw:
        intentos=0
        programador_power()
      else:
        print(f"\nContraseña incorrecta... {(intentos-4)*-1} intento(s) disponibles.")
        intentos+=1
        time.sleep(3)
    if intentos == 5:
      print("\nNúmero máximo de intentos alcanzado...\n\n\tRegresando al menú en 5 segundos...")
      time.sleep(5)

  if opcion == 4:
    os.system('clear')
    creditos()
  
  if opcion == 0:
    os.system('clear')
    titulomain()
    break;