#List Comprehension

#Using for loop
squares = [x*x for x in range(1,6)]
print (squares)

#Using single if condition
evens = [x for x in range (1,11) if x % 2 == 0]
print (evens)

#Using if-else condition
result = ["Even" if x % 2 == 0 else "Odd" for x in range(1,6)]
print (result)

# Using Multiple if conditions
a = [x for x in range (1,31) if x % 2 == 0 if x % 3 == 0]
print(a)
 