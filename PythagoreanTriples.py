"""
    This program uses the formula for calculating Pythagorean triples using transformations of integer coordinate points on the complex plane.
    The formula is based off of 3blue1brown's explanation for calculating Pythagorean triples, given here: https://www.youtube.com/watch?v=QJYmyhnaaek
    
    The program will NOT generate all Pythagorean triples in a given range - see video for why!
"""

limit = int(input()) # Determines highest value that will be plugged into formula

print(
    [
        {2 * i * j, i ** 2 - j ** 2, i ** 2 + j ** 2} # Returns a Pythagorean triple

        for i in range(1, limit + 1)
        for j in range(1, limit + 1)

        if i != j and i ** 2 - j ** 2 > 0 # Ensures that there are no triples with zero or negative values
    ]
)