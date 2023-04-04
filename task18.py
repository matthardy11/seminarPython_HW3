# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

number = int(input("Введите количество элементов в массиве: "))
counter = 0
array = []

for i in range(number):
  array.append(counter+1)
  counter+=1

array.sort() # в моем случае не нужно т.к. массив заполнятеся цифрами по порядку, как в примере. Это на случай использования рандомных чисел

findNumber = int(input("Введите искомое число: "))
minNumber = 0

for i in range(len(array)):
  if findNumber > array[0] and findNumber < array[len(array)-1]:
    for j in range(len(array)):
      if findNumber == array[j]:
        minNumber = findNumber
  elif findNumber < array[0]:
    minNumber = array[0]
  elif findNumber > array[len(array)-1]:
    minNumber = array[len(array)-1] 

print("Ближайшее число к искомому это", minNumber)      
