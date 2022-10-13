import random

#comment
def game(a, v):
    if a == 1:
        p = int(input())
        print("Игрок взял", p, " камней, в куче осталось ", v - p)
    else:
        p = random.randint(1, 3)
        print("Компьютер взял", p, " камней, в куче осталось ", v - p)
    return v - p


n = random.randint(4, 30)
step = 1
print("В куче находится ", n, " камней перед началом игры")
print("Ход игрока первый, введите от 1 до 3")
while n > 3:
    n = game(step, n)
    step = (step + 1) % 2
if n == 1 and step == 1:
    print("Победил компьютер!")
elif n == 1 and step == 0:
    print("Победил игрок!")
elif step == 1:
    print("Победил игрок!")
else:
    print("Победил компьютер!")
