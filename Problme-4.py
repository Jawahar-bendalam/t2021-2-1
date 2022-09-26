multiples_list = [1,2,3,4,5,6,7,8,9]
input_list = [1,2,8,9,12,46,76,82,15,20,30]

result_dict = {}
for i in multiples_list:
    count = 0
    for j in input_list:
        if j%i == 0:
            count += 1 
    result_dict[i] = count 
    
print(result_dict)