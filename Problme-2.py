a = int(input())

result_list = []
for i in range(1, (2*a)):
    if (i % 2 != 0):
        result_list.append(str(i))
        
print(",".join(result_list))