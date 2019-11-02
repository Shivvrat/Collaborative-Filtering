from math import sqrt


def get_mean_absolute_error(actual_y, predicted_y):
    """
    The function calculates the MAE for the given values
    :param actual_y: These are the actual values of the variable
    :param predicted_y: These are the predicted values for the model
    :return: The MAE for given output values
    """
    absolute_error = 0
    for each_prediction in range(len(actual_y)):
        absolute_error += abs(actual_y[each_prediction] - predicted_y[each_prediction])
    return absolute_error / float(len(actual_y))


def get_root_mean_squared_error(actual_y, predicted_y):
    """
    The function calculates the RMSE for the given values
    :param actual_y: These are the actual values of the variable
    :param predicted_y: These are the predicted values for the model
    :return: The RMSE for given output values
    """
    squared_error = 0
    for each_prediction in range(len(actual_y)):
        squared_error += (actual_y[each_prediction] - predicted_y[each_prediction]) ** 2
    return sqrt(squared_error / float(len(actual_y)))
