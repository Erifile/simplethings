import os

# СТРУКТУРЫ ДАННЫХ
LETTER_TO_IDX = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
IDX_TO_LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
SHIPS_LIST = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # Стандартный набор кораблей

p1_ships_field = [['.' for _ in range(10)] for _ in range(10)]
p2_ships_field = [['.' for _ in range(10)] for _ in range(10)]
p1_radar_field = [['.' for _ in range(10)] for _ in range(10)]
p2_radar_field = [['.' for _ in range(10)] for _ in range(10)]


# Функции

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_fields(ships_field, radar_field, player_name):
    clear_screen()
    print(f"=== ХОД ИГРОКА: {player_name} ===")
    print("      ТВОИ КОРАБЛИ                      ТВОЙ РАДАР")
    print("   | a b c d e f g h i j |          | a b c d e f g h i j |")
    print("--------------------------          --------------------------")
    for i in range(10):
        row_num = i + 1
        ships_row = " ".join(ships_field[i])
        radar_row = " ".join(radar_field[i])
        print(f"{row_num:<2} | {ships_row} |       {row_num:<2} | {radar_row} |")
    print()

def get_coordinate(prompt="Введи координату (например, a1 или j10): "):
    while True:
        # .strip() убирает случайные пробелы по бокам, .lower() делает буквы маленькими
        coord = input(prompt).strip().lower()
        
        if len(coord) < 2:
            print("Ошибка! Неверный формат. Нужно: буква и число (например, a1).\n")
            continue
        
        letter = coord[0]     # Первая буква
        num_str = coord[1:]    # Всё остальное — это число
        
        # Проверяем, что буква корректна, а в числовой части только цифры
        if letter not in LETTER_TO_IDX or not num_str.isdigit():
            print("Ошибка! Буква должна быть от a до j, а строка — числом от 1 до 10.\n")
            continue
            
        row = int(num_str) - 1
        col = LETTER_TO_IDX[letter]
        
        # Проверяем, попадает ли число в сетку 1-10 (в индексах 0-9)
        if not (0 <= row <= 9):
            print("Ошибка! Строка должна быть от 1 до 10.\n")
            continue
            
        return row, col


def is_zone_clear(field, row, col):
    """
    Проверяет саму клетку и все 8 клеток вокруг неё (включая диагонали).
    Если где-то рядом уже стоит чужой корабль ('X'), возвращает False.
    """
    # Перебираем сдвиги от -1 до 1 по строкам (dr) и колонкам (dc)
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            neighbor_row = row + dr
            neighbor_col = col + dc
            
            # Проверяем, что соседняя клетка не выходит за границы поля 10х10
            if 0 <= neighbor_row < 10 and 0 <= neighbor_col < 10:
                # Если в этой клетке уже есть корабль, значит ставить сюда нельзя
                if field[neighbor_row][neighbor_col] == 'X':
                    return False
    return True


# РАССТАНОВКА КОРАБЛЕЙ

