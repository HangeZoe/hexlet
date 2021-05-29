# Реализуйте функцию is_palindrome(), которая принимает на вход слово, определяет является ли оно палиндромом и возвращает логическое значение.

def is_palindrome(string):
  reverse_string = string[::-1]
  if reverse_string == string:
    return True
  else:
    return False
