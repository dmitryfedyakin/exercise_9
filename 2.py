class NotSleeping:
  '''
  Class of sheep in person's dream.

  Attriubtes:
    name (str): person's name
    sheeep_amount (int): amount of sheep
  '''

  def __init__(self, name):
    '''
    Initializing initial amount of sheep.

    :param name: person's name
    '''
    self.name = name
    self.sheep_amount = 0

  def add_sheep(self):
    '''
    Increases amount of sheep.
    '''
    self.sheep_amount += 1

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return f'Имя: {self.name}, количество: {self.sheep_amount}'

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


help(NotSleeping)
