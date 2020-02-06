"""
Program: CS 115 Project 1
Author: Lucien Duran-Luthi
Description: This program models out the population of rabbits and foxes throughout a specified time scale using user inputed data values
"""

def main():
    import math
    print('==> Rabbits and Foxes Population Simulator <==')
    print('')
    print('--- Model Parameters ---')
    rbirth = float(input('Rabbits birth rate: '))
    rdeath = float(input('Rabbits death rate: '))
    fbirth = float(input('Foxes birth rate: '))
    fdeath = float(input('Foxes death rate: '))
    print('\n--- Inital Population ---')
    numr = float(input('Number of rabbits (in thousands) at t = 0: ')) #rabbit pop
    numf = float(input('Number of foxes(in thousands) at t = 0: ')) # fox pop
    time = int(input('Timescale:'))
    print('')

    min_rabbit = 10000000000000000000000000000000
    max_fox = - 1
    year_max_f = 0
    fox_year_num = -1
    rabbit_year_num = -1 #r_year_counter
    pop_rabbit = numr
    totalR = 0
    totalF = 0


    if time <= 0:
        # By enclosing the lowr portion of the code into an if loop one can easily route out a negative time scale
        print("Error: cannot have a negative timescale")
    else:
        for i in range(time + 1):
            fox_year_num = fox_year_num + 1
            rabbit_year_num = rabbit_year_num + 1
            if numr <= 0:
                numr = 0 #this portion over here helps set the values to prevent errors when one adds in a negative value, instead setting the value, if negative, to zero
            if numf <= 0:
                numf = 0

            print('Time t = ', str(i), ': ', (round(numr, 3)), 'k rabbits, ', (round(numf, 3)),'k foxes', sep='')

            if numr < min_rabbit:
                min_rabbit = numr
                year_min_r = rabbit_year_num

            if numf > max_fox:
                max_fox = numf
                year_max_f = fox_year_num
            tmpr = round(numr, 3)
            tmpf = round(numf, 3)
            numf = round(numf + (fbirth * numf * numr) - (fdeath * numf), 3)
            numr = round(numr + (rbirth * numr) - (rdeath * numr * tmpf), 3)
            totalR = totalR + tmpr
            totalF = totalF + tmpf

            print("")
            print('--- Simulation Statistics ---')
            print('Average rabbit population: ', round(totalR/(time + 1), 3), "k", sep="") #though a bit complicated and dangerous the only way to correctly spit out the code in this instance was to round it at the end, as well as some last minute calculations
            print('Average fox population: ', round(totalF/(time + 1), 3), 'k', sep="")
            print('Min rabbit population was ', min_rabbit, 'k at t=', year_min_r, sep="")
            print('Max fox population was ', max_fox, "k at t=", year_max_f, sep="")
main()