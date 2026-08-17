cubes = {numb : numb**3 for numb in range(1,11)}
print(cubes)
# num : num**3 - assign this to a variable

text = "programming"
freq = {}
for char in text:
    freq[char] = freq.get(char,0) + 1

print(freq)

languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# enumerate () func returns index and the item - used in lists, string etc not dict , anything iterable except dict
for index, value in enumerate(languages):
    print(f"{index + 1} : {value}")

prime_numbers = []
for x in range(1, 51):
    if x > 1 and all(
        x % y != 0 for y in range(2, int(x**0.5) + 1)
    ):  # a number is prime if n>1 and n % i is not equal to zero for all integers between 2 and root(n).
        # This part of code not working
        prime_numbers.append(x)
    else:
        continue
print(prime_numbers)

primes = []
for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)


