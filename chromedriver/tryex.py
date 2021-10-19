x = input('Enter a number: ')
try:
    print(type(x), x)
    x = x.split(', ')
    x2 = list(map(int, x))
except:
    print("Произошло исключение")
else:
    print("Исключений не произошло")

def x2arifm():
    s = 0
    try:
        for i in x2:
            s += i
        suparf = s/len(x2)
    except:
        print('Error')
    print(suparf)

x2arifm()