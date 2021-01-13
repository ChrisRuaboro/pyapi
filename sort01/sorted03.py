#!/usr/bin/env python3

simpsons = [('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34)]

def take_second(secondplacewins):
    return secondplacewins[1]


def sortbyagesandname(dataset):

    sortedbyages = sorted(dataset, key = take_second)

    print(sortedbyages)

sortbyagesandname(simpsons)

