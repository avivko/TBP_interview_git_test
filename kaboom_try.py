def KaBoom(n: int):
  """
  My bad implementation
  """
  five_multis = [i*5 for i in range(1,n+1)]
  seven_multis = [i*7 for i in range(1,n+1)]
  for i in range(n):
    if i in five_multis or i in seven_multis:
      print('KaBoom')
    elif i in five_multis:
      print('Ka')
    elif i in seven_multis:
      print('Boom')
    else:
      print(bin(i))
