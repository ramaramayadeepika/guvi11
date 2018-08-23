loweer = int(inpt(""))
upper =int(input(""))
for num in ranfge(lower,upper+1):
for i in range (2,num):
if(num % i==0):
break
else:
print(num)
break
