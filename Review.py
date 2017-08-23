#Collin Patterson
#8/23/2017
#Mr. Davis
#Res in IT
import random
result = []
for x in range (10):
    num = random.randint(1,50)
    while num in result:
        num = random.randint(1,50)
    result.append(num)
print (result)