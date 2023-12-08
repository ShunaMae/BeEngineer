class Human:
    def __init__(self, name, age):
        """コンストラクタ"""
        self.name = name
        self.age = age 
    
    def set_occupation(self, occupation):
        self.occupation = occupation
        print(self.name, "さんの職業は", self.occupation, "です。")
    
    def introduce(self):
        print("Name:", self.name, "Age:", self.age, "Occupation:", self.occupation)


yamada = Human("Yamada", 25)
yamada.set_occupation("student")
yamada.introduce()