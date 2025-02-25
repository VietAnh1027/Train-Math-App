import random

def createCal(min, max):
    a = random.randint(min, max)
    b = random.randint(min, max)
    operand = random.choice(["+", "-"])
    question = str(a) + ' ' + operand + ' ' + str(b)
    answer = eval(question)
    return a, b, operand, answer

def createAndCheckCal(min: int, max: int):
    a, b, operand, answer = createCal(min, max)
    while answer < 0:
        a, b, operand, answer = createCal(min, max)
    return a, b, operand, answer