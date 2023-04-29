chosennum = float(input("Write the number you wan't to be found here:"))



def retry(chosennum, trying, escalation, upscale, lv):
    if escalation == "yes":
        if chosennum > trying:
            lv = trying
            trying *= 2
            upscale += 1
            escalation = "yes"
            retry(chosennum, trying, escalation, upscale, lv)

        if trying > chosennum:
            escalation = "no"
            retry(chosennum, trying, escalation, upscale, lv)
        exit()
    if (trying - 0.1) <= chosennum <= (trying + 0.1):
        print(trying, "=", chosennum, "\n", "times: ", upscale)
    else:
        print(lv, trying)
        lvmellan = trying
        trying = (lv + trying)/2
        if lvmellan < trying:
            lv = lvmellan
        retry(chosennum, trying, escalation, upscale, lv)


retry(chosennum, trying=1, escalation="yes", upscale=0, lv="None")
