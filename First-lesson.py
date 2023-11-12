#class = str   :string
name = "bro"
print (name)
#We just gave a value to the element: "name", this we call a string
#If you use name it will always use that value automatically
print ("hello" + name)
print ("hello " + name)
#use a space between the word you want to write and the value you gave something, within the double marks!
print(type(name))
#This way you can check wich type of vaiable you are using, at this moment it's a "string"
First_name = "Siep"
Last_name = "Pieters"
full_name = First_name +" "+ Last_name
#It is not obliged to use a "_underscore" to make a space, but this is common python.
print ("fakka " + First_name + " " + Last_name)
print ("fakka " + full_name)
#see the differ?

#class = int   :integer
age = 19
#Do not put integers like this between "" Because then you create a string and not a variable
age = age + 1
print(age)
#shortcut:
age += 1
print(age)
print(type(age))
#if we would have used "" then it would have become a string. With strings you can not do calculations or any type of math
print("My age is: "+str(age))
#You cannot mix a string type text like "my age is: " with a variable. That's wy we need to adapt to a string!
print("Hello " +full_name + ", your age is: "+str(age))

#class = float    :a decimal number
height = 65.6754
print(height)
print(type(height))
print("your height is: "+str(height)+"cm")

#class = bool     :true or false :boolean
kak = False
print(kak)
print(type(kak))
print("Are you kak?: "+str(kak))
#this is really usefull with "if_statements"

