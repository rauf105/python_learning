# we can use this concept to create multilavel inheritence
class car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stoped..")

class toyotacar(car):
    def __init__(self, name):
        self.name=name

car1 = toyotacar("fortunar")
car2 = toyotacar("supra")

car1.start()