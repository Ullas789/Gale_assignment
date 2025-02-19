class Subjects:
    def __init__(self,sub_name,marks):
        self.sub_name=sub_name
        self.marks=marks

class Semester:
    def __init__(self,sem,subjects):
        self.sem=sem
        self.subjects=subjects

class Student:
    def __init__(self,name,id,branch,current_sem,semester):
        self.name=name
        self.id=id
        self.branch=branch
        self.semester=semester
        self.current_sem=current_sem
    def display(self):
        print(f"\nName: {self.name}\nId: {self.id}\nBranch: {self.branch}")
 



def get_details(id,semester,students):
    
    
    for student in students:
        
        if semester==None:
            semester=student.current_sem
            
            
        if student.id == id and semester!=None:
            for subject in semester.subjects:
                print(f"studentname:{student.name}  studentId :{student.id}  sem:{semester.sem} {subject.sub_name}:{subject.marks}")
        
        


s1_python=Subjects("python",100)
s1_cn=Subjects("cn",60)
s1_os=Subjects("os",70)
s1_ds=Subjects("ds",60)

sem1=Semester(1,[s1_python,s1_os])
sem2=Semester(2,[s1_ds])
sem3=Semester(3,[s1_cn])

s1=Student('student1',10,'cs',sem3,[sem1,sem2,sem3])


s2_python=Subjects("python",90)
# s2_cn=Subjects("cn",90)
s2_os=Subjects("os",80)
s2_ds=Subjects("ds",100)

sem1=Semester(1,[s2_python,s2_os])
sem2=Semester(2,[s2_ds])
# sem3=Semester(3,[s2_cn])

s2=Student('student2',20,'cs',sem2,[sem1,sem2])



get_details(10,sem1,[s1,s2]) #getting the marks using Id
get_details(20,None,[s1,s2])
