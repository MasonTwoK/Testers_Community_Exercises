grades = [5, 4, 5, None, 2, 4, 3]


def example_1(grades_list):
    for i in grades_list:
        if i == 2:
            print('Got the bad mark')
            break
        elif i is None:
            pass
        else:
            print(i)
    else:
        print('Bad marks were not found')

    print("End of work")


def example_2(grades_list):
    n = 0
    while n < len(grades_list):
        if grades_list[n] == 2:
            print('Got the bad mark')
            break
        elif grades_list[n] is None:
            n += 1
            continue
        else:
            print(grades_list[n])
        n += 1
    else:
        print("We haven't bad marks")

    print('The end.')
