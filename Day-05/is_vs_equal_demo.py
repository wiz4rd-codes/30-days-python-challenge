# Understanding Difference between is and "==" 
a = [10,20,30] # lists are mutable objects
b = [10,20,30]

# 'is' checks whether two variables refer to the same object.
# '==' checks whether two objects have equal values. 

print(a is b) #False
# returns false beacuse python create two different list 
print(a == b) #True
# returns True because both list contain same values

# Example with an immutable object :-
a = (10,20,30) #It's a tuple and tuple is immutable
b = (10,20,30)

print(a is b) #True
# It returns true because Python reused the same tuple object means both variable refers to same memory location 
print(a == b) #True
# Returns True because both tuples contain the same values.
