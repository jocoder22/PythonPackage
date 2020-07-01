def print2(*args):
  for arg in args:
    print(arg, end="\n\n")
    
def describe2(data):
  print2(data.shape, data.info(), data.head(),
         data.tail(), data.describe())
