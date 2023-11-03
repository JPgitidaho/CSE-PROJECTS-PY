'''
CSE 111 - Prove Activity - Week 9-10 Juanita P. Aguilera
Exceeded Requirements
Included:
- Write code to discount the product prices by 10% if today is Tuesday or Wednesday.
- Write code to discount the product prices by 10% if the current time of day is before 11:00 a.m.
- Write code to print a coupon at the bottom of the receipt.
- Write the code so that it will always print a coupon for one of the products ordered by the customer.
- Write code to print at the bottom of the receipt an invitation for the customer to complete an online survey.
- Add a new function called generate_invoice that receives the list of ordered items and the invoice number.
  The function generates an invoice with the requested items, including invoice number, item details, subtotal,
  sales tax, and total.
'''
import csv
import datetime
import random

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters:
        filename (str): the name of the CSV file to read.
        key_column_index (int): the index of the column to use as the keys in the dictionary.
    
    Returns:
        dict: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            key = row[key_column_index]
            if key in dictionary:
                dictionary[key].append(row)
            else:
                dictionary[key] = [row]
    return dictionary

def apply_discount(price):
    """
    Apply a 10% discount to the given price.
    """
    return price * 0.9

def generate_coupon(product):
    """
    Generate a coupon for the given product.
    """
    coupon_code = random.randint(1000, 9999)
    return f"Get 20% off on your next purchase of {product} with coupon code: {coupon_code}"

def generate_invoice(items, invoice_number):
    """
    Generate an invoice for the ordered items.

    Parameters:
        items (list): a list of items to include in the invoice.
        invoice_number (int): the invoice number.

    Returns:
        None
    """
    products_dict = read_dictionary('CSE 111/WEEK_9/MILESTONE_TEXT/products.csv', 0)
    subtotal = 0
    print(f"\nInvoice #{invoice_number}")
    print("------------------------------")

    # Iterate over the ordered items
    for item in items:
        product_number = item[0]
        quantity = int(item[1])

        if product_number in products_dict:
            # Get the product details
            product_details = products_dict[product_number][0]
            product_name = product_details[1]
            price = float(product_details[2])

            # Apply discount if applicable
            if is_discount_day() or is_before_11am():
                price = apply_discount(price)

            subtotal += price * quantity
            print(f"{product_name}: {quantity} @ ${price:.2f}")

            # Generate a coupon for the product
            coupon = generate_coupon(product_name)
            print("Coupon:", coupon)
        else:
            print(f"Error: unknown product number '{product_number}'")

    sales_tax = subtotal * 0.07
    total = subtotal + sales_tax
    print("------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("------------------------------")
    print("Please complete our online survey!")

def is_discount_day():
    """
    Check if today is Tuesday or Wednesday.

    Returns:
        bool: True if today is Tuesday or Wednesday, False otherwise.
    """
    today = datetime.datetime.today().weekday()
    return today == 1 or today == 2

def is_before_11am():
    """
    Check if the current time is before 11:00 a.m.

    Returns:
        bool: True if the current time is before 11:00 a.m., False otherwise.
    """
    current_time = datetime.datetime.now().time()
    return current_time < datetime.time(11, 0)

def main():
    try:
        items = []
        products_dict = read_dictionary('CSE 111/WEEK_9/MILESTONE_TEXT/products.csv', 0)
        with open('CSE 111/WEEK_9/MILESTONE_TEXT/request.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                items.append(row)
        generate_invoice(items, 12345)
    except FileNotFoundError:
        print("Error: missing file")
    except PermissionError:
        print("Error: insufficient permissions to access the file")

if __name__ == '__main__':
    main()
