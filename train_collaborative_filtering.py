import convert_data_to_array
import numpy as np
import math


def train(data):
    """
    This is the function used to train the model
    :param data: This is the training data
    :return: We return the mean of each user in the data
    """
    mean_vote_train_data = calculate_mean_vote_train(data)
    return mean_vote_train_data


def test(data, test_user, mean_vote_train_data, test_movie_id, test_user_id):
    """
    This function is used to do the testing
    :param data: The dict containing all the train users ratings
    :param test_user: the dict for test user
    :param mean_vote_train_data: the mean vote for the train data
    :param test_movie_id: the movie for the user for which we are testing
    :param test_user_id: The test user id
    :return: the predicted scores for our algorithm
    """
    test_mean_vote = calculate_mean_vote_test(test_user, test_movie_id, test_user_id, data)
    movie_number = test_movie_id
    predicted_vote = test_mean_vote
    normalizing_factor = 1
    sum = 0
    # Here we follow the equation 1 for each of the user and movie which gives us the predicted score
    for each_user in data:
        if movie_number in list(data[each_user]):
            sum += get_correlation(data[each_user], test_user, mean_vote_train_data[each_user], test_mean_vote, test_movie_id, test_user_id, data[test_user_id]) * (
                np.fromstring(data[each_user][movie_number], dtype=np.float, sep=" ")[0] - mean_vote_train_data[each_user])
            normalizing_factor = normalizing_factor + abs(sum)
    normalizing_factor = 1/float(normalizing_factor)
    predicted_vote += normalizing_factor * sum
    return predicted_vote


def calculate_mean_vote_train(data):
    """
    This function is used to calculate the mean votes for the train data
    :param data: This is the train dict for which mean is to be calculated
    :return: The mean values for each user
    """
    mean_vote = {}
    for each_user in data:
        if isinstance(data[each_user], dict):
            sum_of_reviews = 0
            total_number_of_reviews = 0
            # We just sum all the reviews and find the average
            for each_movie in data[each_user]:
                sum_of_reviews = sum_of_reviews + np.fromstring(data[each_user][each_movie], dtype=np.float, sep=" ")[0]
                total_number_of_reviews += 1
            mean_vote[each_user] = sum_of_reviews / float(total_number_of_reviews)
    return mean_vote


def calculate_mean_vote_test(test_example, test_movie_id, test_user_id, train_example):
    """
    This function is used to calculate the mean votes for the test user
    :param data: This is the test dict for which mean is to be calculated
    :return: The mean values for the given user
    """
    sum_of_reviews = 0
    total_number_of_reviews = 0
    try:
        user_movies = train_example[test_user_id]
    except KeyError:
        return 0
    # WE do the same as the training user, here we only have one user.
    for each_movie in user_movies:
        sum_of_reviews = sum_of_reviews + np.fromstring(user_movies[each_movie], dtype=np.float, sep=" ")[0]
        total_number_of_reviews += 1
    return sum_of_reviews / float(total_number_of_reviews)


def get_correlation(train_data_for_user, test_data_for_new_user, mean_vote_train_user, mean_vote_test_point, test_movie_id, test_user_id, all_movies_rated_by_test_user):
    """
    This function is used to implement the second equation which finds the correlation between users
    :param train_data_for_user: This is the data for the train user
    :param test_data_for_new_user: This is the data for the test user
    :param mean_vote_train_user: This is the mean vote for the train user
    :param mean_vote_test_point: This is the mean vote for the test user
    :param test_movie_id: This is the movie for the test user
    :param test_user_id: This is the user id for the test user
    :param all_movies_rated_by_test_user: This the list of the movies rated by test user
    :return: The value of the correlation
    """
    numerator = 0
    denominator_sum_1 = 0
    denominator_sum_2 = 0
    movies_rated_by_test_user = list(all_movies_rated_by_test_user)
    # Here we follow the equation and find the denominator and the numerator and then divide accordingly
    for each in movies_rated_by_test_user:
        if each in train_data_for_user and np.fromstring(train_data_for_user[each], dtype=np.float, sep=" ")[0] != mean_vote_train_user and (np.fromstring(all_movies_rated_by_test_user[each], dtype=np.float, sep=" "))[0] != mean_vote_test_point:
            numerator += (np.fromstring(all_movies_rated_by_test_user[each], dtype=np.float, sep=" ")[0] - mean_vote_test_point) * (
                np.fromstring(train_data_for_user[each], dtype=np.float, sep=" ")[0] - mean_vote_train_user)
            denominator_sum_1 += (np.fromstring(all_movies_rated_by_test_user[each], dtype=np.float, sep=" ")[0] - mean_vote_test_point) ** 2
            denominator_sum_2 += (np.fromstring(train_data_for_user[each], dtype=np.float, sep=" ")[0] - mean_vote_train_user) ** 2
        else:
            return 0
    return numerator / float(math.sqrt(denominator_sum_2 * denominator_sum_1))


def find_output(data, test_user, test_movie_id, test_user_id):
    """
    This function is used to find the output for the given user
    :param data: The test data
    :param test_user: The test user dict
    :param test_movie_id: The test movie id
    :param test_user_id: The test user id
    :return: The value of the predicted value
    """
    mean_vote_train_data = train(data)
    predicted_rating = test(data, test_user, mean_vote_train_data, test_movie_id, test_user_id)
    return data, predicted_rating

def convert_string_to_int(value):
    """
    This function is used to convert the string to int
    :param value: string
    :return: converted int
    """
    return np.fromstring(value, dtype=np.float, sep=" ")[0]