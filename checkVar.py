import random

def createCal(min, max):
    a = random.randint(min, max)
    b = random.randint(min, max)
    operand = random.choice(["+", "-"])
    question = str(a) + ' ' + operand + ' ' + str(b)
    answer = eval(question)
    return a, b, operand, answer

def createAndCheckCal(min, max, difficulty):
    a = random.randint(min, max)
    b = random.randint(min, max)
    operand = random.choice(["+", "-"])
    question = str(a) + ' ' + operand + ' ' + str(b)
    answer = eval(question)
    if difficulty == "Easy":
        while answer < 0 or answer > 100:
            a, b, operand, answer = createCal(min, max)
    else:
        while answer < 0:
            a, b, operand, answer = createCal(min, max)
    return a, b, operand, answer