
def check_list(string_to_check):            #pass string for checking
    list_to_check = []
    for i in string_to_check:               #Convert string to nice easy to use list
        list_to_check.append(i)
    remove_first(list_to_check)


def remove_first(list_to_check):
    try:
        item_to_check = list_to_check[0]        #Get first item in list
    except IndexError:
        print("No unique items in string!")
        return
    list_to_check.pop(0)                    #Remove first item
    item_removed = False
    for i in list_to_check:                 #Check every character in list
        if i == item_to_check:
            list_to_check.remove(i)
            item_removed = True
    if item_removed == True:                #If we removed a character go again!
        remove_first(list_to_check)
    else:
        print(item_to_check, "Is unique!")


check_list(input("Input string to be tested: "))        #Get user input and check list
