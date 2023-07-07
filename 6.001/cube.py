cube = 64
for i in range(abs(cube)+1):
    if i**3 >= abs(cube):
        break
if i**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        i = -i
    print('Cube root of ' + str(cube) + ' is ' + str(i))