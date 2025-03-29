from copy import deepcopy

our_dict_1 = {
        "key_1": "value_1",
        "key_2": "value_2",
        "key_3": "value_3"
    }

our_dict_2 = {
        "key_1": "value_1",
        "key_2": "value_2",
        "key_3": "value_3",
        "key_11": "value_11",
        "key_12": "value_12"
    }

our_dict_3 = {
        "key_1": "value_1",
        "key_2": "value_2",
        "key_3": "value_3",
        "key_9": [1, 2, 3]
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


def example_3_delete(dictionary_object):
    del dictionary_object['key_3']
    # del dictionary_object['key_10']  # this one will break the code
    print(dictionary_object.pop('key_1'))
    print(dictionary_object)
    dictionary_object.popitem()
    print(dictionary_object)
    dictionary_object.clear()
    print('->', dictionary_object)


def example_4_copy(dictionary_object):
    our_dict_4 = dictionary_object.copy()
    our_dict_4.update({'key=10': 'value_10'})
    our_dict_4['key_9'].append('11')

    print(dictionary_object)
    print(our_dict_4)


def example_5_deepcopy(dictionary_object):
    our_dict_4 = deepcopy(dictionary_object)
    our_dict_4.update({'key_10': 'value_10'})
    our_dict_4['key_9'].append('11')

    print(dictionary_object)
    print(our_dict_4)


def example_6(dictionary_object):
    for item in dictionary_object.items():
        print(item)
    print(' ')

    for key in dictionary_object.keys():
        print(key)
    print(' ')

    for value in dictionary_object.values():
        print(value)

