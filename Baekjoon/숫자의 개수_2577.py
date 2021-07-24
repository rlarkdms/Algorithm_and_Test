sum_value=1
for i in range(3):
    value=int(input())
    sum_value*=value

number=[0]*10

sum_value_str=str(sum_value)
for i in range(len(sum_value_str)):#개수 세기
    number[int(sum_value_str[i])]+=1

for k in range(0,10):#출력
    print(number[k])