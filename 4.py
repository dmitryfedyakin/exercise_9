class User:
  '''
  Class of users.

  Attributes:
    id (str): id of user
    nick_name (str): nickname of user
    first_name (str): first name of user
    last_name (str): last name of user
    middle_name (str): middle name of user
    gender (str): gender of user
  '''

  def __init__(self,
               id,
               nick_name,
               first_name,
               last_name=None,
               middle_name=None,
               gender=None):
    '''
    Initializing user parametres.

    :param id: id of user
    :param nick_name: nickname of user
    :param first_name: first name of user
    :param last_name: last name of user
    :param middle_name: middle name of user
    :param gender: gender of user
    '''
    self.id = id
    self.nick_name = nick_name
    self.first_name = first_name
    self.last_name = last_name
    self.middle_name = middle_name
    self.gender = gender

  def update(self):
    '''
    Upadting information about user.
    '''
    number = input('Edit:\n1.first name\n2.last name\n3.middle name\n')
    if number == '1':
      self.first_name = input("Enter new first_name: ")
    elif number == '2':
      self.last_name = input("Enter new last_name: ")
    elif number == '3':
      self.middle_name = input("Enter new middle_name: ")

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return (f'{self.id}, {self.nick_name}, {self.gender}, '
            f'{self.first_name}, {self.last_name}, {self.middle_name}')

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


user = User('1', 'anonymous', 'Ivan', 'Ivanov', 'Alberto', 'male')
user.update()
print(user.__str__())
user.update()
print(user.__str__())
