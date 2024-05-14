def test(a, *args, txt="Тестовые данные:", **values):
    for i in args:
        b = i+a
        print(txt, b, values)

test(5, 7,8,9, name='Ruzil')


print ("Введите число:")
n = int(input())
def factorial(n):
   if n==1 or n==0:
        return 1
   else:
        return factorial(n-1)*n

print('Факториал числа = ', factorial(n))
