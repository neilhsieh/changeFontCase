print('Case Converter:')
input_word = raw_input("Please enter word: ")

def spongebob_case(input_word):
  new_word = ""
  is_uppercase = False
  for i in range(len(input_word)):
    if not(input_word[i] == " "):
      if is_uppercase:
        new_word += input_word[i].upper()
      else:
        new_word += input_word[i]
      is_uppercase = not(is_uppercase)
    else:
      new_word += ' '


  print('\x1b[0;30;43m' + new_word + '\x1b[0m')

spongebob_case(input_word)