''' CSE 111 - Prove Activity - Week 7-8 Juanita P. Aguilera 
Exceeded Requirements
Included:
Add a dictionary that contains known chemical formulas and their names.
Then write a function named get_formula_name with the following header 
and documentation string.
Call the get_formula_name function from main function and print the 
compound name for the user to see with the other output.
Add the atomic number for each element to the compound dictionary of elements. 
The atomic number of an element is the number of protons in the nucleus of that 
element. Write a function named sum_protons with the following header and 
documentation string.
Call the sum_protons function from  main function and print the number 
of protons for the user to see with the other output.
***The function compute_percent_composition(formula, periodic_table_dict) 
calculates the percent composition of a chemical compound based on its formula 
and the periodic table information provided.
'''
from formula import parse_formula

def make_periodic_table():
    periodic_table_dict = {
        "Ac": ["Actinium", 89, 227],
        "Ag": ["Silver", 47, 107.8682],
        "Al": ["Aluminum", 13, 26.9815386],
        "Ar": ["Argon", 18, 39.948],
        "As": ["Arsenic", 33, 74.9216],
        "At": ["Astatine", 85, 210],
        "Au": ["Gold", 79, 196.966569],
        "B": ["Boron", 5, 10.811],
        "Ba": ["Barium", 56, 137.327],
        "Be": ["Beryllium", 4, 9.012182],
        "Bi": ["Bismuth", 83, 208.9804],
        "Br": ["Bromine", 35, 79.904],
        "C": ["Carbon", 6, 12.0107],
        "Ca": ["Calcium", 20, 40.078],
        "Cd": ["Cadmium", 48, 112.411],
        "Ce": ["Cerium", 58, 140.116],
        "Cl": ["Chlorine", 17, 35.453],
        "Co": ["Cobalt", 27, 58.933195],
        "Cr": ["Chromium", 24, 51.9961],
        "Cs": ["Cesium", 55, 132.9054519],
        "Cu": ["Copper", 29, 63.546],
        "Dy": ["Dysprosium", 66, 162.5],
        "Er": ["Erbium", 68, 167.259],
        "Eu": ["Europium", 63, 151.964],
        "F": ["Fluorine", 9, 18.9984032],
        "Fe": ["Iron", 26, 55.845],
        "Fr": ["Francium", 87, 223],
        "Ga": ["Gallium", 31, 69.723],
        "Gd": ["Gadolinium", 64, 157.25],
        "Ge": ["Germanium", 32, 72.64],
        "H": ["Hydrogen", 1, 1.00794],
        "He": ["Helium", 2, 4.002602],
        "Hf": ["Hafnium", 72, 178.49],
        "Hg": ["Mercury", 80, 200.59],
        "Ho": ["Holmium", 67, 164.93032],
        "I": ["Iodine", 53, 126.90447],
        "In": ["Indium", 49, 114.818],
        "Ir": ["Iridium", 77, 192.217],
        "K": ["Potassium", 19, 39.0983],
        "Kr": ["Krypton", 36, 83.798],
        "La": ["Lanthanum", 57, 138.90547],
        "Li": ["Lithium", 3, 6.941],
        "Lu": ["Lutetium", 71, 174.9668],
        "Mg": ["Magnesium", 12, 24.305],
        "Mn": ["Manganese", 25, 54.938045],
        "Mo": ["Molybdenum", 42, 95.96],
        "N": ["Nitrogen", 7, 14.0067],
        "Na": ["Sodium", 11, 22.98976928],
        "Nb": ["Niobium", 41, 92.90638],
        "Nd": ["Neodymium", 60, 144.242],
        "Ne": ["Neon", 10, 20.1797],
        "Ni": ["Nickel", 28, 58.6934],
        "No": ["Nobelium", 102, 259],
        "Np": ["Neptunium", 93, 237],
        "O": ["Oxygen", 8, 15.9994],
        "Os": ["Osmium", 76, 190.23],
        "P": ["Phosphorus", 15, 30.973762],
        "Pa": ["Protactinium", 91, 231.03588],
        "Pb": ["Lead", 82, 207.2],
        "Pd": ["Palladium", 46, 106.42],
        "Pm": ["Promethium", 61, 145],
        "Po": ["Polonium", 84, 209],
        "Pr": ["Praseodymium", 59, 140.90765],
        "Pt": ["Platinum", 78, 195.084],
        "Pu": ["Plutonium", 94, 244],
        "Ra": ["Radium", 88, 226],
        "Rb": ["Rubidium", 37, 85.4678],
        "Re": ["Rhenium", 75, 186.207],
        "Rh": ["Rhodium", 45, 102.9055],
        "Rn": ["Radon", 86, 222],
        "Ru": ["Ruthenium", 44, 101.07],
        "S": ["Sulfur", 16, 32.065],
        "Sb": ["Antimony", 51, 121.76],
        "Sc": ["Scandium", 21, 44.955912],
        "Se": ["Selenium", 34, 78.96],
        "Si": ["Silicon", 14, 28.0855],
        "Sm": ["Samarium", 62, 150.36],
        "Sn": ["Tin", 50, 118.71],
        "Sr": ["Strontium", 38, 87.62],
        "Ta": ["Tantalum", 73, 180.94788],
        "Tb": ["Terbium", 65, 158.92535],
        "Tc": ["Technetium", 43, 98],
        "Te": ["Tellurium", 52, 127.6],
        "Th": ["Thorium", 90, 232.03806],
        "Ti": ["Titanium", 22, 47.867],
        "Tl": ["Thallium", 81, 204.3833],
        "Tm": ["Thulium", 69, 168.93421],
        "U": ["Uranium", 92, 238.02891],
        "V": ["Vanadium", 23, 50.9415],
        "W": ["Tungsten", 74, 183.84],
        "Xe": ["Xenon", 54, 131.293],
        "Y": ["Yttrium", 39, 88.90585],
        "Yb": ["Ytterbium", 70, 173.054],
        "Zn": ["Zinc", 30, 65.38],
        "Zr": ["Zirconium", 40, 91.224]
    }
    return periodic_table_dict


