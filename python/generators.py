def square_numbers_as_list(nums):
    squared = []
    for i in nums:
        squared.append(i * i)
    return squared


def square_numbers_as_generator(nums):
    for i in nums:
        yield (i * i)


# my_nums = square_numbers([1,2,3,4,5])

# list
my_nums = [x * x for x in [1, 2, 3, 4, 5]]

# generator
my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(next(my_nums))

# or

for num in my_nums:
    print(num)
