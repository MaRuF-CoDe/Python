# from turtle import Turtle, Screen

# timmy = Turtle()#create a new object from a blueprint/class
# timmy.shape("turtle")#we can call methods that are associated with the object
# timmy.color("blue")#we can call methods that are associated with the object
# timmy.forward(100)#we can call methods that are associated with the object


# my_screen = Screen() #create a new object from a blueprint/class
# print(my_screen.canvheight) #tap into attribute by using obeject dot(.) name of the atrribute
# my_screen.exitonclick() #we can call methods that are associated with the object

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name",
["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])
table.align = "l"
print(table)