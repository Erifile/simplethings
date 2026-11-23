class UserMail():
  def __init__(self, login, email):
    self.__login = login
    self.__email = email

  @property
  def login(self):
    return self.__login
  
  @login.setter
  def login(self, login):
    self.__login = login
  
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, newEmail):
    # Вызываем геттер через self.email, чтобы получить старую почту
    if self.email == newEmail:
      print("Ошибка. Новая почта совпадает со старой.")
      return
    if "@" not in newEmail:
      print("Ошибка. Обязателен знак @")
      return
    self.__email = newEmail




class User():
  def __init__(self, login, password, phrase):
    self.__login = login
    self.password = password
    self.__phrase = phrase
  
  @property
  def login(self):
    return self.__login
  
  @login.setter
  def login(self, login):
    self.__login = login
  
  @property
  def password(self):
    return self.__password
  
  @login.setter
  def password(self, password):
    self.__password = password
    # . . . .

