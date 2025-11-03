from fuzzywuzzy import fuzz
from types import SimpleNamespace
import fetch_database as fetch_database

def get_closest_match(table_names, search_term):
    best_match = None
    highest_score = -1
    for table_name in table_names:
        score = fuzz.ratio(table_name.lower(), search_term.lower())
        if score > highest_score:
            highest_score = score
            best_match = table_name
    return best_match

def preprocess(conn, data):
    # x_axis, y_axis, [x_filter], [y_filter], multiplier
    table_names = conn.get_table_names()
    x_axis_dataset = conn.fetch_data(get_closest_match(table_names, data.x_axis))
    y_axis_dataset = conn.fetch_data(get_closest_match(table_names, data.y_axis))
    x_filter_datasets = [conn.fetch_data(get_closest_match(table_names, filter_name)) for filter_name in data.x_filters]
    y_filter_datasets = [conn.fetch_data(get_closest_match(table_names, filter_name)) for filter_name in data.y_filters]
    multiplier_dataset = conn.fetch_data(get_closest_match(table_names, data.multiplier))