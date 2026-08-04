global_variable = "I'm outside the function"

def my_function():
    print(global_variable)

my_function()
print(global_variable)

global_variable = "I'm outside the function"

def my_function():
    print(global_variable)

my_function()(global_variable)