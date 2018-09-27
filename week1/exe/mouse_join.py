# String list joining problem

###################################################
# Student should enter code below

def string_list_join(vec):
    res = ""
    for word in vec:
        res += word
    return res

###################################################
# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd
