# int float str 
# list ([10,"hello",200.3])
#  dict (Dictionary Unordered Key-value pairs Key:Value )
#  tup (Tuples, ordered mutable lists) 
#  sets (set)  bool


#Basic Maths
a = 2+1
b = 2-1
c = 2*2
d = 2/2
f = 7%4 # Modulo
g = 3**8 # To the power of

#print(a*b+((c-d)*(f+g))/g)  # Order of operations

#Variable Assingment

a1 = 10

a1 += a1*2 #Variable Reassignment
print(a1)
print(type(a1)) #type function will return data type of variable

# Strings

#escape sequences \n newline \t tab 

#Indexing[] and slicing Indexing grabs a single character from the string,
#Index starts at 0, can use reverse indexing -1 is last

#Slicing[start(numerical index for slice start)
#:stop(index to go up to but not include)
#:step(size of the jump you take)]
# allows you to grab a subsection 

stringExample = "I'm an old dog" #use double quotes on outside when using apostrophe
print(stringExample)


print(len(stringExample)) #length function for str is len

#Indexing Example

sliceExample1 = stringExample[0] # grabbing the first character
sliceExample2 = stringExample[-1] # grabbing the last character

print(sliceExample1 + " " + sliceExample2)

#Slicing Example
stringExample2 = "Abdcejksldkjdksljsklj"

stringExample2[2:] #Grab everything from index 2
stringExample2[:3] #Go up to position 4 but don't include it
stringExample2[3:6] #From here to there but not including
stringExample2[::] #All the way from the beginning to the end
stringExample2[::2] #Grab in jumps of 2, skip a letter
print(stringExample2[2:12:3]) #Grabs with step size

#String Properties and Methods

#String index changes strings are immutable so you can not change them directly

name = "Sam"
last_letters = name[1:] #taking just the am
print("P" + last_letters) 

stringExample3 = "Hello World"


#String functions examples

upperStringExample3 = stringExample3.upper() #uppercase Evertyhing
splitStringExample3 = stringExample3.split() #Splits everything in the string to a list

#Print formatting for strings


#.format()

print("This is a string {}".format("Inserted")) #Adds an inserted string where the {} are
print("The {2} {0} {1}".format("cat","mouse","ferret")) #Same thing done by list index

#Same thing but calling from variables created inside the .format function
print("The {printVar1} {printVar2} {printVar3}".format(printVar1 = "Ferret",printVar2 = "Cat", printVar3 = "Mouse"))

#Float Formatting "{value:width.precision f}"
result1 = 100/777 #creates a value with a lot of decimals
print("The result was {r1:1.3f}".format(r1 = result1)) #rounds your number based upon your .precision


#f-strings (Formatted string literals)
stringNameExample = "John"
print(f"Hello, his name is {stringNameExample}") #the f in front of the string allows for unformatted compilation




#Lists Ordered sequenced objects [a,b,c] Lists are mutable
my_list1 = [1,2,3]
my_list2 = ["String",100,23.2] #lists can be different kinds of objects
print(len(my_list2)) #lists can show how many items are contained

my_list3 = ["One","two","three"]
my_adjustedList1 = my_list3[1:] #Functions like slicing work on lists as well.  T
print(my_adjustedList1)

combined_list1 = my_adjustedList1 + (my_list2 * 3) #combinings lists
print(combined_list1)

combined_list1[0] = "destructo!" #Mutating our list based on index position
print(combined_list1)

combined_list1.append("Six!") #Adds a new element to the end of your list
print(combined_list1)

combined_list1.pop() #Takes the last Item off the list
print(combined_list1)

popped_item1 = combined_list1.pop() #You can take the last item off an ordered list and store it somewhere
print(combined_list1)
print(popped_item1)

combined_list1.pop(1)  #Popping items off list from index position
print(combined_list1)

letter_list1 = ["a","q","f","m","t"]
num_list1 = [10,22,33,4,208]

letter_list1.sort() #Sort new list
print(letter_list1) #sorted alphabetically

num_list1.sort() #numerically sorted
print(num_list1)


num_list1.reverse() #reverses numbers
print(num_list1)



#Dictionaries unordered mappings Key-Value Pair no need for indexing, can not be sorted though
#{key1:"vaule1",key2:"value2",key3:"value3"}

my_dict1 = {"playerName": "Tom","age": 27}
print(my_dict1)
print(my_dict1["playerName"]) #Key value relationship will return tom

prices_lookup = {"apple" : 0.77, "orange": 0.45, "lemon": 0.82}
print(prices_lookup["orange"]) #looking up the price of an orange using our key value

my_imbedded_list1 = {"z1":123, "k2":[0,1,4,33,2], "k3":{"z2":"catfood","z3":333}} #imbedded lists
print(my_imbedded_list1["k3"]["z3"]) #Accessing imbedded data stacking call

my_imbedded_list1["k4"] = 44 #Adding a new key pair to dictionariy
print(my_imbedded_list1["k4"])

my_imbedded_list1["k4"] = 22 #updating key value data
print(my_imbedded_list1["k4"])

print(my_imbedded_list1.keys()) #returns all of the available keys
print(my_imbedded_list1.values()) #returns all values
print(my_imbedded_list1.items())  #returns both



#Tuples  lists but they are immutable and can not be changed.  

my_tup1 = (1,2,3,"sad",1,1,1)
my_list4 = [1,2,3,"happy"]

print(my_tup1[0]) # just like lists you can print ordered indexted objects

print(my_tup1.count(1))  #method to count how many times something appears in the tuple

print(my_tup1.index("sad")) #returns the index of the first time the object appears in the tuple

#Sets unordered collections of unique elements ie nothing can repeat

#adding items one at a time not a great way to use a set
my_set1 = set() 
my_set1.add(1)
print(my_set1)
my_set1.add("happy") 
print(my_set1)

#better to have a list and set it 
my_list5 = my_list1 + my_list2
my_set2 = set(my_list5)
print(my_set2)



#booleans
num1 = 10

while(num1 > 1):
    if(num1 > 4):
        print(my_list5)
        my_list5.pop()
    else:
        print(num1)
    num1 = num1 - 1

im_true = True
im_false = False
print(type(im_true)) #returns bool type





