'''
#sum
number = [2, 4, 6]
print(sum(number))

#largestnum
number = [1, 2, 3, 100]
print(max(number))

#smallestnum
number = [4, 5, 6, 7]
print(min(number))


#evennumbers
a = [1, 2, 3, 4]
for number in a:
    if number %2 ==0:
        print(number)


# 5
a = [1, 2, 3, 4, 5]
for i in a:
    if i > 0:
        print(i)   
'''
#6
a = [1, 2, 3, 4, 5]
b=[]
for i in a:
    if i > 0:
        b.extend([i])

print(b)          