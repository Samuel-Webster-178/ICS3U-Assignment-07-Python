#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the perimeter of a square
#     with inputted side length


def reorder_list(inpt=[]):
    # I take an inputted list and reorder it based on length of strings
    outpt = []
    for counter1 in range(len(inpt)):
        counter2 = 0
        for string in outpt:
            if len(string) > len(inpt[counter1]):
                counter2 += 1
        outpt.insert(counter2, inpt[counter1])
    return outpt


def main():
    # I am main, I manage input and output
    inpt = []

    # input
    while True:
        # I repeat until valid input is given
        inpt.append(input("Enter string:"))
        if inpt[len(inpt) - 1] == "-Finish":
            inpt.pop()
            break

    # call function
    outpt = reorder_list(inpt)

    # output
    print("\nInput from longest to shortest is: {}".format(outpt))
    print("\nDone.")


if __name__ == "__main__":
    main()
