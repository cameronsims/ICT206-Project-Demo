# display.py - Functions relating to displaying to user
#
# Author: Cameron Sims
# Date: 14/08/2024
#

# Console Imports
import colorama as clr  # Used for colouring the console

def default_colour():
    print(clr.Fore.WHITE + clr.Back.BLACK)

def print_signature():
    print(clr.Fore.WHITE + clr.Back.BLUE + "+---------------------------------------+")
    print("|                                       |")
    print("| ICT206 - Intelligent Systems: Project |")
    print("|        Cameron Sims (34829454)        |")
    print("|                                       |")
    print("+---------------------------------------+")
    default_colour()
    
def print_error(str):
    print(clr.Fore.WHITE + clr.Back.RED + "! ERROR: " + str)
    default_colour()
    
def print_connection_begin():
    print("+ Reading Connections...")
    
def print_connection_end():
    print("- Connections Read!")

def print_pyvis_begin():
    print("+ Creating Python Graph:")
    
def print_pyvis_end():    
    print("- Python Graph Has Concluded!")
    
def print_hours(hours): 
    print("There are " + str(hours) + " hours left!")