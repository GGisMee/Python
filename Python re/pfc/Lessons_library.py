global mellanrum

def restart(code_run, name_or_numb):

    all_tutorials = (
        "1__python_tutorial_for_beginners",
        "2___variables",
        "3__multiple_assignment",
        "4___string_methods_",
        "5___type_cast",
        "6___user_input",
        "7___math_functions",
        "8___string_slicing",
        "9___if_statements",
        "10__logical_operators",
        "11__while_loops",
        "12__for_loops",
        "13__nested_loops",
        "14__break_continue_pass",
        "15__lists",
        "16__2D_lists",
        "17__tuples",
        "18__sets",
        "19__dictionaries",
        "20__indexing",
        "21__functions",
        "22__return_statement",
        "23__keyword_arguments",
        "24__nested_function_calls",
        "25__variable_scope",
        "26__args",
        "27__kwargs",
        "28__string_format",
        "29__random_numbers",
        "30__exception_handling",
        "31__file_detection",
        "32__read_a_file",
        "33__write_a_file",
        "34__copy_a_file",
        "35__move_a_file",
        "36__delete_a_file",
        "37__modules",
        "38__rock,_paper,_scissors_game",
        "39__quiz_game",
        "40__Object_Oriented_Programming_OOP",
        "41__class_variables",
        "42__inheritance",
        "43__multilevel_inheritance",
        "44__multiple_inheritance",
        "45__method_overriding",
        "46__method_chaining",
        "47__super_function",
        "48__abstract_classes",
        "49__objects_as_arguments",
        "50__duck_typing",
        "51__walrus_operator",
        "52__functions_to_variables",
        "53__higher_order_functions",
        "54__lambda",
        "55__sort",
        "56__map",
        "57__filter",
        "58__reduce",
        "59__list_comprehensions",
        "60__dictionary_comprehensions",
        "61__zip_function",
        "62__if_name_==___main__",
        "63__time_module",
        "64__threading",
        "65__daemon_threads",
        "66__multiprocessing",
        "67__GUI_windows",
        "68__labels",
        "69__buttons",
        "70__entrybox",
        "71__checkbox",
        "72__radio_buttons",
        "73__scale",
        "74__listbox",
        "75__messagebox",
        "76__colorchooser",
        "77__text_area",
        "78__open_a_file_file_dialog",
        "79__save_a_file_file_dialog",
        "80__menubar",
        "81__frames",
        "82__new_windows",
        "83__window_tabs",
        "84__grid",
        "85__progress_ba",
        "86__canvas",
        "87__keyboard_events",
        "88__mouse_events",
        "89__drag_&_drop",
        "90__move_images_w_keys",
        "91__animations",
        "92__multiple_animations",
        "93__clock_program",
        "94__send_an_email",
        "95__run_with_command_prompt",
        "96__pip",
        "97__py_to_exe",
        "98__calculator_program",
        "99__text_editor_program",
        "100__tic_tac_toe_game",
        "101__snake_game",
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
        for i in range(0, 100):
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
            name_of_tut = "/Users/gustavgamstedt/PycharmProjects/programmering/Python/Code_storage/pfc/tutorials/" + all_tutorials[int(name_or_numb) - 1]+".py"
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
