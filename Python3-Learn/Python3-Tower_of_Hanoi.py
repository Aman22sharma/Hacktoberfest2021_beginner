def tower_of_hanoi(n, source, destination, auxiliary):
    if(n==1):
        print("Move disc 1 from source", source, "from to destination", destination)
    else: 
        tower_of_hanoi(n-1, source, auxiliary, destination)
        print("Move disc", n, "from source", source,"from to destination", destination)
        tower_of_hanoi(n-1, auxiliary, destination, source)

n_disks=int(input("Please enter the number of disks\n"))

tower_of_hanoi(n_disks, "A", "C", "B")
