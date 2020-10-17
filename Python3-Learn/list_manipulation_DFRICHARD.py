// AUTHOR: Richard
// Python3 Concept: Manipulating data in lists
// GITHUB: https://github.com/DFRICHARD

//Add your python3 concept below

domestic_animals = [] #creating an empty list to contain domestic animals
domestic_animals.append("dog") #adding dog to the list domestic_animals
print(domestic_animals) # The result: ["dog"]
domestic_animals.append("cat")
print(domestic_animals) #The result: ["dog", "cat"]

wild_animals = ["lion", "elephant", "tiger" , "leopard"]

animals = domestic_animals + wild_animals #Joining lists
print(animals) #The result : ["dog", "cat", "lion", "elephant", "tiger", "leopard"]

print(animals[0]) #printing the first item of the list of animals : dog
print(animals[2:5]) #printing the third to fifth item of the list of animals
print(len(animals)) #printing the number of items in the list of animals
animals[3] = "pen" #replacing the fourth item(elephant) with "pen" 
print(animals)  # the result: ["dog", "cat", "lion", "pen", "tiger", "leopard"]
animals.remove("pen") #removing pen from the list of animals
print(animals)  # the result: ["dog", "cat", "lion", "tiger", "leopard"]
