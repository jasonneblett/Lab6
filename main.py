# ******************************************************************************
# Author:           Jason Neblett
# Lab:              Lab 6
# Date:             02/20/2022
# Description:      Classes and Objects
# Input:            Dictionary of names, dates, gender, and number 
# Output:           Dictionary List of names, dates, gender and number


from Name import *
from Database import Database


def main():
    names = Name.readNames(cls)
    for names in names:
        print(f"{names['name']}\t{names['year']}\t{names['gender']}\t{names['Count']}")

    year = Database.year()
    gender = Database.gender()


if __name__ == "__main__":
    main()