# Реализуйте функцию is_palindrome(), которая принимает на вход слово, 
# определяет является ли оно палиндромом и возвращает логическое значение.


def is_palindrome(string):
  """Функция определяет, является ли введеное слово палиндромом
  и возвращает истину, если это так
  """
  reverse_string = string[::-1]
  if reverse_string == string:
    return True
  else:
    return False

  
# Another solution:
#
# def is_palindrome(string):
#     return str(string)[::-1] == str(string)
