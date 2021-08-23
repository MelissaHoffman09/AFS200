# List of friends from 'csv' 
csv = "Eric,John,Michael,Terry,Graham,TerryG,Brian"

# Split List 
friends_list = csv.split(',')
print("Split List:", friends_list)

# Join List
friends_join = ', '.join(friends_list)
print("Join List:", friends_join)