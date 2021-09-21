from flask import Flask, request, jsonify, make_response
import query_db as db


def valid_user_data(data):
    var_in_data = ['username', 'name', 'gender', 'birthdate', 'password']

    # return error if len "data" !=5
    if len(data) != 5:
        return False

    # list comprehension to check if "data" contains username, name, gender, birthdate
    # if checkvar return list with len != 5 it means var username, or password, or name, or gender , or birthdate not in "data"
    check_var = [x for x in var_in_data if x in data]
    if len(check_var) != 5:
        return False

    return True


def register(data, created_date):

    # check if username is exists or not in database
    check_username = db.get_specified_user(data['username'])
    if check_username == 0:
        new_user = (data['username'], data['password'], data['name'],
                    data['gender'], data['birthdate'], created_date)
        insert_data = db.insert_user(new_user)
        if insert_data == False:
            return False

        return True
    else:
        return 'exists'


def get_users():
    users_data = db.select_all_users()
    return users_data
