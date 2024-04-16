def is_palindrome(number):
  
    return str(number) == str(number)[::-1]

valid_numbers = []
current_number = 10 

while len(valid_numbers) < 12:
    reversed_number = int(str(current_number)[::-1])
    if reversed_number % current_number == 0 and not is_palindrome(current_number) and not is_palindrome(reversed_number):
        valid_numbers.append(current_number)
    current_number += 1

print("Expected Answer:")
for number in valid_numbers:
    print(number)