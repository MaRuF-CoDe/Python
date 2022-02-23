programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again."
}

# Retrive a dictionary
# print(programming_dictionary)

# Adding new item in dictionary
programming_dictionary["loop"] = "A never ending process without condition"

# Find a specific item in dictionary
# print(programming_dictionary["Bug"])

# Wipe out a dictionary
# programming_dictionary={}
# print(programming_dictionary)

# Change in dictionary
programming_dictionary["Bug"] = "A month in your PC"
# print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])