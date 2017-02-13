name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old. %s is old." % (name, age, name))

mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s. Your current balance is $%s." % (data[0],data[1],data[2]))