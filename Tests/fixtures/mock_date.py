"Fixtures for testing"

def data_raw_tsv() -> dict:
    """
    Data raw to mock
    :return: Dictionary with data
    """
    data = {
        'unit,sex,age,geo\time': ['YR,F,Y1,AL','YR,F,Y1,AL','YR,F,Y1,PT'],
        '2021': ['79.4e','79.6','79.6'],
        '2022': ['79.4e','79.6','79.6'],
        '2023': ['83.2 ','79.6','79.6']
    }
    return data

def data_tabular() -> dict:
    """Data in tabular form"""
    data = {
        'unit': ['YR','YR','YR','YR','YR','YR','YR','YR','YR'],
        'sex': ['F','F','F','F','F','F','F','F','F'],
        'age': ['Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1'],
        'geo\time': ['AL','AL','PT','AL','AL','PT','AL','AL','PT'],
        'year': ['2021','2021','2021','2022','2022','2022','2023','2023','2023'],
        'life_expectancy': ['79.4e','79.6','79.6','79.4e','79.6','79.6','83.2 ','79.6','79.6']
    }
    return data

def data_with_floats() -> dict:
    """Data with floats"""
    data = {
        'unit': ['YR','YR','YR','YR','YR','YR','YR','YR','YR'],
        'sex': ['F','F','F','F','F','F','F','F','F'],
        'age': ['Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1'],
        'geo\time': ['AL','AL','PT','AL','AL','PT','AL','AL','PT'],
        'year': ['2021','2021','2021','2022','2022','2022','2023','2023','2023'],
        'life_expectancy': [79.4,79.6,79.6,79.4,79.6,79.6,83.2,79.6,79.6]
    }
    return data

def data_loaded() -> dict:
    """Data loaded"""
    data = {
        'unit': ['YR','YR','YR','YR','YR','YR','YR','YR','YR'],
        'sex': ['F','F','F','F','F','F','F','F','F'],
        'age': ['Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1','Y1'],
        'region': ['AL','AL','PT','AL','AL','PT','AL','AL','PT'],
        'year': ['2021','2021','2021','2022','2022','2022','2023','2023','2023'],
        'life_expectancy': [79.4,79.6,79.6,79.4,79.6,79.6,83.2,79.6,79.6]
    }
    return data

def data_expect() -> dict:
    """
    Data expected to mock
    :return: Dictionary with data prepared mocked
    """
    data = {
        'unit': ['YR','YR','YR'],
        'sex': ['F','F','F'],
        'age': ['Y1','Y1','Y1'],
        'region': ['PT','PT','PT'],
        'year': [2021,2022,2023],
        'value': [79.6,79.6,79.6]
    }
    return data
