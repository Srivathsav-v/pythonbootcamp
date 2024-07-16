class studentinfo:
    def __init__(self,name,age,favorate_subject):
        self.name=name
        self.age=age
        self.favorate_subject=favorate_subject

    def fullinfo(self):
        return "name of the student:"+self.name+'age '+str(self.age)+'favorate subject is'+self.favorate_subject

s1=studentinfo('john snow',16,'maths')
s2=studentinfo('henry jay',15,'computers')

print(s1.fullinfo())
print(s2.fullinfo())
