print("\nExercise #1\n")

for num in range(1, 21):
    print(num)

print("\nExercise #2\n")

one_mil_nums = list(range(1, 1000001))
print(f"Minimum {one_mil_nums[0]}")
print(f"Maximum {one_mil_nums[-1]}")

print("\nExercise #3\n")

counter = 0
for mil_num in one_mil_nums:
    counter = counter + mil_num
print(f"Total is {counter}")


print("\nExercise #4\n")

odd_numbers = list(range(1, 21, 2))

for odd_num in odd_numbers:
    print(odd_num)

print("\nExercise #5\n")

multiples = list(range(3, 31, 3))

for multiple in multiples:
    print(multiple)

print("\nExercise #6\n")

numbers_to_power = list(range(1, 11))

for number in numbers_to_power:
    print(number**3)

