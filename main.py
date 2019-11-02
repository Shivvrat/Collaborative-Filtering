import sys
import warnings
import numpy as np
import convert_data_to_array
import evaluation_metrics
import import_data
import train_collaborative_filtering

warnings.filterwarnings("ignore")


def import_files(dataset_name):
    """
    This function is used to import both the training and the testing datasets
    :param dataset_name: The name of the dataset
    :return: The dictionaries for each users in the dataset
    """
    try:
        string_train = import_data.import_train_data(dataset_name)
        data_dict_train = convert_data_to_array.convert_to_array(string_train)
    except:
        print "You have given wrong dataset name or the dataset is in wrong directory, please check"
        exit(1)
    string_train = import_data.import_test_data(dataset_name)
    data_dict_test = convert_data_to_array.convert_to_array(string_train)
    return data_dict_test, data_dict_train


def run_algorithm(data_dict_test, data_dict_train):
    """
    This function is the main function for the algorithm which adds all the bits and pieces
    :param data_dict_test: the test data
    :param data_dict_train: the train data
    :return: the values for RMSE and MAE
    """
    predicted_values = []
    actual_values = []
    for each_user_key in data_dict_test:
        for each_movie in data_dict_test[each_user_key]:
            user_movie_pair = {each_user_key: {each_movie: data_dict_test[each_user_key][each_movie]}}
            data, predicted_rating = train_collaborative_filtering.find_output(data_dict_train, user_movie_pair,
                                                                               each_movie,
                                                                               each_user_key)
            predicted_values.append(predicted_rating)
            actual_values.append(np.fromstring(data_dict_test[each_user_key][each_movie], dtype=np.float, sep=" ")[0])
            # print predicted_rating, data_dict_test[each_user_key][each_movie]
    mae = evaluation_metrics.get_mean_absolute_error(actual_values, predicted_values)
    rmse = evaluation_metrics.get_root_mean_squared_error(actual_values, predicted_values)
    return mae, rmse


# Here we take the inputs given in the command line
arguments = list(sys.argv)
try:
    data_set_name = str(arguments[1])
except:
    print "You have not provided enough arguments, please provide the dataset name or read the readme"
    exit(-1)


def main():
    """
    This is the main function which is used to run the algorithm
    :return: Nothing just print the evaluation metrics
    """
    data_dict_test, data_dict_train = import_files(data_set_name)
    mae, rmse = run_algorithm(data_dict_test, data_dict_train)
    print "Mean absolute error :-", mae, "\nRoot mean square error :-", rmse


if __name__ == "__main__":
    main()
