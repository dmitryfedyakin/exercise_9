class StandsDNA:
  '''
  Class of DNA stands

  Attributes:
    all_strands (list): A list containing DNA strands
  '''

  def __init__(self):
    '''
    Initializes the list of DNA strands.
    '''
    self.all_strands = ['ГАТЦ', 'АЦГ', 'ЦАЦАТГ', 'ТГА', 'ТТГ']

  def add_strands(self, strands):
    '''
    Add new DNA strands to the existing list.

    :param strands: string containing new DNA strands
    '''
    self.all_strands += strands.split()

  def get_max_strands(self):
    '''
    Get the DNA strands with the maximum length.

    :return: list of DNA strands with the maximum length
    '''
    list_1 = sorted(set(self.all_strands))
    return [i for i in list_1 if len(i) == len(max(list_1, key=len))]

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return f'All strands: {self.all_strands}'

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


stands = StandsDNA()
stands.add_strands('АГТ ЦАЦ ГАГАГА')
print(stands)
print(*stands.get_max_strands())
