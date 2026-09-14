def changecase(func):
  def myinner():
    return func().upper()
  return myinner

''' 
for upper case we used this function
'''


def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())