a = int(input())

result_list = []
if(a%2 == 0):
    for i in range(1, (2*a)-1):
        if (i % 2 != 0):
            result_list.append(str(i))
else:
    for i in range(1, (2*a)):
        if (i % 2 != 0):
            result_list.append(str(i))

print(",".join(result_list))