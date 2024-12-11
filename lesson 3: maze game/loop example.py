# declare x as a variable that we can find and change later
x = 0

while True:
    # depending on how much the code has to do, the loop will go faster or slower
    for i in range(0,1000000):
        square = i*i # random math that wastes time

    # increase x by 1
    x += 1

    print(x)