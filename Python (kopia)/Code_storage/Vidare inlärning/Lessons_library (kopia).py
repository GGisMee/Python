global mellanrum


def restart(code_run, name_or_numb):

    all_tutorials = (
        "1__F_Strings"
    )

    def number_chooser():

        try:
            int(name_or_numb)
            print("----------------------------------------------------")
            print(all_tutorials[int(name_or_numb) - 1] + " is run here below:")
            print("----------------------------------------------------")
            if code_run == "run":
                __import__("tutorials." + all_tutorials[int(name_or_numb) - 1])
            if code_run == "code":
                coderunner(new_value=None)
        except ValueError:
            try:
                print("----------------------------------------------------------------------------------------------------")
                chosen_tutorial = int(input("Which number?: "))
                print("----------------------------------------------------")
                print(all_tutorials[int(chosen_tutorial) - 1] + " is run here below:")
                print("----------------------------------------------------")
                if code_run == "code":
                    coderunner(new_value=None)
                if code_run == "run":
                    __import__("tutorials." + all_tutorials[int(chosen_tutorial) - 1])
                print("----------------------------------------------------")
            except ValueError:
                number_chooser()

    def view():
        print("----------------------------------------------------------------------------------------------------")

        import cmd
        cli = cmd.Cmd()
        # noinspection PyTypeChecker
        cli.columnize(all_tutorials, displaywidth=120)
        number_chooser()

    def by_name():
        list_over_concluded_lessons = []
        tutorialpart = name_or_numb.lower()
        for i in range(0, 1):
            if tutorialpart in all_tutorials[i]:
                list_over_concluded_lessons.append(all_tutorials[i])
        if len(list_over_concluded_lessons) > 1:
            for i in range(0, len(list_over_concluded_lessons)):
                print(i + 1, ": ", list_over_concluded_lessons[i])
            try:
                chosen_tutorial = int(input("Choose number by lessons (1 to " + str(len(list_over_concluded_lessons)) + "): "))
            except ValueError:
                print("Needs to be a number")
                exit()
            try:
                new_value = list_over_concluded_lessons[chosen_tutorial - 1]
            except IndexError:
                print("Needs to be a smaller number")
                exit()
            print("----------------------------------------------------")
            print(new_value + " is being run below:")
            print("----------------------------------------------------")

            if code_run == "run":
                __import__("tutorials." + new_value)
            if code_run == "code":
                coderunner(new_value)

        if len(list_over_concluded_lessons) == 1:
            try:
                lista_over_lessons = list_over_concluded_lessons[0]
            except IndexError:
                print("Your input didn't include number or letter, but symbols or both, try again")
                exit()
            print("----------------------------------------------------")
            print(lista_over_lessons+ " is being run below:")
            print("----------------------------------------------------")
            __import__("tutorials." + lista_over_lessons)

    def coderunner(new_value):
        try:
            name_of_tut = "/Users/gustavgamstedt/PycharmProjects/programmering/Python/Code_storage/tutorials/" + all_tutorials[int(name_or_numb) - 1]+".py"
            with open(name_of_tut) as file:
                fileinfo = file.read()
                print(fileinfo)
        except FileNotFoundError:
            print("didn't find: " + all_tutorials[int(name_or_numb) - 1]+" \n In form:"+name_of_tut)
        except ValueError:
            try:
                name_of_tut = "/Users/gustavgamstedt/PycharmProjects/programmering/Python/Code_storage/tutorials/" +new_value+".py"
                with open(name_of_tut) as file:
                    fileinfo = file.read()
                    print(fileinfo)

            except TypeError:
                print(str(new_value) + "\n break name or numb after  "+all_tutorials[int(name_or_numb) - 1])
        print("----------------------------------------------------------------------------------------------------")
        exe = input("exe?: ")
        if exe == "":
            try:
                __import__("tutorials." + new_value)
            except TypeError:
                __import__("tutorials." + all_tutorials[int(name_or_numb) - 1])
            print("----------------------------------------------------")
        else:
            exit()
    # ------------------------------------------------------------------------------------------

    while name_or_numb == "":
        name_or_numb = input("Inp: ")
    if "!" in name_or_numb.upper():
        lista_over_tasbort = []
        avslutning_hmm = "!"
        Editas = name_or_numb
        if "*" not in avslutning_hmm:
            lista_over_tasbort.append(avslutning_hmm)
        for char in lista_over_tasbort:
            name_or_numb = Editas.replace(char, "")
        code_run = "run"

    try:
        int(name_or_numb)
        number_chooser()


    except ValueError:
        if code_run == "run":
            if name_or_numb.upper() == "#V":
                view()

        if name_or_numb.upper() == "#HELP":
            print("----------------------------------------------------")
            print("The following things can be done:")
            print("Type the number of the tutorial to write it out")
            print("Or type parts or the whole name of the program")
            print("----------------------------------------------------")
            print("Commands include: ")
            print("#V for view of all programs")
            print("----------------------------------------------------")
            print("Additions include: ")
            print("! to run program")

        else:

            by_name()


restart(code_run="code", name_or_numb="")
