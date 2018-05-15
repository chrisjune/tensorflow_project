import random
#Digits generate
def generate_digits():
    digits = list(str(num) for num in range(10))
    random.shuffle(digits)
    return digits[:3]

#Get input
def get_input():
    guess = list(input("Guess number: "))
    return guess

#Compare
def compare(digits,guess):
    '''
    Digits = '123'
    Guess = '123'
    '''
    result = []
    if digits == guess:
        result.append("PerfectMatch")
        return result
    for i in range(3):
        if digits[i] == int(guess[i]):
            result.append("Match")
        elif int(guess[i]) in digits:
            result.append("Close")
    if result == []:
        result.append("Nope")
    return result

#Main
digits=generate_digits()
result = []
while result != ["PerfectMatch"]:
    guess = get_input()
    print("Digits:",digits,"Guess:",guess)
    result = compare(digits,guess)
    print(result)