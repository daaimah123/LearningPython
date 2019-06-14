
#create for and while loop that creates the following:
# 😀
# 😀😀
# 😀😀😀
# 😀😀😀😀
# 😀😀😀😀😀
# 😀😀😀😀😀😀
# 😀😀😀😀😀😀😀
# 😀😀😀😀😀😀😀😀 #8 times


# for num in range(1, 9):
#     print('\U0001f600' * num)

num = 1
while num <= 8:
    print ('\U0001f600' * num)
    num+=1