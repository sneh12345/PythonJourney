test_list = [2, 3, 6, 7, 8, 9 ,10]
print("The Original list:", test_list)
res = [
    ele for ele in range(
        max(test_list) + 1
    )
    if ele not in test_list
]
print("The missing numbers are:", res)