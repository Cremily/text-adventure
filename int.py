even_list = []
odd_list = []
evens = 0
odds = 0
for x in range(0,10):
    number = int(input("Give an integer!"))
    if number % 2 == 0:
        evens += 1
        even_list.append(number)
    else:
        odds += 1
        odd_list.append(number)
print("There were %s odds and %s evens!" % (odds,evens))
print(even_list)
print(odd_list)