def convert_to_array(string_of_examples):
    """
    This function is used to convert the given string into array based on the movie id(columns) and the user id(rows)
    :param string_of_examples: This is the string of input data
    :return: The dictionary having the rating for each user and movie
    """
    data = {}
    # In this case we are just appending all the movies for each user in that users key
    for each in string_of_examples:
        each = each.rstrip()
        string = each.split(',')
        if string[1] not in data:
            data[string[1]] = {}
            data[string[1]][string[0]] = string[2]
        else:
            data[string[1]][string[0]] = string[2]
    return data
