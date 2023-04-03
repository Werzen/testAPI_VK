import pytest
import os

from client import APIClient
from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages
from src.schema.post import POST_SCHEMA_GET_USERS


@pytest.mark.parametrize(
    "params, result",
    [
        (
            {"user_ids": "79331389"},
            {
                "response": [
                    {
                        "id": 79331389,
                        "first_name": "Alexey",
                        "last_name": "Chistov",
                        "can_access_closed": True,
                        "is_closed": False,
                    }
                ]
            },
        ),
        ({"user_ids": "7933138e9"}, {"response": []}),
        (
            {"user_ids": "79331389", "fields": "city,bdate"},
            {
                "response": [
                    {
                        "id": 79331389,
                        "bdate": "4.1.1990",
                        "city": {"id": 71, "title": "Kostroma"},
                        "first_name": "Alexey",
                        "last_name": "Chistov",
                        "can_access_closed": True,
                        "is_closed": False,
                    }
                ]
            },
        ),
    ],
    ids=["correct user_id", "incorrect user_id", "correct user_id with additional fields"],
)
def test_users_get(params, result, get_general_params, monkeypatch):

    # create mock
    def mock_get_users(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        parameters = args[1]
        if parameters.get('user_ids') == str(79331389) and parameters.get('fields') == "city,bdate":
            return MockResponse({
                "response": [
                    {
                        "id": 79331389,
                        "bdate": "4.1.1990",
                        "city": {"id": 71, "title": "Kostroma"},
                        "first_name": "Alexey",
                        "last_name": "Chistov",
                        "can_access_closed": True,
                        "is_closed": False,
                    }
                ]
            }, 200)
        elif parameters.get('user_ids') == str(79331389):
            return MockResponse({
                "response": [
                    {
                        "id": 79331389,
                        "first_name": "Alexey",
                        "last_name": "Chistov",
                        "can_access_closed": True,
                        "is_closed": False,
                    }
                ]
            }, 200)
        elif parameters.get('user_ids') == "7933138e9":
            return MockResponse({"response": []}, 200)
        return MockResponse(None, 404)
    monkeypatch.setattr('client.APIClient.get_users', mock_get_users)

    # load data
    request = APIClient(os.getenv('GLOBAL_URL')).get_users(params | get_general_params)
    received_users = request.json()

    # tests
    assert request.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    validate(received_users, POST_SCHEMA_GET_USERS)
    assert sorted(received_users.items()) == sorted(result.items()), GlobalErrorMessages.WRONG_VALUE_FIELDS.value
