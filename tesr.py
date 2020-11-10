class A():
    def __init__(self):
        self.name = "A"
    def fly(self):
        print(f"{self.name} Can Fly")
class B():
    def __init__(self):
        self.name = "B"
    def fly(self):
        print(f"{self.name} Cannot Fly")
class C(B,A):
    def __init__(self,name):
        self.name = name
print()
print(C("A").name)
print("**********************")


