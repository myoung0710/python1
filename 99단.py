Line = ""

for i in range(2,10,1):
    print("#   ", i, "    # ", end="")
print("")

for j in range(1, 10, 1):
    for k in range(2, 10 , 1):
        print("|", k, "*", j, "=", k*j, "", end="")
    print("")