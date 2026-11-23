# class Soda:
#   # Конструктор (собирает объекты)
#   def __init__(self, additive):
#     self.additive = additive
  
#   # Метод отображения напитков
#   # self указ. к какому объекту относится метод
#   def show_my_drink(self):
#     if (self.additive is not None):
#       print(f"Газировка и {self.additive}")
#     else:
#       print("Обычная газировка")
  

# # Создание объектов на осн. класса
# lemonade = Soda('лимон')
# mint = Soda('мята')
# lemonade.show_my_drink()
# mint.show_my_drink()


# class TriangleChecker():
#   def __init__(self, l1, l2, l3):
#     self.l1 = l1
#     self.l2 = l2
#     self.l3 = l3
  
#   def is_triangle(self):
#     lines = [self.l1, self.l2, self.l3]
#     print(f"Отрезки: {lines}")
#     linesSorted = sorted(lines)
#     if (linesSorted[0] + linesSorted[1] > linesSorted[2]):
#       print("Треугольник можно построить")
#     else:
#       print("Треугольник невозможен")
  
  
  
# triangle1 = TriangleChecker(1, 23, 5)
# triangle1.is_triangle()

# triangle2 = TriangleChecker(2, 6, 5)
# triangle2.is_triangle()



# class BankAccount():
#   account_number = None
#   balance = None

#   def __init__(self, account_number=1, balance=0):
#     self.account_number = account_number
#     self.balance = balance

#   def add(self, account_number, balance):
#     account_number = self.account_number
#     balance = self.balance
#     print(f"Номер вашего счёта: {account_number}\n Ваш счёт: ")
# acc1 = add(2, 250)

students = {}
i = 1

class Student():
    def __init__(self, full_name, group_number, progress=None):
      # self - т.е переменная присвается к самому объекту при его создании
      self.full_name = full_name
      self.group_number = group_number
      self.progress = progress
      
    def __str__(self):
        return f"{self.full_name}  {self.group_number}  {self.progress}"
    

while True:
  print(f"\nСтудент №{i}")
  full_name = input("Имя: ")
  group_number = int(input("Номер группы: "))
  raw_progress = input("Список оценок (через запятую): ")
  progress = []
  # берем делителем запятую
  for x in raw_progress.split(","): 
  # убираем пробелы
    clean_x = x.strip()
    if clean_x:  # если после удаления пробелов что-то осталось - добавляем отдельными элементами
        progress.append(int(clean_x))


  student = Student(full_name, group_number, progress)
  students[i] = student
  i += 1
 
  # Если передать в sorted() studentsw, python выкинет все значения и отсортирует только ключи. 
  # Метод .items() вытаскивает из словаря данные в виде списка пар: [('1', Максим, 3419/2, 2, 2, 2), ('Кирилл', 1, 2, 3)]
  # item[1].full_name.lower() - указание для сортировки по значению full_name
  sorted_students = dict(sorted(students.items(), key=lambda item: item[1].full_name.lower()))
  print(f"\nСписок студентов:\n")
  print(f"№ |Ф.И.О|Группа|Оценки")
  for num, student in sorted_students.items():
      print(f"{num}. {student}")
  


    