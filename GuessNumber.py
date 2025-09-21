import random

number = random.randint(1,100)
attempts = 0
max_attempts = 7

print("Tebak angka (1 - 100)")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}: Masukan tebakan mu: "))
        attempts +=1

        if guess == number:
            print("Benar bgt, tebakan mu tepat")
            break
        elif guess < number:
            print("kekecilan")
        else: 
            print("kebesaran")

    except ValueError:
        print("Masukin angka yang benar")

if attempts == max_attempts and guess != number:
    print(f"Diluar batas {number}")