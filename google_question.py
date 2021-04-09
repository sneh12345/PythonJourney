test_list = [2, 421493803948032967598756984579684756]
print("The Original list:", test_list)
res = [
    ele for ele in range(
        max(test_list) + 1
    )
    if ele not in test_list
]
print("The missing numbers are:", res)