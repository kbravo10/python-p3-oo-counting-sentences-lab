#!/usr/bin/env python3

class MyString:

  def __init__(self, string = None):
    if string != None:
      if type(string) == str:
        self.value = string
    else:
      self.value = ""


  def is_sentence(self):
    if self.value.endswith("."):
      return True
    return False
  
  def is_question(self):
    if self.value.endswith("?"):
      return True
    return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    return False

  def count_sentences(self):
    if(len(self.value) != 0):
      new_sentense = self.value
      if(new_sentense.__contains__('?')):
        new_sentense = new_sentense.replace('?', '.')
      if(new_sentense.__contains__('!')):
        new_sentense = new_sentense.replace('!','.')
      return len(new_sentense.split(". "))
    
    return 0
  
  def set_string(self, string):
    if(type(string) == str):
      self._string = string
    else:
      print("The value must be a string.")
  
  def get_string(self):
    return self._string

  value = property(get_string, set_string)