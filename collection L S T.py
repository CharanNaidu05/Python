#collection = single "variable" used to store mültiple values

# List = [] ordered and changeable. Duplicates OK

# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#LIST
fruits = ["apple", "orange", "bananna", "coconut"]

#1print(fruits[::-2]) 
#for x in fruits:
 #   print(x)

#2for fruit in fruits:
 #   print(fruit)

#3print(len(fruits))
#print("apple" in fruits)

#4fruits[1] = "pineapple"
#for fruit in fruits:
#    print(fruit)

#5fruits.append("pineapple")
#print(fruits)

#6fruits.remove("apple")
#print(fruits)

#7fruits.insert(3, "pineapple")
#print(fruits)

#8fruits.sort()
#print(fruits)

#9fruits.reverse()
#print(fruits)

#10fruits.clear()
#print(fruits)

#11print(fruits.index("bananna"))
#print(fruits)

#12print(fruits.count("bananna"))
#print(fruits)

##SET

fruits = {"apple", "orange", "bananna", "coconut"}
#print(fruits)

#1fruits.add("pineapple")
#print(fruits)

#2fruits.remove("apple")
#print(fruits)

#3fruits.pop()
#print(fruits)

#4fruits.clear()
#print(fruits)

#5fruits = {"apple", "orange", "bananna", "coconut", "coconut"} #sets cannot contain duplicate
#print(fruits)

###TUPLE

fruits = ("apple", "orange", "bananna", "coconut", "coconut")
 
#1print(fruits.index("apple"))
#print(fruits)

#2print(fruits.count("coconut"))
#print(fruits)

#3print(fruits.index("bananna"))
#for fruit in fruits:
#    print(fruits)

#4for fruit in fruits: ##it wont repeat 5 times in output cuz of break
#    print(fruits)
#    break