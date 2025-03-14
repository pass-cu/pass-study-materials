# This is an example of copying lists.
# When copying lists as seen in the first line of the main function
# we must use the [:]. Try removing [:] and compare the output to when
# it is still there.

old_list = [2, 5, 3, 4]

def edit(new_list):
    new_list.append(5)
    return new_list

def main():   
    new_list = edit(old_list[:])
    print(old_list)
    print(new_list)

# COPY : old_list[:]

main()

# THUS -> When copying lists:
old_list = [1, 2, 3]
new_list = old_list # WRONG
new_list = old_list[:] # CORRECT