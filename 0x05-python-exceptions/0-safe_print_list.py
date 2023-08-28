#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0;
    
    """input a range as the index then try-catches the results"""
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="");
            count += 1;
        except IndexError:
            break;
    print("")
    return (count);