def get_formula_name(formula, known_molecules_dict):
    """Try to find the formula in the known_molecules_dict.
    If the formula is found, return the name of the chemical compound;
    otherwise, return "unknown compound".

    Parameters:
        formula (str): A string that contains a chemical formula.
        known_molecules_dict (dict): A dictionary that contains known
            chemical formulas and their names.

    Returns:
        str: The name of a chemical formula if found, otherwise "unknown compound".
    """
    if formula in known_molecules_dict:
        return known_molecules_dict[formula]
    else:
        return "unknown compound"


def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in the elements
    listed in the symbol_quantity_list.

    Parameters:
        symbol_quantity_list (list): A list of lists, where each inner list
            contains the chemical symbol and quantity of an element.
        periodic_table_dict (dict): A dictionary containing the periodic table
            information.

    Returns:
        int: The total number of protons in the given elements.
    """
    total_protons = 0

    for element in symbol_quantity_list:
        symbol = element[0]
        quantity = element[1]
        # Accessing atomic number from periodic table
        atomic_number = periodic_table_dict[symbol][1]
        total_protons += atomic_number * quantity 

    return total_protons


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1



def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    """
    total_molar_mass = 0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity

    return total_molar_mass


def compute_percent_composition(formula, periodic_table_dict):
    # Function to compute the percent composition of a chemical compound
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)  # Parse the formula and obtain a list of symbols and quantities
    total_molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)  # Compute the total molar mass of the compound

    percent_composition = {}  # Create an empty dictionary to store the percent composition

    for element in symbol_quantity_list:
        symbol = element[0]  # Get the symbol of the element
        quantity = element[1]  # Get the quantity of the element in the compound
        atomic_mass = periodic_table_dict[symbol][1]  # Get the atomic mass of the element from the periodic table dictionary

        percent = (atomic_mass * quantity) / total_molar_mass * 100  # Calculate the percent composition of the element
        percent_composition[symbol] = percent  # Store the percent composition in the dictionary

    return percent_composition  # Return the percent composition dictionary



def main():
    # Dictionary of known molecules and their names
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    # Creation of the periodic table
    periodic_table = make_periodic_table()

    # Prompt the user to enter the molecular formula of the sample
    chemical_formula = input("Enter the molecular formula of the sample: ").upper()

    # Prompt the user to enter the mass in grams of the sample
    sample_mass = float(input("Enter the mass in grams of the sample: "))

    # Parse the chemical formula and obtain a list of symbols and quantities
    symbol_quantity_list = parse_formula(chemical_formula, periodic_table)

    # Compute the molar mass of the sample using the symbol-quantity list
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Calculate the number of moles in the sample by dividing the sample mass by the molar mass
    number_of_moles = sample_mass / molar_mass
    


    # Get the name of the chemical compound using the known molecules dictionary
    compound_name = get_formula_name(chemical_formula, known_molecules_dict)

    # Calculate the total number of protons in the sample using the symbol-quantity list
    total_protons = sum_protons(symbol_quantity_list, periodic_table)

    # Calculate the percent composition of the chemical compound
    percent_composition = compute_percent_composition(chemical_formula, periodic_table)

    # Print the obtained results
    print(f"The molar mass of the molecule is: {molar_mass} grams/mol")
    print(f"The number of moles in the sample is: {number_of_moles:.5f} moles")
    print(f"The compound name is: {compound_name.upper()}")
    print(f"The total number of protons is: {total_protons}")
    print("Composition:")
    for symbol, percent in percent_composition.items():
        print(f"{symbol}: {percent:.2f}%")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()




