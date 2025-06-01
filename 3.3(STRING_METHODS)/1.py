#.upper
a = 'hello'.upper()
print(a)
# HELLO
##########################
a = 'HeLLO'.lower()
print(a)
# hello
##########################
s = 'hello world'
print(s.title())
# Hello World
##########################
s = 'hello world'
print(s.capitalize())
# Hello world
##########################
s = 'hellO wOrld!123'
print(s.swapcase())
# HELLo WoRLD!123
##########################
s = 'hello world'
print(s.count('o'))          # 2
print(s.count('o', 6))       # 1
print(s.count('l', 1, 3))    # 1
##########################
# * Вернет значение -1, если ничего не будет найдено
s = 'hello world'
print(s.find('o'))        # 4
print(s.find('ll'))       # 2
print(s.find('o', 5))     # 7
print(s.find('x'))        # -1
##########################
# * Вернет значение -1, если ничего не будет найдено
s = 'hello world'
print(s.rfind('o'))     # 7
print(s.rfind('ll'))    # 2
print(s.rfind('o', 5))  # 7
print(s.rfind('x'))     # -1
##########################
# * Можно указать сколько замен - удалений нужно сделать
s = 'hello world'
print(s.replace('o', '+'))    # hell+ w+rld
print(s.replace('l', ''))     # heo word
print(s.replace('l', '', 2))  # * heo world
print(s.replace(' ', ''))     # helloworld
##########################
text = "Python is best"
print(text.split())      # ['Python', 'is', 'best']
text = "Ivanov Ivan Ivaovich"
print(text.split('n'))   # ['Iva', 'ov Iva', ' Ivaovich']
text = "43,54,674,1434"
print(text.split(','))   # ['43', '54', '674', '1434']
##########################
s1 = 'hello world'
s2 = 'helloworld'
print(s1.isalpha())    # * False
print(s2.isalpha())    # True
##########################
s1 = '1234'
s2 = '12 34'
print(s1.isdigit())   # True
print(s2.isdigit())   # * False