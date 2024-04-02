class Game:
  '''
  Class of basketball game

  Attributes:
    teams (dict): dictionary containing the names of the two teams playing the game
    score (dict): dictionary containing the score of each team
  '''

  def __init__(self, teams):
    '''
    Initializing the game with the info about two teams playing the game

    :param teams: dictionary containing the names of the two teams playing the game
    '''
    self.teams = teams
    self.score = {teams['command1']: 0, teams['command2']: 0}

  def ball_thrown(self, command, points):
    '''
    Update the score based on the team that scored.

    :param command: name of the team that scored
    :param points: points scored by the team
    '''
    self.score[command] += points

  def get_score(self):
    '''
    Get the current score of the game.

    :return: tuple containing the current score of the game
    '''
    return tuple(self.score.values())

  def get_winner(self):
    '''
    Get the winner of the game based on the scores.

    :return: name of the team that won the game or draw
    '''
    score_1, score_2 = self.score.values()
    if score_1 > score_2:
      return self.teams['command1']
    elif score_2 > score_1:
      return self.teams['command2']
    else:
      return 'Ничья'


teams = {'command1': 'Alpha', 'command2': 'Beta'}
game = Game(teams)

game.ball_thrown('Alpha', 2)
game.ball_thrown('Alpha', 2)
game.ball_thrown('Beta', 3)
print(game.get_score())
print(game.get_winner())
