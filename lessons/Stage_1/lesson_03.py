def example_1():
    var = 0
    new_var = bool(var)
    print(type(new_var), new_var)

def example_2():
    var_false = False
    var_true = True

    print(type(var_true), var_true)
    print(type(var_false), var_false)

def example_3():
    print(True and False) # False
    print(True and True) # True
    print(False and False) # False

def example_4():
    print(True or False) # True
    print(True or True) # True
    print(False or False) # False

def example_5():
    print(not True) # False
    print(not False) # True


def example_6():
    first_val = 200
    second_val = 200
    third_val = -200

    print(id(first_val))
    print(id(second_val))
    print(id(third_val))
    # Урок 3. 4:43 Незрозуміло як у first_val та second_val можуть бути однакові id. Я не розумію як працюють id

    print(first_val is second_val) # True
    print(first_val is third_val) # False

def example_7():
    first_val = 200
    second_val = 200
    third_val = -200

    print(first_val == second_val) # True
    print(first_val == third_val) # False

    print()

    print(first_val != second_val) # False
    print(first_val != third_val) # True
    # Урок 3. 5:00 Я не розумію в яких ситуаціях id з однаковим значенням будуть не збігатися

def example_8():
    answer_1 = int(input("3+3 =:"))
    assert answer_1 == 6, "Wrong answer."

    print("correct answer")
    print("next question")

    answer_2 = int(input("3+7 =:"))
    assert answer_2 == 10, "Wrong answer."

    print("well done")
