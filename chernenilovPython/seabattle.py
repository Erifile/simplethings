

player1Ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
player1Cords = 
[
  a1, b1, c1, d1, e1, f1, g1, h1, i1, j1
  a2, b2, c2, d2, e2, f2, g2, h2, i2, j2
  a3, b3, c3, d3, e3, f3, g3, h3, i3, j3
  a4, b4, c4, d4, e4, f4, g4, h4, i4, j4
  a5, b5, c5, d5, e5, f5, g5, h5, i5, j5
  a6, b6, c6, d6, e6, f6, g6, h6, i6, j6
  a7, b7, c7, d7, e7, f7, g7, h7, i7, j7
  a8, b8, c8, d8, e8, f8, g8, h8, i8, j8
  a9, b9, c9, d9, e9, f9, g9, h9, i9, j9
  a0, b0, c0, d0, e0, f0, g0, h0, i0, j0

]


def prepareShips1():
  
    left1x = 4
    left2x = 3
    left3x = 2
    left4x = 1
  for ship in player1Ships:

    

    print(f"Этап расстановки кораблей\n(Игрок 1)\nОсталось расставить:\n1х ({left1x}) 2х ({left2x}) 3х ({left3x}) 4х ({left4x})")

    while True:
      try:
        selectedShip = int(input("Выбери корабль для расстановки\n(введи размер корабля): "))
        if selectedShip < 1 or selectedShip > 4:
          print("Ошибка. Число от 1 до 4\n")
        else:
          # перезапись перебираемого корабля из списка, чтобы впоследствии именно его удалить
          ship = selectedShip 
          break
      except ValueError:
        print("Ошибка. Введите число\n")

    print(f"\nВыбери место установки для {ship}x корабля\n")
    if selectedShip == 1:
      selectedCord = input("Введи незанятую координату поля")
      if ()
      # while True
      #   если выбр. корда занята:
      #     ошибка. введите незанятую
      #елсе:
          
      #   break
      # 

    print("   |a|b|c|d|e|f|g|h|i|j|")
    print(" 1 | | | | | | | | | | |")
    print(" 2 | | | | | | | | | | |")
    print(" 3 | | | | | | | | | | |")
    print(" 4 | | | | | | | | | | |")
    print(" 5 | | | | | | | | | | |")
    print(" 6 | | | | | | | | | | |")
    print(" 7 | | | | | | | | | | |")
    print(" 8 | | | | | | | | | | |")
    print(" 9 | | | | | | | | | | |")
    print(" 0 | | | | | | | | | | |")




print("Морской бой")
while True:
  startInput = input("Введите '1', чтобы начать: ")
  if startInput == '1':
    prepareShips1()
    break



 

