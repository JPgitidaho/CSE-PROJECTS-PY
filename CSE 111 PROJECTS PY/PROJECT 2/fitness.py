from datetime import datetime


def main ():
    gender = input('Please enter your gender (M or F): ')
    birthdate =input('Enter your birthdate (YYYY-MM-DD): ')
    pounds = int(input('Enter your weight in U.S. pounds : '))
    inches = int(input('Enter your height in U.S. inches: '))
    feets = int(input('Enter your height in U.S. feet: '))
    stones = int(input('Enter weight in British stones:'))
    years = compute_age(birthdate)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    mt = mt_from_in(inches)
    kg = kg_from_stone(stones)
    cm = cm_from_ft(feets)
    
    bmi = body_mass_index(kg, cm)
    
    bmr = basal_metabolic_rate(gender, kg, cm, years)
    
    print(f"Age (years): {years}")
    print(f"Weight (from lb to kg): {kg:.2f}")
    print(f"Weight (from st to kg): {kg:.2f}")
    print(f"Height (from in to cm): {cm:.1f}")
    print(f"Height (from cm to mt): {mt:.1f}")
    print(f"Height (from feet to cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year 
    
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years

# Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg

# Converts the weight from pounds to British stone (1 lb = 0.0714286 st).
def kg_from_stone(stones):
    kg = stones * 0.0714286
    return kg

#  Converts inches to centimeters (1 in = 2.54 cm).
def cm_from_in(inches):
    cm = inches * 2.54
    return cm

#  Converts inches to meters (1 in = 0.0254 mt).
def mt_from_in(inches):
    mt = inches * 0.0254
    return mt

#  Converts feet to centimeters (1 ft = 30.48).
def cm_from_ft(feets):
    cm = feets * 30.48
    return cm

# Calculates age, BMI
def body_mass_index(wheigth, height):
    bmi = wheigth / (height ** 2) * 10000
    return bmi
# Calculates age, BMR
def basal_metabolic_rate(gender, weigth, height, age):
    
    if gender.upper() == 'F':
       bmr = 447.593 + 9.247 * weigth + 3.098 * height - 4.330* age
    else:
       bmr = 88.362 + 13.397* weigth + 4.799 * height - 5.677 * age
    return bmr
    


    
main()
