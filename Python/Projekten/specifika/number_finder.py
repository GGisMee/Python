import math
def find_number(precision, devider, roof, guess_number):
    changer = roof
    number: int = 0 # numret som ska bli inp
    while not guess_number-precision < number < guess_number+precision:
        changer/=devider
        # time.sleep(3)
        if number < guess_number: 
            number += changer
        elif number > guess_number: 
            number -= changer
    iterations = round(-((math.log10(changer/roof))/(math.log10(devider))))
    return number, iterations


# kan typ göra en algoritm som hittar det värdet där numret hittas oftast, med ai blir det ännu mer nice