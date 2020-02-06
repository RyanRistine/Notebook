"""
Program: CS 115 Project 1
Author: Ryan Ristine
Description: A Simulation of rabbit and fox populations based on user input, statistics about the
             simulation are also generated and printed after the simulation is run.
"""

import math

def main():
    # collects parameteres of the simulation
    print("==> Rabbits and Foxes Population Simulator <== \n \n--- Model Parameters ---")
    rBr = float(input("Rabbits birth rate: "))
    rDr = float(input("Rabbits death rate: "))
    fBr = float(input("Foxes birth rate: "))
    fDr = float(input("Foxes death rate: "))
    print("\n--- Initial Population ---")
    r = float(input("Number of rabbits (in thousands) at t = 0: "))
    f = float(input("Number of foxes (in thousands) at t = 0: "))
    tS = int(input("Timescale: "))
    if (tS < 0):
        print("Error: cannot have a negative timescale")
        exit(-1)
    if (r < 0):
        r = float(0)
    if (f < 0):
        f = float(0)
    rT = []
    fT = []
    # does the calculations
    for i in range(tS + 1):
        rT.append(r)
        fT.append(f)
        rbirths = rBr * r
        fbirths = fBr * f * r
        rdeaths = rDr * r * f
        fdeaths = fDr * f
        # prints then redefines the number of rabbits and foxes
        print("\nTime t = ", i, ": ", round(r, 3), "k rabbits, ", round(f, 3), "k foxes", sep="")
        r = round(r + rbirths - rdeaths, 3)
        f = round(f + fbirths - fdeaths, 3)
        if (r < 0):
            r = float(0)
        if (f < 0):
            f = float(0)
    # Calculates the simulation statistics
    rA = sum(rT) / len(rT)
    fA = sum(fT) / len(fT)
    rMin = min(rT)
    rMax = max(rT)
    fMin = min(fT)
    fMax = max(fT)
    rMinPos = rT.index(min(rT))
    rMaxPos = rT.index(max(rT))
    fMinPos = fT.index(min(fT))
    fMaxPos = fT.index(max(fT))
    # prints the simulation statistics
    print("\n--- Simulation Statistics ---")
    print("Average rabbit population: ", round(rA, 3), "k", sep="")
    print("Average fox population: ", round(fA, 3), "k", sep="")
    print("Min rabbit population was ", round(rMin, 3), "k", " at t=", rMinPos, sep="" )
    print("Max fox population was ", round(fMax, 3), "k", " at t=", fMaxPos, sep="" )
main()
