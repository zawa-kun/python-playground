class Animal:
    def speak(self):
        print("動物が泣きます")

class Dog(Animal):
    # 親クラスのメソッドン内容を上書きする -> "オーバーライド"
    def speak(self):
        print("わんわん！")

animal = Animal()
print("親クラス：Animal")
animal.speak()

dog = Dog()
print("子クラス：Dog")
dog.speak()