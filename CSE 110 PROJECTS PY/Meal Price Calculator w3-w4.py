# 03 Prepare: meal price
# Juanita P Aguilera

from ast import Break


meal_child = float(input("What is the price of a child's meal?: $ "))
meal_adult = float(input("What is the price of an adult's meal?: $ "))
children = int(input('How many children are there?: '))
adults = int(input('How many adults are there?: '))
sal_tax_rat = float(input('What is the sales tax rate?:$ '))
print()

subtotal_a = children * meal_child
subtotal_b = adults * meal_adult
Subtotal = subtotal_a + subtotal_b

Sale_Tax = (Subtotal * (sal_tax_rat / 100))

Total = Subtotal + Sale_Tax

print('Subtotal: ${:.2f}'.format(subtotal_a + subtotal_b))
print('Sale Tax: ${:.2f}'.format(Sale_Tax))
print('Total: ${:.2f}'.format(Subtotal + Sale_Tax))
print()# display a blank line


# tip in percenteg
print('1: If the diner is totally satisfied (1), calculate a 15 percent tip')
print('2: If the diner is satisfied (2), calculate a 10 percent tip')
print('3: If the diner is Notsatisfied (3), calculate a 5 percent tip')
print()     # display a blank line

satisfy=input('Satisfaccion rating: 1=Totally satisfied, 2 = satisfied, 3 = Dissatisfied: ' )

if satisfy == '1':
    tip = ((float(Total) *15 )/100)
    print('Very satisfied (1), calculate a 15% tip: ${:.2f}'.format(tip))
    print()  # display a blank line

if satisfy == '2':
    tip = ((float(Total) * 10 )/100)
    print('Satisfied (2), calculate a 10% tip: ${:.2f}'.format(tip))
    print()  # display a blank line

if satisfy == '3':
    tip = ((float(Total) * 5 )/100)
    print('Notsatisfied (3), calculate a 5% tip: ${:.2f}'.format(tip))
    print()  # display a blank line

# pay_amount
print('Total + tip: ${:.2f}'.format(tip + Total))
payment = float(input('What is the payment amount?:'))
print('Change: ${:.2f}'.format(payment-(Total+tip)))
print()  # display a blank line
