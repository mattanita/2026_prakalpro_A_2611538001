first_name = " muhammad "
last_name = "rafi "

full_name = first_name.strip() + " " + last_name.strip()

print(full_name)
print(full_name.title())

# Question 6: Campus Username

full_name = " Matt Anita"
nim = "2611538001"

# Remove spaces at the beginning and end
clean_name = full_name.strip()

# find the first space
space_position = clean_name.find(" ")

# Get the first name
if space_position == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space_position]

# Build the username
username = first_name.lower() + nim[-3:]

print("Campus username:", username)
