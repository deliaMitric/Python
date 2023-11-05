#ex1
#Write a function that receives as parameters two lists a and b and
# returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def ex1(list1, list2):
    intersection = set(list1) & set(list2)
    union = set(list1) | set(list2)
    difference12 = set(list1) - set(list2)
    difference21 = set(list2) - set(list1)

    result_list = [intersection, union, difference12, difference21]
    print(result_list)
    return result_list

#ex2
#Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences of that character in the given text.
def ex2(string):
    dict_characters = {character:string.count(character) for character in string}
    print(dict_characters)
    return dict_characters

#ex3
#Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers,
# such as dictionaries, lists, sets, etc.)
def compare_sets(set1, set2):
    if len(set1) != len(set2):
        return False
    how_much_find = 0

    for element1 in set1:
        find = False
        for element2 in set2:
            if recursively_check(element1, element2):
                find = True
        if find:
            how_much_find += 1
    if how_much_find == len(set1):
        return True
    return False


def recursively_check(element1, element2):
    if type(element1) != type(element2):
        return False
    if isinstance(element1, dict):
        if len(element1) != len(element2):
            return False

        for key in element1.keys():
            if key not in element2:
                return False

            val1 = element1[key]
            val2 = element2[key]
            if not recursively_check(val1, val2):
                return False
    elif isinstance(element1, list):
        if len(element1) != len(element2):
            return False
        for val1, val2 in zip(element1, element2):
            if not recursively_check(val1, val2):
                return False

    elif isinstance(element1, set):
        if len(element1) != len(element2):
            return False
        return compare_sets(element1, element2)

    elif isinstance(element1, tuple):
        if len(element1) != len(element2):
            return False
        for val1, val2 in zip(element1, element2):
            if not recursively_check(val1, val2):
                return False
    elif element1 != element2:
        return False
    return True

#ex4
#The build_xml_element function receives the following parameters: tag, content,
#and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element.
def ex4(tag, content, **elements):
    result_html = f"<{tag}"
    for key in elements.keys():
        result_html += f" {key}={elements.get(key)}"
    result_html += f">{content}</{tag}>"

    print(result_html)
    return result_html

#ex5
#
def ex5(rules, elements):
    for key in elements:
        find = False
        value = elements.get(key)
        if not isinstance(key, str):
            return False
        if not isinstance(value, str):
            return False

        new_value = ""
        #daca cheia si valoarea e string verificam daca respecta o ragula din rules
        for rule in rules:
            if rule[0] == key:
                find = True

                #prefix
                if rule[1] != "" and not value.startswith(rule[1]):
                    return False
                new_value += value[len(rule[1]):]

                #sufix
                if rule[3] != "" and not new_value.endswith(rule[3]):
                    return False

                #middle
                if rule[2] != "" and not new_value.find(rule[2], 0, len(new_value) - len(rule[3])):
                    return False



        if not find:
            return False
    return True

#ex6
#Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).
def ex6(elements):
    #varianta in care se numara toate aparitiile in plus ale unui element unic, ex: [5,5,3,3,3] -> (2,3)
    # if isinstance(elements, list):
    #     elements_set = set(elements)
    #     return (len(elements_set), len(elements) - len(elements_set))

    ##varinta in care se numara doar o data duplicatul, ex: [5,5,3,3,3] -> (2,2)
    if isinstance(elements, list):
        elements_set = set(elements)
        number_duplicate = 0
        for unique_element in elements_set:
            if elements.count(unique_element) > 1:
                number_duplicate += 1
        return (len(elements_set), number_duplicate)

    return "not a list!"


#ex7
#Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two:
# reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
def ex7(*sets):
    sets_copy = list(sets).copy()
    dict_operations = {}
    for first_set in sets:
        sets_copy.remove(first_set)
        for second_set in sets_copy:
            if len(first_set) > 0 and len(second_set) > 0:
                key = str(first_set)
                key += " | "
                key += str(second_set)
                dict_operations[key] = first_set | second_set

                key = str(first_set)
                key += " & "
                key += str(second_set)
                dict_operations[key] = first_set & second_set

                key = str(first_set)
                key += " - "
                key += str(second_set)
                dict_operations[key] = first_set - second_set

                key = str(second_set)
                key += " - "
                key += str(first_set)
                dict_operations[key] = second_set - first_set

            elif len(first_set) == 0:
                key = str(first_set)
                key += " | "
                key += str(second_set)
                dict_operations[key] = second_set

                key = str(first_set)
                key += " & "
                key += str(second_set)
                dict_operations[key] = {}

                key = str(first_set)
                key += " - "
                key += str(second_set)
                dict_operations[key] = {}

                key = str(second_set)
                key += " - "
                key += str(first_set)
                dict_operations[key] = second_set

            elif len(second_set) == 0:
                key = str(first_set)
                key += " | "
                key += str(second_set)
                dict_operations[key] = first_set

                key = str(first_set)
                key += " & "
                key += str(second_set)
                dict_operations[key] = {}

                key = str(first_set)
                key += " - "
                key += str(second_set)
                dict_operations[key] = first_set

                key = str(second_set)
                key += " - "
                key += str(first_set)
                dict_operations[key] = {}
    return dict_operations

#ex8 (10)
#Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way:
# the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
def ex8(mapping):
    visited =[]
    result_list = []
    if 'start' not in mapping:
        return "no start key in dict!"
    value = mapping.get('start')
    while value not in visited and value is not None and len(visited) != len(mapping):
        visited.append(value)
        result_list.append(value)
        value = mapping.get(value)
    return result_list

#ex9
#Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.
def ex9(*arguments, **pos_arguments):
    contor = 0
    for key in pos_arguments:
        if pos_arguments.get(key) in arguments:
            contor += 1
    return contor

def main():
    #ex1([1,2,3,4],[2,3,4,5])
    #ex2("Ana are mere multe si marunte.!")
    # print(recursively_check({
    # 'numere': [1, 2, 3],
    # 'stringuri': ['abc', 'def', 'ghi'],
    # 'seturi': {(1, 2), 1, 3},
    # 'dictionare': {'a': 10, 'b': 20}}, {
    # 'numere': [1, 2, 3],
    # 'stringuri': ['abc', 'def', 'ghi'],
    # 'seturi': {1, (1, 2), 3},
    # 'dictionare': {'a': 10, 'b': 20}}))
    #ex4("a", "Hello there", href=" http://python.org ", _class=" my-link ", id= " someid ")
    print(ex5({("key1", "", "inside", ""), ("key2", "start", "start", "start")}, {"key1": "come inside, it's too cold out", "key2": "start"}))
    #print(ex6([1, 2, 2, 3, 4, 3, 4, 1, 6, 7, 8, 9, 7, 3, 7]))
    #print(ex7({1, 2, 3}, {}, {3, 5, 8}))
    #print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    #print(ex9(1, 2, 3, 4,'123', x='123', y=2, z=3, w=5))
if __name__ == "__main__":
    main()
