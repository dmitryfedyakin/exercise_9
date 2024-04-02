class Morsemsg:
  '''
  Class of decoding morse message

  Attributes:
    msg (str): morse message
    decode (str): decoded message
    eng_alph (str): english alphabet
    rus_alph (str): russian alphabet
    vowels_eng (str): vowels in english alphabet
    vowels_rus (str): vowels in russian alphabet
    consonants_eng (str): consonants in english alphabet
    consonants_rus (str): consonants in russian alphabet
  '''

  def __init__(self, msg):
    '''
    Initializing morse message and dictionaries

    :param msg: morse message
    '''
    self.msg = msg
    self.decode = ''
    self.eng_alph = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    self.rus_alph = {
        '.-': 'А',
        '-...': 'Б',
        '.--': 'В',
        '--.': 'Г',
        '-..': 'Д',
        '.': 'Е',
        '...-': 'Ж',
        '--..': 'З',
        '..': 'И',
        '.---': 'Й',
        '-.-': 'К',
        '.-..': 'Л',
        '--': 'М',
        '-.': 'Н',
        '---': 'О',
        '.--.': 'П',
        '.-.': 'Р',
        '...': 'С',
        '-': 'Т',
        '..-': 'У',
        '..-.': 'Ф',
        '....': 'Х',
        '-.-.': 'Ц',
        '---.': 'Ч',
        '----': 'Ш',
        '--.-': 'Щ',
        '--.--': 'Ъ',
        '-.--': 'Ы',
        '-..-': 'Ь',
        '..-..': 'Э',
        '..--': 'Ю',
        '.-.-': 'Я'
    }

    self.vowels_eng = ['A', 'E', 'I', 'O', 'U']
    self.vowels_rus = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Я', 'Ю', 'Ы', 'Э']
    self.consonants_eng = [
        'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
        'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
    ]
    self.consonants_rus = [
        'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С',
        'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ъ'
    ]

  def eng_decode(self):
    '''
    Decoding morse message in english

    :return: decoded message
    '''
    self.decode = ''
    for i in self.msg.split():
      if i in self.eng_alph:
        self.decode += self.eng_alph[i]

    return self.decode

  def rus_decode(self):
    '''
    Decoding morse message in russian

    :return: decoded message
    '''
    self.decode = ''
    for i in self.msg.split():
      if i in self.rus_alph:
        self.decode += self.rus_alph[i]

    return self.decode

  def get_vowels(self, lang):
    '''
    Get vowels from morse message

    :param lang: language of decoding

    :return: vowels
    '''
    vowels = []
    if lang == 'eng':
      for i in self.eng_decode():
        if i in self.vowels_eng:
          vowels.append(i)
    elif lang == 'rus':
      for i in self.rus_decode():
        if i in self.vowels_rus:
          vowels.append(i)

    return vowels

  def get_consonants(self, lang):
    '''
    Get consonants from morse message

    :param lang: language of decoding

    :return: consonants
    '''
    consonants = []
    if lang == 'eng':
      for i in self.eng_decode():
        if i in self.consonants_eng:
          consonants.append(i)
    elif lang == 'rus':
      for i in self.rus_decode():
        if i in self.consonants_rus:
          consonants.append(i)

    return consonants


msg = input()
lang = input()
morse = Morsemsg(msg)
print(morse.eng_decode())
print(morse.rus_decode())
print(morse.get_vowels(lang))
print(morse.get_consonants(lang))