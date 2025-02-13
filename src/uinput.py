# file.py - Reads Road File(s) and Prints Results
#
# Author: Cameron Sims
# Date: 14/08/2024
#

def get_uint(str, errf):
    driver_n = -1
    while driver_n < 1:
        try:
            driver_n = int(input(str))
        except:
            driver_n = -1
        if (driver_n < 1):
            errf("Non-Positive Number")
    return driver_n

def get_driver_amount(errf): 
    return get_uint("Input the amount of drivers (recommended between 50<=n<=500): ", errf)
    
def get_sim_time(errf): 
    return get_uint("Input the amount of months of the simulation (ticks are every hour): ", errf)