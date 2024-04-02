class TrafficLight:
  '''
  Class of traffic light.

  Attributes:
    permissible_values (list): A list of permissible signal values
    current_signal (str): color of current signal
    previous_signal (str): color of previous signal
  '''

  permissible_values = ['green', 'yellow', 'red']

  def __init__(self):
    '''
    Initializing current and previous signals.
    '''
    self.current_signal = TrafficLight.permissible_values[0]
    self.previous_signal = TrafficLight.permissible_values[1]

  def next_signal(self):
    '''
    Get the next signal.
    '''
    green = TrafficLight.permissible_values[0]
    yellow = TrafficLight.permissible_values[1]
    red = TrafficLight.permissible_values[2]

    if self.current_signal == green:
      self.previous_signal = green
      self.current_signal = yellow
    elif self.current_signal == yellow:
      if self.previous_signal == green:
        self.previous_signal = yellow
        self.current_signal = red
      else:
        self.previous_signal = yellow
        self.current_signal = green
    elif self.current_signal == red:
      self.previous_signal = red
      self.current_signal = yellow

  def __str__(self):
    '''
    Return string representation of an object (for users).
    '''
    return f'Current signal: {self.current_signal}'

  def __repr__(self):
    '''
    Return formal string representation of an object (for developers).
    '''
    return self.__str__()


traffic_light = TrafficLight()
print(traffic_light)

for _ in range(10):
  traffic_light.next_signal()
  print(traffic_light)
