def filter_list(l):
  y = [i for i in l if type(i)==int and i>=0]
  return y