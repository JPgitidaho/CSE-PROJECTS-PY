''' CSE 111 - Prove Activity - Week 5-6 Juanita P. Aguilera 
Exceeded Requirements
Included:
1. Program includes and uses constants for Earth's acceleration of gravity, 
water density, and water dynamic viscosity 
2. Program includes a function that converts kilopascals to pounds per square inch 
3. Test file includes a test function that verifies that the kPa to psi conversion function works correctly 
4. Program includes some other additional functionality: functionality to calculate the time required to 
fill a water tank. Call it multiple times in my test function to rigorously test its functionality.'''

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

# Formulas

def water_column_height(tower_height, tank_height):
    height = tower_height + (3 * tank_height / 4)
    return height


def pressure_gain_from_water_height(height):
    density_water = 998.2
    g = 9.80665
    P = (density_water * g * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2  # in kg/m^3
    P = -(friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return P


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2  #  in kg/m^3
    pressure_loss = (-0.04 * density_water * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss




def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates the Reynolds number for water flowing through a pipe.
    """
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates the water pressure lost due to pipe diameter reduction.
    """
    k = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)
    P = -k * WATER_DENSITY * (fluid_velocity**2) / 2000
    return P


def kPa_to_psi(pressure):
    psi = pressure * 0.145038
    return psi


def calculate_filling_time(flow_rate, tank_volume):
    time = tank_volume / flow_rate
    return time



PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters) 11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65  # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters) 1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)



def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    tank_volume = float(input("Tank volume (cubic meters): "))
    
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_psi = kPa_to_psi(pressure)
    filling_time = calculate_filling_time(velocity, tank_volume)
    
    
    

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
    print(f"Pressure at house: {pressure_psi:.1f} pounds per square inch")

    print(f"Filling time for the tank: {filling_time:.2f} seconds")


if __name__ == "__main__":
    main()





