#there are three type of class methods:
#static method
#instance method
#class method

class Student:

    school_name = 'ABC School'            #class variable

    # constructor
    def __init__(self, name, age):
                                              
        self.name = name                   # instance variables
        self.age = age

                
    def show(self):                        # instance variables
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']
        

        # create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_School('XYZ School')
# call class method using the object
jessa.change_School('PQR School')

# call static method using the class
Student.find_notes('Math')
# call class method using the object
jessa.find_notes('Math')