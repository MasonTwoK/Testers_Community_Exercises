our_dict = {
        "key_1": "value_1",
        "key_2": "value_2",
        "key_3": "value_3"
    }


def example_1(dictionary_object):
    # print(dictionary_object['key_4'])  # KeyError: 'key_4'
    print(dictionary_object['key_1'])  # value 1
    print(dictionary_object.get('key_4'))  # None
    print(dictionary_object.get('key_1'))  # value 1
    print(dictionary_object.get("key_4", "text in case key was missing"))  # text in case key was missing
    print(dictionary_object)


def example_2(dictionary_object):
    print(dictionary_object.setdefault("key_5", "value_5"))  # updates dictionary_object with a new pair of key:value
    print(dictionary_object.setdefault("key_1", "value_6"))  # Value for key_1 won't change by getting 2 parameters
    print(dictionary_object)

    dictionary_object["key_1"] = "value_6"  # updates "key_1" with "value_6"
    dictionary_object["key_6"] = "value_6"  # updates dictionary with pair "key_6": "value_6"
    print(dictionary_object)

    dictionary_object.update({"key_1": "value_7"})  # updates "key_1" with "value_7" by getting {dict}
    dictionary_object.update({"key_8": "value_8"})  # updates dictionary with pair "key_8": "value_8" by getting {dict}
    print(dictionary_object)


example_2(our_dict)
