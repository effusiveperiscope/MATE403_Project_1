#!/usr/bin/env python

# Calculates quantized energy levels for a particle in a cubic 3D infinite
# potential well of arbitrary side length up to a given wavenumber.

# Imports
from itertools import combinations_with_replacement 
from collections import Counter

# Python 2/Python 3 compatibility - renames input function
try:
    input = raw_input
except NameError:
    pass

# Constants
h = 6.62607004e-34 # Planck constant, J*s
m = 9.1094e-31 # Mass of particle, kg
MAX_WAVENUMBER = 6 # Maximum wavenumber

# Header/User input with validation
print("This program calculates quantized energy levels for a particle in a "
    "cubic 3D infinite potential well.")
print("Please enter all decimals in e-notation (e.g. 1*10^9 ==> 1e9).") 

# Function for grabbing and validating numerical input 
def grab_number(prompt, min_bound=0, max_bound=None):
    while True: # Re-prompt if error encountered
        try: ret = float(input(prompt))
        except ValueError as err: # Ensure user input is a number
            print("Error: "+str(err))
            continue
        if ret <= min_bound: # Respect minimum bound
            print("Error: must be greater than "+str(min_bound)+".")
        elif (max_bound != None) and (ret > max_bound): # Respect maximum bound
            print("Error: must be less than "+str(max_bound)+".")
        else:
            return ret

# Grab user input (size of quantum well, particle mass, upper wavenumber)
L = grab_number("Enter the size of the quantum well (m): ")
m = grab_number("Enter the effective mass of the particle (kg): ")
n = int(grab_number("Enter the upper wavenumber limit (must be an"
    " integer between 1 and "+str(MAX_WAVENUMBER)+"): ",0))

# Takes a 3-tuple of wavenumbers and calculates the energy
def energy(wavenumbers):
    return h**2/(8*m)*(
        wavenumbers[0]**2+wavenumbers[1]**2+wavenumbers[2]**2)/L**2
    pass

# Takes a 3-tuple of wavenumbers and outputs the degree of degeneracy 
def degeneracy(wavenumbers):
    uniq = len(Counter(wavenumbers).keys()) # Number of unique numbers 
    if uniq == 1: return uniq
    elif uniq == 2: return 3
    elif uniq == 3: return 6

output = [] # List containing output tuples (wavenumbers, energy, degeneracy)

# Iterate through all possible combinations of wavenumbers up to (n,n,n)
for wavenumbers in list(combinations_with_replacement(range(1,n+1),3)):
    # Append a tuple: (wavenumbers, energy, degree of degeneracy)
    output.append((wavenumbers, energy(wavenumbers), degeneracy(wavenumbers)))

# Sort by energy level
output.sort(key=(lambda x: x[1]))

# Printing
print("\twavenumbers\tenergy (J)\tdegeneracy") # Display column titles
for tup in output: # Iterate through output tuples
    print("\t{nx} {ny} {nz}\t\t{en:.5}\t{deg}".format(nx=tup[0][0],
        ny=tup[0][1], nz=tup[0][2], en=tup[1], deg=tup[2])) # Display data
input("Press any key to exit.")

# References:
# Particle in a 3-Dimensional box https://chem.libretexts.org/@go/page/1726
# (accessed Apr 24, 2021).