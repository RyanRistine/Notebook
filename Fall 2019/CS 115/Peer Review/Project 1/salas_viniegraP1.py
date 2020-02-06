# rtThe number of prey (rabbits) at time t.
# ftThe number of predators (foxes) at time t.
# aThe birth rate of rabbits.
# bThe death rate of rabbits (depends on predator population).
# cThe birth rate of foxes (depends on prey population).
# dThe death rate of foxes.
"Author: Eleazar Salas Viniegra"
"CS 115 - 19 - FA"
"Project 1"
"This is a calculator that determines the population size of foxes and rabbits who " \
 "live within a certain area of land"


def main():
    print("==> Rabbits and Foxes Population Simulator <==")
    print()
    print("--- Model Parameters ---")
    a = float(input("Rabbits birth rate: "))
    b = float(input("Rabbits death rate: "))
    c = float(input("Foxes birth rate: "))
    d = float(input("Foxes death rate: "))
    print()
    print("--- Initial Population ---")
    rt = float(input("Number of rabbits (in thousands) at t = 0: "))
    if rt < 0:
        rt = 0.0  # If The user inputs a value below zero, it will simply make the user's value zero.
    ft = float(input("Number of Foxes (in thousands) at t = 0: "))
    if ft < 0:
        ft = 0.0  # If The user inputs a value below zero, it will simply make the user's value zero.
    time_scale = int(input("Timescale: "))
    if time_scale < 0:
        time_scale = 0.0
        print("Error: cannot have a negative timescale")
        exit(-1)
    # Set the populations to the correct category.
    avg_r_pop = rt
    avg_f_pop = ft
    # Same Concept with the quote above ^. We will be using these variables further down the function.
    min_r_pop = rt
    max_f_pop = ft
    r_zero = 0
    f_zero = 0
    print()
    print("Time t = 0: ", round(rt, 3), "k rabbits", ",", " ", round(ft, 3), "k foxes", sep="")
    for j in range(time_scale):
        r_time = rt
        rt = round(rt + a * rt - b * rt * ft, 3)
        ft = round(ft + c * ft * r_time - d * ft, 3)
        if rt < 0:
            rt = 0.0  # If The user inputs a value below zero, it will simply make the user's value zero.
        if ft < 0:
            ft = 0.0  # If The user inputs a value below zero, it will simply make the user's value zero.
        avg_f_pop = ft + avg_f_pop
        avg_r_pop = rt + avg_r_pop
        if rt < min_r_pop:
            min_r_pop = rt
            r_zero = j + 1
        if ft > max_f_pop:
            max_f_pop = ft
            f_zero = j + 1
        print("Time t = ", j + 1, ":", " ", round(rt, 3), "k rabbits,", " ", round(ft, 3), "k foxes", sep="")
    avg_r_pop = round((avg_r_pop / (time_scale + 1)), 3)
    avg_f_pop = round((avg_f_pop / (time_scale + 1)), 3)
    print()
    print("--- Simulation Statistics ---")
    print("Average rabbit population: ", avg_r_pop, "k", sep="")
    print("Average fox population: ", avg_f_pop, "K", sep="")
    print("Min rabbit population was ", min_r_pop, "k at t=", r_zero, sep="")
    print("Max fox population was ", max_f_pop, "k at t=", f_zero, sep="")


main()
