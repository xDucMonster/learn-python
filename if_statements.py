
is_male = True
is_tall = True
#          or
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are a tall female")
else:
    print("You aren't male and tall")


