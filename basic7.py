# values = [1,5,8,3]
# if 3 in values:
#     print("3 is present")
# else:
#     print("3 is absent")
# if -1 in values:
#     print("-1 is present")
# else:
#     print("-1 is not present")

def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True 
    return False
print(is_group_member([1,5,8,3],3))
print(is_group_member([1,5,8,3],-1))
