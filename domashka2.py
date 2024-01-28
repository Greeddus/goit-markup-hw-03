import random
def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
       nums = random.randint(min, max)
       if nums not in lottery_numbers:
           lottery_numbers.add(nums)

    return sorted(list(lottery_numbers))




lottery_numbers = get_numbers_ticket(1, 1000, 10)
print(lottery_numbers)