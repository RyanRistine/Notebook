def main ():

    print("==> Rabbits and Foxes Populations Simulator <==\n\n--- Model Parameters ---")

    a = float(input("Rabbits birth rate: "))
    b = float(input("Rabbits death rate: "))
    c = float(input("Foxes birth rate: "))
    d = float(input("Foxes death rate: "))

    print("\n--- Initial Population ---")

    Rabbits_t = float(input("Number of rabbits (in thousands) at t=0: "))
    Foxes_t = float(input("Number of foxes (in thousands) at t=0: "))
    time_scale = int(input("Timescale: "))

    average_foxes = float(0)
    average_rabbits = float(0)


    min_rabbit = Rabbits_t
    if Rabbits_t < 0:
        min_rabbit = float(0)
    max_fox = Foxes_t

    Y = 0
    X = 0

    if time_scale > 0:


        for i in range (time_scale + 1):

            if (Rabbits_t < 0):
                Rabbits_t = 0.0
            if (Foxes_t < 0):
                Foxes_t = 0.0

            print("Time t= ",i, ': ', Rabbits_t, 'k rabbits,', ' ', Foxes_t, 'k foxes',sep='')

            average_foxes += Foxes_t
            average_rabbits += Rabbits_t

            Rabbits_t1 = round(Rabbits_t + (a * Rabbits_t) - (b * Rabbits_t * Foxes_t), 3)
            Foxes_t1 = round(Foxes_t + (c * Foxes_t * Rabbits_t) - (d * Foxes_t), 3)

            Rabbits_t = Rabbits_t1
            Foxes_t = Foxes_t1

            if time_scale != i:
            #if i < time_scale:

                if Rabbits_t < min_rabbit:
                    min_rabbit = Rabbits_t
                    X = i + 1

                if Rabbits_t < 0:
                    min_rabbit = float(0)

                if Foxes_t > max_fox:
                    max_fox = Foxes_t
                    Y = i + 1

        print("\n --- Simulation Statistics--- ")
        # calc average

        num_rabbits = average_rabbits / (time_scale + 1)
        num_foxes = average_foxes/(time_scale + 1)

        print("Average rabbit population: ", round(num_rabbits,3), "k", sep='') # print rounded number
        print('Average fox population: ', round(num_foxes,3), "k", sep='')
        print("Min rabbit population was ", round(min_rabbit,3), "k at t=", X, sep='')
        print("Max fox population was ", round(max_fox,3), "k at t=",Y, sep= '')
    else:
        print("Error: cannot have a negative timescale")

main()
