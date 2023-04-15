from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

"""
The has_match function will check if an item(user) has a match from the parameter(args). by default set to False and if a match (key, value) pair is found will be changed to True. used switch statement to implement matching requirements per key(field)
"""
def has_match(args, user):
    matched = False
    for key, value in args.items():
        match key:
            case "id":
                if value == user['id']:
                    matched = True
            case "name":
                if value.lower() in user['name'].lower():
                    matched = True
            case "age":
                if (user['age'] - 1) == int(value) or (user['age'] + 1) == int(value) or user['age'] == int(value):
                    matched = True
            case "occupation":
                if value.lower() in user['occupation'].lower():
                    matched = True
    return matched

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    #checks if args is empty and return the full USERS list
    if not args :
        return USERS
    else:
        #create an new list based on the items that matched the parameters using has_match() function
        result = [user for user in USERS if has_match(args, user)]

    return result

