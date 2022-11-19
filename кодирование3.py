import math
def ChoiceProblem():
    print("Задачу на что вы хотите решить? : 1 - информация, 2 - звук, 3 - изображение")
    n = int(input())
    if n == 1:
        res = inf()
    elif n == 2:
        res = sound()
    elif n == 3:
        res = img()
    else:
        print("Введите другое значение")
        return
    print("Ответ на вашу задачу: ", res)
    return

def sound():
    print("Что хотите найти? (1 - объем, 2 - частота дискретизации, 3 - время записи, 4 - разрядность квантования")
    arg = int(input())
    if arg == 1:
        H = int(input("Введите частоту: "))
        t = int(input("Введите время: "))
        b = int(input("Введите разрядность: "))
        return H * t *b
    elif arg == 2:
        I = int(input("Введите объем: "))
        t = int(input("Введите время: "))
        b = int(input("Введите разрядность: "))
        return I // (t * b)
    elif arg == 3:
        I = int(input("Введите объем: "))
        H = int(input("Введите частоту: "))
        b = int(input("Введите разрядность: "))
        return I // (H * b)
    elif arg == 4:
        I = int(input("Введите объем: "))
        t = int(input("Введите время: "))
        H = int(input("Введите частоту: "))
        return I // (H * t)
    else:
        return "Введите другое значение"

def img():
    print ("Что хотите найти? (1 - кол-во цветов, 2 - глубина избражения)")
    arg = int(input())
    if arg == 1:
        i = int(input("Введите глубину изображения: "))
        return 2 ** i
    elif arg == 2:
        N = int(input("введите кол-во цветов: "))
        return math.log(N, 2)
    else:
        return "Введите другое значение"
def inf():
    print("Что хотите найти? (1 - информационный объем текста, 2 - мощность алфавита, 3 - количество символов, 4 - информационный вес символа)")
    arg = int(input())
    if arg == 1:
        a = int(input("Введите 1, если вы знаете информационный вес символа?"))
        if a == 1:
            i = int(input("Введите информационный вес символа: "))
            K = int(input("Введите количество символов: "))
            return i * K
        else:
            N = int(input("Введите мощность алфавита : "))
            K = int(input("Введите количество символов: "))
            return math.log2(N) * K
    elif arg == 2:
        i = int(input("Введите информационный вес символа: "))
        return 2**i
    elif arg == 3:
        a = int(input("Введите 1, если вы знаете информационный вес символа?"))
        if a == 1:
            i = int(input("Введите информационный вес символа: "))
            I = int(input("Введите информационный объем текста: "))
            return I / K
        else:
            N = int(input("Введите мощность алфавита : "))
            I = int(input("Введите информационный объем текста: "))
            return I / math.log2(N)
        
        
    elif arg == 4:
        N = int(input("Введите мощность алфавита : "))
        return math.log2(N)

    else:
        return "Введите другое значение"                                                                                                            

ChoiceProblem()