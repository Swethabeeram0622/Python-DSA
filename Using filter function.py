# printing ages greater than 18 using filter.
ages = (31, 42, 18, 16, 17, 22, 23)
def myfunction(x):
    if x> 18:
        return True
    else:
        return False
adults = filter(myfunction, ages)
for i in adults:
    print(i)  
