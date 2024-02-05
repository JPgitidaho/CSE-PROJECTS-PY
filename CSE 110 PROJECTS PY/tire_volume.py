''' CSE 111: 01-02 Prove: Calling Functions
    Juanita Perez Aguilera
    Teacher : Brother William Clements

Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire
**Exceeding Requirements**: 
Find tire prices for four or more tire sizes online. 
Add a set of if … elif … else statements in my program 
that use the tire width, tire aspect ratio, and wheel 
diameter that the user enters to find a price and then print the price.
After your program prints the tire volume to the terminal window, your program should ask the user 
if she wants to buy tires with the dimensions that she entered. If the user answers “yes”, 
your program should ask for her phone number and store her phone number in the volumes.txt file.
In order to earn the remaining 7% of points: 
will show him that the number is scheduled to call him shortly. Also add a function to make additional 
discounts for the purchase of two or more wheels. 
As well as if you want less than two or more than 0 or if the customer knows that he can access a discount.
'''



import math
from datetime import datetime 
current_date_and_time = datetime.now()


count_item = []
counter = []

print('*'*100)
print('Thanks for visit the webpage. Enter the details of your tire to find out if there is an offer for you!')
print('*'*100)
# Tire Width
w = 174
while True:
    w = (input('Enter the width of the tire in mm (175mm-275mm): '))
    if w.isalpha() == True:
        print('You entered "' + str(w) + '" Only positive numbers are accepted,please try again.')
    elif int(w) <= 174:
        print(str('The number you entered is too small, please enter a widthbetween 185mm and 205mm. '))
    elif int(w) >= 276:
        print(str('The number you entered is too large, please enter a widthbetween 185mm and 205mm. '))
    else:
        w = math.ceil(float(w))
        break
#Tire Ratio
a = 29
while True:
    a = (input('Enter the aspect ratio of the tire (40- 70): '))
    if a.isalpha() == True:
            print('You entered "' + str(a) + '" Only positive numbers are accepted,please try again.')
    elif int(a) <= 39:
            print(str('The number you entered is too small, please enter a ratiobetween 185 and 205. '))
    elif int(a) >= 71:
            print(str('The number you entered is too large, please enter a ratiobetween 185 and 205. '))
    a = math.ceil(float(a))
    break
#Tire Diameter
d = 13
while True:
    d = (input('Enter the aspect ratio of the tire (14 - 20): '))
    if d.isalpha() == True:
        print('You entered "' + str(a) + '" Only positive numbers are accepted,please try again.')
    elif int(d) <= 13:
        print(str('The number you entered is too small, please enter a ratiobetween 185 and 205. '))
    elif int(d) >= 21:
        print(str('The number you entered is too large, please enter a ratiobetween 185 and 205. '))
    d = math.ceil(float(d))
    break
# Compute the volume of the tire
# Volume
v = (math.pi*w**2*a)*(w*a + 2540*d)/10000000000
print(f'The approximate volume is {v:.2f} liters.')
print()
# 175/65R14
if w == 175 and a == 65 and d == 14:
    print('We have  ASSURANCE MAXLIFE 175/65R14 Load Range XL tires in stock, they are $75.96 per tire. ')
#  205/55R16
elif w == 205 and a == 55 and d == 16:
    print('We have  Goodyear EFFICIENT GRIP ROF 205/55 R16 91W tires in stock, they are  $233.33  per tire. ')
# 225/60R18
elif w == 225 and a == 50 and d == 18:
    print('We have  Goodyear 225/60R18 Load RangeSL tires in stock, they are $210,805 per tire. ')
#225/60R16
elif w == 225 and a == 60 and d == 16:
    print('We have  Goodyear 225/60R16 Maximum Load (lbs)850 tires in stock, they are $301.73 per tire. ')
    print()
else :
    print('Your tires is not in ofert. However the price is still the lowest on the market ')
purchase = input('Would you like to purchase these tires? (yes or no)').lower()
print()
while True :    
    if  purchase.lower() == 'yes':
        number = int(input('Please enter your telephone number. '))
        # the quantity indicated by the user
        count_item = int(input('How many do you want to add: '))
        counter.append(count_item)
        #here list the order
        listNumber = 1
        # Here I show the user the quantity of product
        print(f'{listNumber}). {count_item} has been added to your order.')
        if count_item >= 2:
            print('    Your order will have an additional 15% discount.')
            
        elif count_item == 1 :
            print('    Your can access a discount for the purchase of two or more tires.')
            
        else :
            print('You have entered an incorrect number.')
       
# Open a text file named volumes.txt in append mode.
        f = open('volume.txt', 'at')
        f.write(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f},{number} \n')
        f.close
        print('Thank you for your visit. We will contact you shortly. ')
        print(f"{current_date_and_time:%Y-%m-%d} ")
        exit()
    elif purchase == 'no':
        # Open a text file named volumes.txt in append mode.
        f = open('volume.txt', 'at')
        #print(f"{current_date_and_time:%Y-%m-%d}")
        f.write(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f} \n ')
        f.close
        print('Thank you for your order. ')
        exit()
    else:
        print('Please enter yes or no')
            



