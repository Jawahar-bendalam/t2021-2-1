a = int(input())

result_list = []
i = 1 
while True:
    if (i % 2 == 1):
        result_list.append(str(i))
        if len(result_list) == a:
            break
    i += 1 

print(",".join(result_list))