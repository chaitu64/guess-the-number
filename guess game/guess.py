import random

low_number = 1
high_number = 100

random_number = random.randint(low_number, high_number)  # oka randam num genator chestam ekkada

print('Welcome to guessing Game')

print(f'well just for reference {random_number} ')  # just manaki correct ga run avutunda ani

keep_running = True

while keep_running:

    try:
        guess = int(input(f'Guess a number between {low_number} and {high_number} '))  
        if guess < low_number or guess > high_number:
            print('sakkaga chusi enter cheyyi bayya')
        elif guess > random_number:
            print('kucham chinna Value chudu bro') #ichina value padadi ayitey
        elif guess < random_number:
            print('kuncham peddaga alochinchu bro') #same antey kani reverse
        else:
            print('Abba bale guess chesavu bayya')
            keep_running = False

    except ValueError:
        print("Invalid input. Please enter a number.")