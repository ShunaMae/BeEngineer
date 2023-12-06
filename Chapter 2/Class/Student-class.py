class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        print("こんにちは", self.last_name, self.first_name, "さん")

class Student(Human):
    def set_club(self, club="帰宅部"):
        self.club = club 
        
    def greeting(self):
        super().greeting()
        print(self.last_name, "さんの部活は", self.club)

tanaka = Student("太郎", "山田")
tanaka.set_club()
tanaka.greeting()