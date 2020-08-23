import re
ideal_variable = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# r => treat input as raw string i.e. no special characters
# ^ => start with
# [] => set of valid characters
# * => as many characters as possible(since we have to check throughtout the variable name)
# $  => end with

check1 = re.search(ideal_variable,"_this_is_a_valid_variable_name")
check2 = re.search(ideal_variable,"this is invalid")
check3 = re.search(ideal_variable,"3again_invalid")
check4 = re.search(ideal_variable,"this2_is_valid_1")

print(check1,check2,check3,check4)
