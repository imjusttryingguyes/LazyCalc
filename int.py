# write your code here
result = 0
memory = float(0)
msg = ["Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]


def digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
        return output
    else:
        output = False
        return output

def check(v1, v2, v3):
    msg = ''
    if digit(v1) is True and digit(v2) is True:
        msg = msg + ' ... lazy'
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + ' ... very lazy'
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + ' ... very, very lazy'
    if msg != '':
        msg = 'You are' + msg
        print(msg)



def calculation():
    count = 1
    global result
    while count > 0:
        print('Enter an equation')
        calc = input()
        calc = calc.split()

        if calc[0] == 'M':
            calc[0] = memory
        if calc[-1] == 'M':
            calc[-1] = memory

        try:
            calc[0] = float(calc[0])
        except ValueError:
            calc[0] = 'error'

        try:
            calc[-1] = float(calc[-1])
        except ValueError:
            calc[-1] = 'error'

        check(calc[0], calc[-1], calc[1])

        if calc[0] == 'error' or calc[-1] == 'error':
            print('Do you even know what numbers are? Stay focused!')
        elif calc[1] != '+' and calc[1] != '-' and calc[1] != '*' and calc[1] != '/':
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        elif calc[1] == '/' and calc[-1] == 0:
            print('Yeah... division by zero. Smart move...')
        else:
            count -= 1


    if calc[1] == "+":
        result = calc[0] + calc[-1]
        print(calc[0] + calc[-1])
    elif calc[1] == '-':
        result = calc[0] - calc[-1]
        print(calc[0] - calc[-1])
    elif calc[1] == '*':
        result = calc[0] * calc[-1]
        print(calc[0] * calc[-1])
    else:
        result = calc[0] / calc[-1]
        print(calc[0] / calc[-1])

calculation()
answering = 1

while answering > 0:
    print('Do you want to store the result? (y / n):')
    answer = input()

    if answer == 'y':
        msg_index = 0
        while msg_index < 3:
            if digit(result) is True:
                print(msg[msg_index])
                answer_3 = input()
                if answer_3 == 'y':
                    msg_index += 1
                    if msg_index == 2:
                        memory = result
                else:
                    msg_index += 2
                    break
            else:
                msg_index += 2
                memory = result
                break


        print('Do you want to continue calculations? (y / n):')
        answer_2 = input()
        if answer_2 == 'y':
            calculation()
        elif answer_2 == 'n':
            answering -= 1
    elif answer == 'n':
        print('Do you want to continue calculations? (y / n):')
        answer_2 = input()
        if answer_2 == 'y':
            calculation()
        elif answer_2 == 'n':
            answering -= 1
