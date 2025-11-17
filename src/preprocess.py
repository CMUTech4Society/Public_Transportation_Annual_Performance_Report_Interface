import shutil
import shlex
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

def preprocess(args):
    conn = DatabaseConnection();
    # x_axis, y_axis, [x_filter], [y_filter], multiplier
    table_names = conn.get_table_names()
    x_dataframe = conn.fetch_data(get_closest_match(table_names, args.x_axis))
    y_dataframe = conn.fetch_data(get_closest_match(table_names, args.y_axis))

    x_dataset = Dataset(args.x_axis, x_axis_dataframe)
    y_dataset = Dataset(args.y_axis, y_axis_dataframe)
    
    x_filters = []
    for x in args.x_filters:
        func = get_filter(x)
        x_filters.append(Filter(x, func))

    y_filters = []
    for y in args.y_filters:
        func = get_filter(y)
        y_filters.append(Filter(y, func))


    return PlotStruct(None, x_dataset, y_dataset, x_filters, y_filters, None)

def get_filter_func(f): # f="population > 500"
    if f is None: return None
    column, operator, value = shlex.split(f)
    table_names = conn.get_table_names()
    column = get_closest_match(table_names, column)

    match operator:
        case ">":
            operator = lambda a, b: a > b
            break
        case ">=":
            operator = lambda a, b: a >= b
            break
        case "<":
            operator = lambda a, b: a < b
            break
         case "<=":
            operator = lambda a, b: a <= b
            break
         case "=":
            operator = lambda a, b: a == b
            break
         case "!=":
            operator = lambda a, b: a != b
            break

    if value.replace('.', ' ', 1).isnumeric():
        return lambda row: operator(row.loc[column], float(value))
    else
        return lambda row: operator(row.loc[column], value)
