import random
import time

difficult = input("Choose your mode: Easy / Normal / Hard: ")
while difficult not in {"Easy", "Normal", "Hard"}:
    print("This mode doesn't not exist !")
    difficult = input("Choose your mode: Easy / Normal / Hard: ")

operand_lst = ['+', '-']

if difficult == "Easy":
    min = 1
    max = 9
if difficult == "Normal":
    min = 10
    max = 50
if difficult == "Hard":
    min = 100
    max = 1000

number_ques = int(input("How many quest do you want ?: "))
operand = random.choice(operand_lst)


def createCal():
    a = random.randint(min,max)
    b = random.randint(min,max)
    operand = random.choice(operand_lst)
    question = str(a) + ' ' + operand + ' ' + str(b)
    answer = eval(question)
    return question, answer


def challenge(number_ques):
    wrong = 0
    input("Are you ready, Press Enter to start !")
    for i in range(number_ques):
        q, a = createCal()
        if difficult == 'Easy':
            while a < 0 or a > 10:
                q, a = createCal()
        your_answer = input('Question {}: {} = '.format(i+1, q))
        while your_answer != str(a):
            wrong += 1
            print("Wrong !")
            your_answer = input('Question {}: {} = '.format(i+1, q))
    return wrong


start_time = time.time()

wrong = challenge(number_ques)

end_time = time.time()
time_finish = round(end_time - start_time, 2)


print("Congratulation ! You finished {} questions in {} with {} errors".format(number_ques, time_finish, wrong))