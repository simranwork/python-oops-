
#creating a class
from unicodedata import name


class person:
    def __init__(self,name,sex,profession):     #contructor
    #data members (instance/object variables)
     self.name = name
     self.sex = sex
     self.profession = profession

    # behaviour instance method
    def show(self):                               # func1 
        print(f'Name: {self.name}\n sex: {self.sex}\n professon: {self.profession}')

    #behavior instance method                      # func 2 
    def work(self):
        print(f'I am {self.name} working as a {self.profession}')

#create object
Jessa = person('Jessa',"Female",'Software developer')


#calling methods
Jessa.show()
Jessa.work()


    