def draw_museum():
    
    print(" ==================")
    for x in range(10):
        print("||", end="")
        if x==0:
            print(" MUSEUM OF ARTS ", end="")
        else:
            print("                ", end="")
        print("||")
        
    return
draw_museum()