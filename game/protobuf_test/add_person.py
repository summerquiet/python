#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
This is a python sample for protobuf test
'''

import sys
import addressbook_pb2

def prompt_for_address(person):
    '''function for prompt for address'''
    try:
        person.id = int(input("Please input the id of this person... "))
    except ValueError as v_e:
        raise ValueError(v_e)
    person.name = input("Please input a name for the person... ")
    email = input("Please enter the email address of the person.... ")

    if email != "":
        person.email = email

    while True:
        number = input("Enter a phone number: ")
        if number == "":
            break

        phone_number = person.phone.add()
        phone_number.number = number

        type_str = input("Is this a mobile 'm', home 'h', or work 'w' phone? ")
        if type_str == 'm':
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif type_str == 'h':
            phone_number.type = addressbook_pb2.Person.HOME
        elif type_str == 'w':
            phone_number.type = addressbook_pb2.Person.WORK
        else:
            print("Unknown phont type, leaving as default value.")

def main():
    '''main function for this py'''
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
        sys.exit(-1)

    print("What am i doing....")
    address_book = addressbook_pb2.AddressBook()

    try:
        read_f = open(sys.argv[1], "rb")
        address_book.ParseFromString(read_f.read())
        read_f.close()
    except IOError:
        print(sys.argv[1] + " : File not found. Creating a new file")

    print(address_book)
    for p in address_book.person:
        print(p.name + ',' + str(p.id) + ',' + p.email)
        for ph in p.phone:
            print(ph.number, ph.type)

    try:
        prompt_for_address(address_book.person.add())

        try:
            write_f = open(sys.argv[1], "wb")
            write_f.write(address_book.SerializeToString())
            write_f.close()
        except IOError:
            print(sys.argv[1] + " : File write error")
    except ValueError:
        print("Invalid ID input all end")

if __name__ == '__main__':
    main()

#EOF
