def test_func():
    arr = []
    num = 1
    num2 = 16
    for x in range(9):
        arr.append([])
        for y in range(9):
            if x == y:
                arr[x].append(num)
                num += 2
            elif x+y == 8:
                arr[x].append(num2)
                num2 -= 2
            else:
                arr[x].append('')

    for x in arr:
        print(x)

print(test_func())