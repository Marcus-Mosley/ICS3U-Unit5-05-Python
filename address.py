#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on November 2020
# This program gives the proper format for a Canadian Address


def address_format(addressee, str_num, str_name, city, province,
                   postal_code, apprt_num=None):

    # Gets a users name and prints out their formal name

    if apprt_num is not None:
        full_address = addressee + "\n" + apprt_num + "-" + str_num + " "
        full_address += str_name + "\n" + city + " " + province + " "
        full_address += postal_code
    else:
        full_address = addressee + "\n" + str_num + " " + str_name + "\n"
        full_address += city + " " + province + " " + postal_code

    print(full_address)


def main():
    # This function receives input
    apprt_num = None

    print("Use Caps Only!")
    print(" ")

    addressee = input("Enter the name of the addressee: ")
    apprt_question = input("Do you have an Apartment Number?: ")
    if apprt_question.upper() == "Y" or apprt_question.upper() == "YES":
        apprt_num = input("Enter the Apartment Number: ")
    str_num = input("Enter the Street Number: ")
    str_name = input("Enter the Street Name: ")
    city = input("Enter the City Name: ")
    province = input("Enter the Province: ")
    postal_code = input("Enter the Postal Code: ")
    print(" ")

    if apprt_num is not None:
        address_format(addressee, str_num, str_name, city,
                       province, postal_code, apprt_num)
    else:
        address_format(addressee, str_num, str_name, city,
                       province, postal_code)

    # print(full_address)


if __name__ == "__main__":
    main()
