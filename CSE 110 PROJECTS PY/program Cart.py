"""
Milestone Week 09 - Juanita Perez - CSE 110 | Programming Building Blocks

  **Exceeding Requirements**: Consider that it would be a good option to give
    the user the option to add a product but also choose the quantity of it. 
    My code adds the entered quantity of the product for each item added. 
    So in total not only adds items but also adds the quantity of each item.
    Thus giving a complete total. Subtracting items and prices that have been removed.
    Also this time, validate input when there is a type error in most cases is 
    something I need to improve.
    I also inform the user when he adds an existing product to the list. 
    In general, if you don't write what corresponds to the entry, it is reported 
    as incorrect and starts over with the option to continue and thus write correctly.
    Try to give my best :)
"""


list_cart = []
new_counter = []
new_prices = []
items = []
prices = []
counter = []

print("*"*80)
print('          Welcome to program Cart')
print("*"*80)
while True:
    
    print()
    print('1. Add item ')
    print('2. View cart ')
    print('3. Remove Item ')
    print('4. Compute total')
    print('5. Quit')
    print()
    select = input('**Please type in a number to go on: ')
    print()
    if select == '1':
        item = input('** What would you like to add?:  ')
        item = item.lower()  # with this option validate the input and transform it into lowercase
        if item in items:  # with this if I validate the entry of the product that is repeated in the cart
            print('**This product is ready in the car')
        else:
            price = float(input(f'**Enter the price of {item.capitalize()}: $'))
            # here the user indicates the quantity of the item he wants
            count_item = int(input('**How many do you want to add: '))
            print()
            items.append(item)
            prices.append(price)
            counter.append(count_item)
            # here the price of the product is multiplied by the quantity indicated by the user
            new_price = count_item * price
            listNumber = 1
            # Here I show the user the capitalized product
            print(f'  {listNumber}). {count_item} {item.capitalize()} has been added to your cart.')
            # here the new price of the article and the quantity are printed
            print(f'  The price is ${new_price}.')
            continue
    elif select == '2':
        count_item = 0
        listNumber = 1
        for i in range(len(items)):
            print(f'{listNumber}). {counter[i]} {items[i]} ${prices [i]} each one.')
            count_item += 1
            listNumber += 1
        continue
    elif select == '3':
        count_item = 0
        listNumber = 1
        for i in range(len(items)):
            print(f' {listNumber}. {counter[i]} {items[i]} ${prices[i]} ')
            count_item += 1
            listNumber += 1
        #  choose the pop option to remove the price and remove to remove the
        # item and ensure it is completely removed
        takeout = input('**Type the name of item that you would like to remove: ')
        # with this option validate the input and transform it into lowercase
        takeout = takeout.lower()
        prices.pop(items.index(takeout))
        items.remove(takeout)
        print(f'  {takeout.capitalize()} has been removed.')
        continue

    elif select == '4':
        count_item = 0
        listNumber = 1
        total_price = 0
        for i in range(len(items)):
            print(f' {listNumber}. {counter[i]} {items[i]} ')
            count_item += 1
            listNumber += 1
            # I transformed the lists into variables
            # to be able to multiply them and thus obtain my total
            new_counter = counter[i]
            new_prices = prices[i]
            list_cart = new_counter * new_prices
            total_price += list_cart

        print(f"Your total is: ${total_price}")

    elif select == '5':
        print('**Thank you. Comeback soon**.')
        print()
        break
    else:
        #  with this option I validate the incorrect inputs
        print('*'*50)
        print('Type a correct option! ')
        print('*'*50)
