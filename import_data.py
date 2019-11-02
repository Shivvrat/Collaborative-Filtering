import os

def import_train_data(data_set_name):
    """
    This function is used to import the train data
    :param data_set_name: Please provide the name of dataset in string format
    :return: the string containing all train dataset
    """
    path = os.path.join(os.getcwd(), data_set_name)
    path = os.path.join(path, "TrainingRatings.txt")
    # We are just adding the values for train dataset to the string with adding a new line
    with open(path) as files:
        string_train = files.readlines()
    return string_train

def import_test_data(data_set_name):
    """
    This function is used to import the test data
    :param data_set_name: Please provide the name of dataset in string format
    :return: the string containing all test dataset
    """
    path = os.path.join(os.getcwd(), data_set_name)
    path = os.path.join(path, "TestingRatings.txt")
    # We are just adding the values for test dataset to the string with adding a new line
    with open(path) as files:
        string_train = files.readlines()
    return string_train