def place_ships(ships_field, player_name):
    counts = {4: SHIPS_LIST.count(4), 3: SHIPS_LIST.count(3), 
              2: SHIPS_LIST.count(2), 1: SHIPS_LIST.count(1)}
    
    empty_radar = [['.' for _ in range(10)] for _ in range(10)]
    
    while sum(counts.values()) > 0:
        print_fields(ships_field, empty_radar, player_name)
        print(f"Осталось расставить: 4х({counts[4]}) 3х({counts[3]}) 2х({counts[2]}) 1х({counts[1]})")
        
        while True:
            try:
                size = int(input("Выбери размер корабля (1-4): "))
                if size in counts and counts[size] > 0:
                    break
                print("Таких кораблей не осталось или размер неверный!\n")
            except ValueError:
                print("Введите число.\n")
        
        while True:
            print(f"\nСтавим корабль {size}х. Укажи НАЧАЛЬНУЮ точку.")
            row, col = get_coordinate()
            
            # Для однопалубника направление не нужно, но ауру вокруг проверить надо
            if size == 1:
                if not is_zone_clear(ships_field, row, col):
                    print("Ошибка! Корабли не могут соприкасаться. Выберите другое место.\n")
                    continue
                ships_field[row][col] = 'X'
                break
            else:
                direction = input("Направление (v — вниз, h — вправо): ").strip().lower()
                if direction not in ['v', 'h']:
                    print("Неверное направление!\n")
                    continue
                
                can_place = True
                cells = []
                
                # Собираем все клетки, которые займет корабль
                for i in range(size):
                    r = row + i if direction == 'v' else row
                    c = col if direction == 'v' else col + i
                    
                    # Проверяем границы поля
                    if not (0 <= r < 10 and 0 <= c < 10):
                        print("Ошибка! Корабль выходит за границы поля.\n")
                        can_place = False
                        break
                        
                    # Проверяем саму клетку и её окружение через нашу новую функцию
                    if not is_zone_clear(ships_field, r, c):
                        print(f"Ошибка! Клетка {IDX_TO_LETTER[c]}{r+1} или её окружение заняты.\n")
                        can_place = False
                        break
                        
                    cells.append((r, c))
                
                if can_place:
                    for r, c in cells:
                        ships_field[r][c] = 'X'
                    break
                    
        counts[size] -= 1
    
    print_fields(ships_field, empty_radar, player_name)
    input("Корабли расставлены! Передай управление следующему игроку и нажми Enter...")


# СТРЕЛЬБА

def check_victory(field):
    for row in field:
        if 'X' in row:
            return False
    return True

def make_shot(enemy_ships, my_radar):
    while True:
        row, col = get_coordinate("Куда стреляем? Введи координату: ")
        
        if my_radar[row][col] != '.':
            print("Ты уже стрелял в эту клетку! Выбери другую.\n")
            continue
            
        if enemy_ships[row][col] == 'X':
            print("ПОПАДАНИЕ!")
            enemy_ships[row][col] = '📍'
            my_radar[row][col] = '💥'
            return True
        else:
            print("МИМО!")
            my_radar[row][col] = '•'
            return False


# --- ГЛАВНАЯ ФУНКЦИЯ ИГРЫ ---

def main():
    print("=== МОРСКОЙ БОЙ ===")
    input("Игрок 1, приготовься расставлять корабли. Нажми Enter...")
    place_ships(p1_ships_field, "ИГРОК 1")
    
    clear_screen()
    input("Игрок 2, приготовься расставлять корабли. Нажми Enter...")
    place_ships(p2_ships_field, "ИГРОК 2")
    
    current_player = 1
    
    while True:
        if current_player == 1:
            print_fields(p1_ships_field, p1_radar_field, "ИГРОК 1")
            hit = make_shot(p2_ships_field, p1_radar_field)
            
            if check_victory(p2_ships_field):
                print_fields(p1_ships_field, p1_radar_field, "ИГРОК 1")
                print("🎉 🎉 🎉 ИГРОК 1 ПОБЕДИЛ! Все корабли врага потоплены! 🎉 🎉 🎉")
                break
                
            if not hit:
                input("\nНажми Enter, чтобы передать ход Игроку 2...")
                current_player = 2
        else:
            print_fields(p2_ships_field, p2_radar_field, "ИГРОК 2")
            hit = make_shot(p1_ships_field, p2_radar_field)
            
            if check_victory(p1_ships_field):
                print_fields(p2_ships_field, p2_radar_field, "ИГРОК 2")
                print("🎉 🎉 🎉 ИГРОК 2 ПОБЕДИЛ! Все корабли врага потоплены! 🎉 🎉 🎉")
                break
                
            if not hit:
                input("\nНажми Enter, чтобы передать ход Игроку 1...")
                current_player = 1

if __name__ == "__main__":
    main()
