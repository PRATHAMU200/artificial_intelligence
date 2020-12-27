for row in range(1,8):
    for col in range(1,6):
        if col==3 or (row==1 and col!=3) or (row==7 and col<3):
            print("*",end="")
        else:
            print(end=" ")
    print()
