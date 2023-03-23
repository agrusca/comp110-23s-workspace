#list syntax
grocery_list: list[str] = ["eggs", "milk", "bread"]

#initializing empty list
grocery_list: list[str] = list()

#adding an item to a list
grocery_list.append("bananas")

#indexing 
grocery_list[0]

#modifying by index
grocery_list[1] = "eggs"

#length of a list
len(grocery_list)

#remove item from a list
grocery_list.pop(2)

#importing a module
from lessons import functions
    #from <package name> import <module name>

#importing a function
from lessons.functions import randint

#using an import
functions.randint(1,7)
    #function: <module name>.<function name>(arguments)
    #variable: <module name>.<variable name>

#having something only run in main function
if __name__== "__main__":
    main()

#making a local variable global
lauren: str = "a friend"
def a_forceful_stranger() -> None:
    global lauren
    lauren = "my horse"

#using for loops
grocery_list: list[str] = ["bananas", "apples"]
for item in grocery_list:
    print(item)

#sequences
    #str is a sequence of character data
    #list is a dynamically sized sequence of values of a specific type
    #tuple is a fixed size sequence of values of any types
    #range is a sequence of integers at intervals between a start and end

#tuple
coordinate: tuple[float, float, float] = (1.0, 1.0, 1.0)
    #parentheses help python recognize its not a list
Player: tuple[str, int]
lebron: Player = ("James", 6)
mj: Player = ("Jordan", 23)
    #store in heap

#range
range(1, 10, 3)
    #range from 1 to 10 with steps of 3
    #if step is not included python assumes step of 1
    #don't include end point 
    #store in heap

#using a range in a for... in... loop
names: list[str]= ["alyssa", "jannet", "vrinda"]
for idx in range(0,len(names)):
    #end of range = len of list because last idx not included 
    print(f"{idx}: {names[idx]}")

#dictionaries
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
    #can also use single quotes 
empty_dict: dict[str, int] = dict() 
another_empty_dict: dict[int, int] = {}

#adding elements to dictionary
ice_cream["chocolate"] = 12 

#removing items from dictionary
ice_cream.pop("chocolate") 

#accessing values from dictionary
print(f"Number of vanilla orders: {ice_cream['vanilla']}")
    #need single quotes when using f string

#modyfing values from dictionary
ice_cream["vanilla"] = 9 
ice_cream["vanilla"] += 1

#length of a dictionary
len(ice_cream)

#check if key in dictionary
"mint" in ice_cream
    #returns true if key exists in dictionary and false otherwise 
    #can't have duplicates of keys but can have duplicates of values 

#dictionary in for loops
grades: dict[str, str] = {"Alyssa": "A", "Aksana": "A", "Regis": "B"}
for student in grades:
    print(grades[student])
    #student refers to keys and output refers to associated values