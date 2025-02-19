class Contact:
   
   def __init__(self,number,address):
       self.number=number
       self.address=address
  

class Person:
    def __init__(self,name,identifier,email, contact):
        self.name=name
        self.identifier=identifier
        self.email=email
        self.contact_detail = contact


class Employee(Person):

    def __init__(self,name,identifier,email,contact_detail,designation,salary):
        super().__init__(name,identifier,email,contact_detail)
        self.designation=designation
        self.salary=salary
    def display(self):
        print(f"Name:{self.name} Id:{self.identifier} Email:{self.email} Designation:{self.designation} contact:{self.contact_detail.number} Address:{self.contact_detail.address}")
     


    
c1 = Contact(123, 'abc')
p1 = Person('abc', 123, 'email', c1)
e1=Employee(p1.name,p1.identifier,p1.email,c1,'jnr',10000)   