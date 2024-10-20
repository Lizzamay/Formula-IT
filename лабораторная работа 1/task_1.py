numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
skip = numbers[:4]
skipp = numbers[5:]
sklip = skip + skipp
total = sum(sklip) / len(numbers)
numbers[4] = total
print ("Измененный список:", numbers)
