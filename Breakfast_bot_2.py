#!/usr/bin/python
# -*- coding: utf-8 -*-

# A break fast app

import time


# most important functions

def print_pause(string):

    print(string)

    time.sleep(2)


def valid_input(prompt, option1, option2):

    response = input(prompt).lower()

    if option1 in response:
        return response
    elif option2 in response:

        return response
    else:

        print_pause("Sorry, I don't understand!")


# Intro

def intro():

    print_pause('Hello! I am Bob, the Breakfast Bot.')

    print_pause('Today we have two breakfasts available.')

    print_pause('The first is waffles with strawberries and whipped cream.'
                )

    print_pause('The second is sweet potato pancakes with butter and syrup.'
                )


# Get Order

def get_order():

    order = \
        valid_input('''Please order here.
What would you like? waffles or pancakes
''',
                    'waffles', 'pancakes').lower()

    if order == 'pancakes':
        print_pause('Pancakes it is!')
    elif order == 'waffles':

        print_pause('Waffles it is!')
    else:

        print_pause("Sorry I don't understand!")


# Order again

def order_again():
    order_again = \
        valid_input('''What would you like next?
Please enter yes or no
''',
                    'yes', 'no')
    if 'yes' in order_again:
        print_pause('Great! What would you like?\n')
        get_order()
    elif 'no' in order_again:

        print_pause('Thanks for ordering!')
    else:

        print_pause("I don't understand!")

    print_pause('Your order will be ready shortly!')


def order_breakfast():

    intro()

    get_order()

    order_again()


while True:

    order_breakfast()
