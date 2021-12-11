numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
a=len(numbers)
i=0
count=0
while i<len(numbers):
    c=numbers[i]
    if c>20 and c<40:
        count+=1
    i+=1
print(count)



