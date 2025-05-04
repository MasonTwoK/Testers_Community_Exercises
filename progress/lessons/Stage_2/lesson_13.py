def example_1():
    total_adds = 92
    adds_per_page = 8

    full_pages_count = total_adds // adds_per_page
    print(f"Amount of full pages: {full_pages_count}")

    last_page_adds = total_adds % adds_per_page
    print(f"Advertisements on last page amount: {last_page_adds}")

def example_2():
    total_apples = 11
    amount_of_persons = 3

    apples_per_person = total_apples // 3
    print(f"Each person got: {apples_per_person}")

    apples_left = total_apples % amount_of_persons
    print(f"Apples left: {apples_left}")
