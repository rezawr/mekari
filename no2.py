# palindrome

def palindrome(num):
    # return True if num == num[::-1] else False
    arr_num = [int(x) for x in str(num)]
    count = len(arr_num) - 1
    reversed_arr_num = []

    while count >= 0:
        reversed_arr_num.append(arr_num[count])
        count -= 1

    flag = True
    for x in range(len(arr_num)):
        if arr_num[x] != reversed_arr_num[x]:
            flag = False
            break

    return flag


check_num = 123321
print(palindrome(check_num))