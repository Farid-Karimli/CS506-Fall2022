def draw_power_plant():
    print("CS506 Power Plant")
    print("----------------")
    for x in range(10):
       
        print("|", end="")
        if x==0:
            print(" POWER PLANT", end=" ")
        else:
            print("             ", end="")
        print("|")
    return
draw_power_plant()