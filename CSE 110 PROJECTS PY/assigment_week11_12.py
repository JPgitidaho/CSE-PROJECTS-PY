"""
Milestone Week 11-12 -Assignment - Data Analysis
Juanita Perez - CSE 110 | Programming Building Blocks

  **Exceeding Requirements**: Allow the user to type in a country, then 
  show the minimum, maximum, and average life expectancy for that country.
  
"""

high_life_exp = 0
high_life_exp_year = 0
high_life_exp_entity = ''

low_life_exp =1000
low_life_exp_year = 1000
low_life_exp_entity = ''

choice_max_life_exp = 0
choice_max_life_exp_year = 0
choice_max_life_entity = ''

choice_min_life_exp = 1000
choice_min_life_exp_year = 1000
choice_min_life_entity = ''

choice_min_entity_exp = 1000
choice_min_entity_year = 1000
choice_min_entity_exp_entity =''

choice_max_entity_year = 0
choice_max_entity_exp = 0
choice_max_entity_exp_entity = ''
count = 0
counter = 0
i = 0
avg_life_exp = 0
avg_entity_life_exp = 0



print()
choice_year = int(input(f'Enter the year of interest for data based on all countries :'))
print()
choice_entity = str(input(f'Enter the country of interest:'))


# Download the dataset 
# Load the dataset in your Python program
# Iterate through the data line by line

with open('week 11/life-expectancy.csv')as life_expectancy_file:
    for line in life_expectancy_file:
        i = i+ 1
        clean_line = line.strip()
        # Split each line into parts
        parts = clean_line.split(',')
        if i > 1:
            entity = parts[0]
            code = parts[1]
            year = int(parts[2])
            life_exp = float(parts[3])
        # with this ob code we will have the total life expectancy. 
        # The maximum and minimum of all countries
            if high_life_exp < life_exp:
                high_life_exp = life_exp
                high_life_exp_year = year
                high_life_exp_entity = entity
            if  low_life_exp > life_exp:
                low_life_exp = life_exp
                low_life_exp_year = year
                low_life_exp_entity = entity 
            # With this code the average will be obtained 

            if choice_year == year:
                avg_life_exp = avg_life_exp + life_exp
                counter += 1
            # if the option is per year, then the maximum and
            # minimum will be obtained according to the YEAR
                if  choice_max_life_exp < life_exp:
                    choice_max_life_exp = life_exp
                    choice_max_life_entity = entity 
                    choice_max_life_year = year
                    
                if  choice_min_life_exp > life_exp:
                    choice_min_life_exp = life_exp
                    choice_min_life_entity = entity
                    choice_min_life_year = year
            #   With this code the user will access the information by Entity
            if choice_entity == entity.lower():
                print(f'>>{entity}<<--{year}-- {life_exp:.2f}')
                avg_entity_life_exp = avg_entity_life_exp + life_exp
                count += 1
                                    
                if  choice_min_entity_exp > life_exp:
                    choice_min_entity_exp = life_exp
                    choice_min_entity_exp_entity = entity
                    choice_min_entity_year = year
                                                        
                if  choice_max_entity_exp < life_exp:
                    choice_max_entity_exp = life_exp
                    choice_max_entity_exp_entity = entity
                    choice_max_entity_year = year
                                                
                    
# With this code, the life expectancy will be averaged by country and the life expectancy will be averaged per year.
avg_life_exp = avg_life_exp / counter
avg_entity_life_exp = avg_entity_life_exp / counter

print(f'The overall min life expectancy is: {low_life_exp:.2f}-{low_life_exp_year}-{low_life_exp_entity}')  
print(f'The overall max life expectancy is: {high_life_exp:.2f}-{high_life_exp_year}-{high_life_exp_entity}')
print('')
print(f'For the year {choice_year}:')
print(f'The average life expectancy across all countries was {avg_life_exp:.2f}')
print()
print(f'The min life expectancy was in {choice_min_life_year} {choice_min_life_entity.capitalize()} with {choice_min_life_exp:.2f}')
print(f'The max life expectancy was in {choice_max_life_year} {choice_max_life_entity.capitalize()} with {choice_max_life_exp:.2f}')
print()
print(f'For the country {choice_entity.capitalize()}:')
print(f'The min life expectancy was in {choice_min_entity_exp_entity} {choice_min_entity_year} with {choice_min_entity_exp:.2f}')
print(f'The max life expectancy was in {choice_max_entity_exp_entity} {choice_max_entity_year} with {choice_max_entity_exp:.2f}')
print()
print(f'The average life expectancy was {avg_entity_life_exp:.2f}')



