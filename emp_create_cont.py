d={}
def dict(contact,person):
    for key in d:
        if(key==contact.number):
            print("Validation Err")
            return
        
    d.update({contact.number:person.name})
    print(d)
   

    
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
        print(f"\nName:{self.name}\nId:{self.identifier} \nEmail:{self.email}\nDesignation:{self.designation} \ncontact:{self.contact_detail.number} \nAddress:{self.contact_detail.address}")
     
def get_details(contact,employee):
    for key ,values in d.items():
        if(key==contact):
            name=values
   
    for emp in employee:
         if(emp.name==name):
            emp.display()

        
def get_number(id,employee):
    
    for emp in employee:
        
        if(emp.identifier==id):
            print(emp.contact_detail.number)


            
        


    
c1 = Contact(1111111111, 'abc')
p1 = Person('p1', 100, 'p1.email', c1)
e1=Employee(p1.name,p1.identifier,p1.email,c1,'jnr',10000)  
c2 = Contact(2222222222, 'abc')
p2 = Person('p2', 200, 'email', c2)
e2=Employee(p2.name,p2.identifier,p2.email,c2,'snr',20000) 
c3 = Contact(3333333333, 'abc')
p3 = Person('p3', 300, 'email', c3)
e3=Employee(p3.name,p3.identifier,p3.email,c3,'Tc',30000) 
c4 = Contact(1111111111, 'abc')
p4 = Person('p4', 400, 'email', c4)
e4=Employee(p4.name,p4.identifier,p4.email,c4,'snr',40000) 
dict(c1,p1) 
dict(c2,p2)
dict(c3,p3) 
dict(c4,p4)

get_details(c2.number,[e1,e2,e3,e4])#get details by giving phone number
get_number(p1.identifier,[e1,e2,e3,e4]) #get number by giving id