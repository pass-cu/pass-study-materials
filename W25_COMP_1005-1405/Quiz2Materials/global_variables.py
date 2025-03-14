var_1 = 1	# global variable
var_2 = 2	# global constant
var_3 = 3	# global constant
var_4 = 4   # global constant

def eggs(y):
    return y + 10

def spam(x):
    var_1 = 1
    global var_2
    var_1 += 1
    return var_1 + var_2 

def foo():
    global var_4
    var_4 + spam(var_3)
    return var_4

def main():
    print(foo() + var_3)

main()
