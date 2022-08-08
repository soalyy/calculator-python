while True:
    try:
        x=int(input("Первое значение:"))
        y=int(input("Второе значение:"))
    except:
        print("Ошибка: Неверный формат данных")
    z=input("Операция:")
    if z=="+":
        print(x+y)
    elif z=="-":
        print(x-y)
    elif z=="*":
        print(x*y)
    elif z=="/":
        if y==0:
            print("Ошибка: Деление на 0")
        else:
            print(x/y)
    else:
        print("Ошибка: Неверный тип операции")
    