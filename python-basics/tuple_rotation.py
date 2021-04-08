'''
В этом испытании вы будете работать с "тройками" — кортежами из трёх элементов. Вам предстоит реализовать две функции, которые "вращают" тройку влево и вправо. Как это выглядит, вы можете понять из пары примеров:
# >>> triple = ('A', 'B', 'C')
# >>> rotate_left(triple)
# ('B', 'C', 'A')
# >>> rotate_right(triple)
# ('C', 'A', 'B')
'''

triple = ('A', 'B', 'C')

def rotate_left(values):
  result = (values[1], values[2], values[0])
  return result

def rotate_right(values):
  result = (values[2], values[0], values[1])
  return result
