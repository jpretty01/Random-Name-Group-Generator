import random

# Enter the list of names separated by commas
names = input("Enter the list of names separated by commas: ")
names_list = [name.strip() for name in names.split(',')]

# Shuffle the list of names
random.shuffle(names_list)

# Get the number of groups and the number of people in each group
num_groups = int(input("Enter the number of groups: "))
num_per_group = len(names_list) // num_groups

# Create the groups
groups = []
for i in range(num_groups):
    group = names_list[i*num_per_group:(i+1)*num_per_group]
    groups.append(group)

# Add any remaining names to the last group
if len(names_list) % num_groups != 0:
    groups[-1].extend(names_list[num_groups*num_per_group:])

# Print the groups
for i, group in enumerate(groups):
    print(f"Group {i+1}: {', '.join(group)}")
