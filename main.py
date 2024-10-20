a=str(input("Введите строку: "))
b=str(input("Введите строку: "))
def proverka(a, b):
    return sorted(a) == sorted(b)  

if proverka(a, b): 
    print("Строки являются анаграммами.")  
else:
    print("Строки не являются анаграммами.") 
