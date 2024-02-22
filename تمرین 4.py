user_input = input("reshte ra vared konid")
numbers = user_input.split(',')
for i in range(len(numbers)):
    print(f'index {i}: {len(numbers[i])} len')
