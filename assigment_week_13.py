''' 13 Prove: Assignment Wind Chill Calculations: Juanita Perez
Meets requirements:

Write a function to calculate and return the wind chill based on a given temperature and wind speed.

Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by(9/5) and then add 32.

Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.
SHOWING CREATIVITY :
Convert Kelvin to Fahrenheit'''



# Wind_Chill(ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

# T es la temperatura en grados farenheit

# V  es la velocidad del viento en millas por hora

# V^0.16 significa Va la potencia de 0.16, que se puede encontrar en Python usando el **operador.


# a function to calculate and return the wind chill based on a given temperature and wind speed.
def windspeed_calculation():
    for x in range(0, 60, 5):
        x += 5
        #a function to convert from Celsius to Fahrenheit. 
        #The formula for this conversion is to multiply the Celsius temperature by(9/5) and then add 32.
        if if_tem.upper() == 'C':
            tem_new = (tem * 9/5) + 32
            Wind_Chill = 35.74 + (0.6215*tem_new) - 35.75 * (x**0.16) + (0.4275*tem_new * (x**0.16))   
            print(f'At temperature {tem_new}F, wind speed at {x} mph. The windchill is: {Wind_Chill:.2f}F.')
        # a function to convert from Kelvin to Fahrenheit.
        # The formula for this conversion is to subtract the Kelvin temperature by(1.8) and then add 32.
        if if_tem.upper() == 'K':
            tem_new =((tem -273.15) * 1.8) + 32   
            Wind_Chill = 35.74 + (0.6215*tem) - (35.75 * (x**0.16)) + (0.4275*tem*(x**0.16))
            print(f'At temperature {tem}F, and wind speed at {x} mph. The windchill is: {Wind_Chill:.2f}F. ')
        elif if_tem.upper() == 'F':
            Wind_Chill = 35.74 + (0.6215*tem) - (35.75 * (x**0.16)) + (0.4275*tem*(x**0.16))
            print(f'At temperature {tem}F, and wind speed at {x} mph. The windchill is: {Wind_Chill:.2f}F. ')
        


tem = float(input('What is the temperature? ')) 
if_tem = input('Kelvin, Fahrenheit or Celsius (K/F/C)? ').upper()
print()
windspeed_calculation()
