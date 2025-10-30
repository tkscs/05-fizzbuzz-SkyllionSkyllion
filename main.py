a = 3
b = 5
fizz = "ido is dumb"
buzz = "ido is stupid"
fizzbuzz = "ido is a stinky"

for i in range (1000000):
    if i % b == 0 and i % a != 0:
        print (fizz)
    elif i % a ==0 and i % b != 0:
        print (buzz)
    elif i % a ==0 and i % b == 0:
        print (fizzbuzz)
    else:
        print (i)