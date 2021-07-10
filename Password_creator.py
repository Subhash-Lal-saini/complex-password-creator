import random
import array

# We can set our password lenth
# maximum length of password needed
# this can be changed to suit your password length
Total_len = 12

# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

Special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

# mix all the character arrays above to form one array
Mix_all = Numbers + UPERCASE + lowercase + Special

# randomly select at least one character from each character set above
rand_digit = random.choice(Numbers)
rand_upper = random.choice(UPERCASE)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(Special)

# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(Total_len - 4):
	temp_pass = temp_pass + random.choice(Mix_all)

	# convert temporary password into array and shuffle to
	# prevent it from having a consistent pattern
	# where the beginning of the password is predictable
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
		password = password + x
		
# print out password
print("Please find Your best password :",password)
