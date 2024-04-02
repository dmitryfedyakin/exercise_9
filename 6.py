class Point:
  '''
  Class of point.

  Attributes:
    coords (tuple): coordinates of the point
    x (int): x coordinate of the point
    y (int): y coordinate of the point
  '''

  def __init__(self, coords=(0, 0)):
    '''
    Initializing the point with the coordinates.

    :param coords: coordinates of the point
    '''
    self.x, self.y = coords

  def get_x(self):
    '''
    Get the x coordinate of the point.

    :return: x coordinate of the point
    '''
    return self.x

  def get_y(self):
    '''
    Get the y coordinate of the point.

    :return: y coordinate of the point
    '''
    return self.y

  def distance(self, other):
    '''
    Get the distance between the point and another point.

    :param other: another point

    :return: distance between the point and another point
    '''
    return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

  def summ(self, other):
    '''
    Get the sum of the coordinates of the point and another point.

    :param other: another point

    :return: sum of the coordinates of the point and another point
    '''
    return Point((self.x + other.x, self.y + other.y))

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return f'({self.x}, {self.y})'

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


first_point = Point((2, 1))
second_point = Point((4, 5))
print(f'{first_point.get_x()}, {first_point.get_y()}')
print(f'{second_point.get_x()}, {second_point.get_y()}')
print(first_point.distance(second_point))
print(first_point.summ(second_point))
