import data
import sender_stand_request

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client(kit_body, get_new_user_token())
    assert response.status_code == 201

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client(kit_body, get_new_user_token())
    assert  response.status_code == 400

def test_1_kit_name_with_1_letter():
    new_kit_body = get_kit_body(data.with_one_letter)
    positive_assert(new_kit_body)

def test_2_kit_name_with_511_letters():
    new_kit_body = get_kit_body(data.with_511_letters)
    positive_assert(new_kit_body)

def test_3_kit_name_with_0_letter():
    new_kit_body = get_kit_body(data.with_0_letters)
    negative_assert_code_400(new_kit_body)

def test_4_kit_name_with_512_letters():
    new_kit_body = get_kit_body(data.with_512_letters)
    negative_assert_code_400(new_kit_body)

def test_5_kit_name_with_special_characters():
    new_kit_body = get_kit_body(data.with_special_characters)
    positive_assert(new_kit_body)

def test_6_kit_name_allowed_with_a_space():
    new_kit_body = get_kit_body(data.with_a_space)
    positive_assert(new_kit_body)

def test_7_kit_name_with_numbers():
    new_kit_body = get_kit_body(data.with_numbers_str)
    positive_assert(new_kit_body)

def test_8_without_the_kit_name_parameter():
    new_kit_body = get_kit_body(data.without_any_parameters)
    negative_assert_code_400(new_kit_body)

def test_9__kit_name_with_numbers():
    new_kit_body = get_kit_body(data.with_numbers)
    negative_assert_code_400(new_kit_body)
