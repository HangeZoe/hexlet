triple = ('A', 'B', 'C')

def rotate_left(values):
  result = (values[1], values[2], values[0])
  return result

def rotate_right(values):
  result = (values[2], values[0], values[1])
  return result
