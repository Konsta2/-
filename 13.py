'''1 задание'''
# class Cat():
#     name=''
#     color=''
#     weight=0
#     def bark(self):
#         print(self.name,'говорит МЯУ!')
# My_cat=Cat()
# My_cat.name='Красотка'
# My_cat.color='Шоколадная'
# My_cat.weight=4
# My_cat.bark()
#
'''2 задание'''
# class Animal():
#      name=''
#      def __init__(self, newName):
#          self.name = newName
#          print('Родилось животное', self.name)
#      def eat(self):
#          print(self.name,'Намням')
#      def makeNoise(self):
#          print(self.name,'говорит Гррр')
#      def setName(self,newName):
#          self.name=newName
#      def getName(self):
#          return self.name
#
# My_animal=Animal("Плюшка")
# print(My_animal.getName())
# My_animal.setName("Пупсик")
# print(My_animal.getName())
# My_animal.makeNoise()
# My_animal.eat()


'''3 Задание'''
# class StringVar():
#     pop=''
#     def __init__(self,new):
#         self.pop=new
#     def set(self,new):
#         self.pop=new
#         print(self.pop,'Как дела?')
#     def get(self):
#         return self.pop
# popi=StringVar("Пупс")
# print(popi.get())
# print(popi.set("Оляхандра"))
# print(popi.get())
'''4 задание'''
# class point():
#     def __int__(self,x:int,y:int):
#         self.x=x
#         self.y=y
#         print("Прочитал")
#     def set(self,newposx,newposy):
#         self.x= newposx
#         self.y=newposy
#         print('Поменял')
#     def get(self):
#         print(self.x,'и',self.y)
# potik=point()
# print(potik.set(9,8))
# print(potik.get())
'''5 задание'''
# class Animal():
#     name = ''
#     def __init__(self):
#         print("Я родительский конструктор")
# class Cat(Animal):
#     name='Шуша'
#     def __init__(self):
#         Animal.__init__(self)
#     def makeNoise(self):
#         print(self.name,'говорит Мяу')
# a=Cat()
# print(a.makeNoise())
# o=Animal()
'''6 задание'''
# class Animal():
#     def __init__(self):
#         print("Родительский конструктор")
# class Dog(Animal):
#     name = 'Шурша'
#     def __init__(self):
#         print('Родилась собака')
#         Animal.__init__(self)
#     def makeNoise(self):
#         print(self.name,'говорит Гав')
# k=Dog()
# print(k.makeNoise())
#
#
'''7 Задание'''
# class Animal():
#     name=""
#     def __init__(self):
#         print ("Создано животное")
#     def set(self, new):
#         self.name = new
#     def get(self):
#         return self.name
#     def eat(self):
#         print('Намням',self.name)
#     def makeNoise(self):
#         print('Просто орёт',self.name)
# class Cat (Animal):
#     name="кошечка"
# class dog(Animal):
#     name = "собачка"
# class Giraffe (Animal):
#     name="жиравчик"
# cats=Cat()
# cats.eat()
# cats.makeNoise()
# dogs=dog()
# dogs.eat()
# dogs.makeNoise()
# dogs=dog()
# dogs.eat()
# dogs.makeNoise()
# giraffe=Giraffe()
# giraffe.eat()
# giraffe.makeNoise()
