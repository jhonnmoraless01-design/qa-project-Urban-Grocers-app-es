import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         headers = data.headers,
                         json = user_body)

def post_new_client(kit_body, auth_token):
    current_header = data.headers.copy()
    current_header["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = data.headers)