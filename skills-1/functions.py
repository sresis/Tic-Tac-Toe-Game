"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

#sets hometown as global variable
HOMETOWN = 'Palatine'

def is_hometown(town):

    # returns evaluation of whether town is the same as my hometown
    return town == HOMETOWN

"""print(is_hometown('Chicago'))
print(is_hometown('Palatine'))"""

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here

def return_full_name(first, last):

    full_name = (f'{first} {last}')

    return full_name

# print(return_full_name('Stephanie', 'Resis'))

    
"""
PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here
def print_hometown_greeting(first, last, town):
    # evaluates which greeting to print based on if person is from hometown
    if is_hometown(town):
        print(f"Hi {first} {last}, we're from the same place!")
    else:
        print(f"Hi {first} {last}, I'd like to visit {town}!")

# print(print_hometown_greeting('Abby', 'Adams', 'Palatine'))
# print(print_hometown_greeting('Bob', 'Smith', 'Los Angeles'))

"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# sets berries as global variable
BERRIES = ['strawberry', 'raspberry', 'blackberry', 'currant']

def is_berry(fruit):

    return fruit in BERRIES

# print(is_berry('currant'))
# print(is_berry('durian'))



"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""
def return_shipping_cost(item):

    if item in BERRIES:
        return int(0)
    else:
        return int(5)
# print(return_shipping_cost('strawberry'))
# print(return_shipping_cost('eggs'))

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# sets tax rates/fees as global variables
CA_TAX = .03
PA_FEE = 2
MA_TAX_UNDER_100 = 1
MA_TAX_OVER_100 = 3
# function to return the total cost after taxes/special fees
def return_total_cost(base_price, state, tax = .05):

    price_with_tax = int(base_price) * (1 + float(tax))
    
    # if state is CA, PA, MA --> add special tax
    if state == 'CA':
        total_price = price_with_tax * (1 + float(CA_TAX))
    elif state == 'PA':
        total_price = price_with_tax + PA_FEE
    elif state == 'MA':
        if base_price <= 100:
            total_price = price_with_tax + MA_TAX_UNDER_100
        else:
            total_price = price_with_tax + MA_TAX_OVER_100
    # if not in CA, PA, MA --> total pricce is price with tax
    else:
        total_price = price_with_tax

    return round(total_price,2)

# ** think if you want to round these
# print(return_total_cost(5, 'CA', .1))
# print(return_total_cost(10, 'IL'))
# print(return_total_cost(100, 'MA'))
# print(return_total_cost(200, 'MA'))
# print(return_total_cost(200, 'PA', .1))

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

def add_to_list(list, *items):

    for item in items:
        list.append(item)

    return list

# print(add_to_list(['apple', 'pear', 'grape'], 'berries', 'plums', 'eggs'))
# print(add_to_list(['abc'], 1, 2, 'cde'))



"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

def return_tuple(word):

    # defines inner function to multiply given word by 3x
    def return_word_3x(word):
        new_word = word * 3
        return new_word

    # creates tuple consisting of word and word produced in inner function
    new_tuple = (word, return_word_3x(word))

    return new_tuple


# print(return_tuple('hi'))
# print(return_tuple('gretings'))



