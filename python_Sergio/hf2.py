word = "bottles"
for beerNum in range(99, 0, -1):
    print(beerNum, word, "of beer on the wall")
    print(beerNum, word, "of beer")
    print("Take one down")
    print("Pass it around")
    if beerNum == 1:
        print("No more bottles of beer on the wall")
    else:
        newNum = beerNum - 1
        if newNum == 1:
            word = "bottle"
        print(newNum, word, "of beer on the wall")
    print()