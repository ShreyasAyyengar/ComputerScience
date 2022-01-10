list_of_people = []

john = {"name": "john", "favourite_number": 12}

sarah = {"name": "sarah", "favourite_number": 55}

madison = {"name": "madison", "favourite_number": 81}

jim = {"name": "jim", "favourite_number": 2}

pete = {"name": "pete", "favourite_number": 15}

list_of_people.append(john)
list_of_people.append(sarah)
list_of_people.append(madison)
list_of_people.append(jim)
list_of_people.append(pete)

try:
    for people in list_of_people:
        print(people["name"] + "'s favourite number is " + people["favourite_number"].__str__())
        print(people.get("random_key_that_i_know_for_a_fact_does_not_exist", "Key-Value <K, V> pair does not exist!"))

except KeyError:
    print("Key-Value <K, V> pair does not exist!")
