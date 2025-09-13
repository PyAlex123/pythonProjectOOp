# class Student:
#     print("hi")
#     def __init__(self):
#         self.height = 160
#         print("a am Alive")
#
# first_student = Student()
# Student.__init__(self=first_student)
# print(first_student.height)

# class Student:
#     amount_of_students = 0
#     def __init__(self,n,s,h=160):
#         self.name = n
#         self.surename = s
#         self.height = h
#         Student.amount_of_students += 1
#     def Greating(self):
#         print(f"Hi a am  {self.surename} {self.name} ")
#     def getHeight(self):
#         return self.height
#     def __bool__(self):
#         return self.name!=None
#     def __len__(self):
#         return self.height
#
#     # def __del__(self):
#     #     print("Training is over.I am now an expert!")
#
# first_student = Student("Ivan","Ivanov",185)
# print(first_student.name)
# first_student.Greating()
# print(first_student.getHeight())
# second_student =Student("Mariya","Markina",)
# print(second_student.getHeight())
# print(first_student.amount_of_students)
# print(Student.amount_of_students)
# # print(first_student.__len__())


import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
    def end_of_day(self):
            print(f "Gladness = {self.gladness}")
            print(f"Progress ={round(self.progress, 2)}")
    def live(self, day):
            day = "Day" + str(day) + "of" +self.name + "life"
            print(f"{day:=^50}")
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
                self.end_of_day()
                self.is_alive ()
nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)


