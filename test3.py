def sum_list(x):
    sum=0
    for n in x:
        sum=sum+n
    return sum

list1=list(map(int,input("수를 입력하세요(예:1,2,3):").split(',')))

print(list1)
print(sum_list(list1))