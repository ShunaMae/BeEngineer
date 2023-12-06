class Character():
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("私の名前は", self.name, "だ！")


class Brave(Character):
    def buy_weapon(self, weapon):
        self.weapon = weapon
        print(self.weapon, "を手に入れた！")

class Wizard(Character):
    def __init__(self, name):
        self.name = name
        self.magic_list = []

    def learn_magic(self, magic):
        self.magic = magic
        self.magic_list.append(magic)
        print(self.magic, "を覚えた！")
        print("現在使える魔法は", self.magic_list, "だ！")
    
    def introduce(self):
        super().introduce()
        print(self.magic_list, "が使える魔法使いだ！")
    
kei = Wizard("ケイ")
kei.introduce()
kei.learn_magic("回復の魔法")
kei.introduce()
kei.learn_magic("攻撃の魔法")
kei.introduce()