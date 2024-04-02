class Dog:
  '''
  Class of dog.

  Attributes:
    name (str): name of dog
  '''

  def __init__(self, name):
    '''
    Initializing dog parametres.

    :param name: name of dog
    '''
    self.name = name

  def say(self):
    '''
    Print dog's sound.
    '''
    print("Гав!")

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return f'Пёс {self.name}'

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


help(Dog)
