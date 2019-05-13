import numpy as np


def fit_ridge_regression(X, Y, l=0.1):
    """
    :param X: A numpy matrix, where each row is a data element (X)
    :param Y: A numpy vector of responses for each of the rows (y)
    :param l: ridge variable
    :return: A vector containing the hyperplane equation (beta)
    """
    # TODO, fill ridge regression part
    X, Y = np.array(X), np.array(Y)
    beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
    return beta


def get_data(df):
    """
    :param df: all apartment information in DataFrame
    :return: X, Y, where X(each row is a data element) is matrix and Y(response vector)
    """
    X, Y = [], []
    for _, datum in df.iterrows():
        x, y = featurize(dict(datum))
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)
dfkjkdfjbdkbj

def featurize(apartment):
    """
    :param datum: single house information in dict
    :return: (x, y) tuple, where x is a numpy vector, and y is a number
    """
    volume = apartment["area"] * apartment["ceiling_height"]
    if apartment["district"] == "Center":
        z = 1
    else:
        z = 0
    u = apartment["floor"] / apartment["max_floor"]
    k= apartmen["area"] / apartment["num_rooms"]
    return np.array([1, apartment["area"], apartment["num_rooms"], volume, z,u,k]), \
           apartment['price']

