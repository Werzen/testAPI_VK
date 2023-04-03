import pytest
import os
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_dotenv_fixture():
    load_dotenv()


@pytest.fixture(scope="session")
def get_general_params():
    params = {
        "access_token": os.getenv("SERVICE_ACCESS_KEY"),
        "v": os.getenv("GLOBAL_VERSION_API_VK"),
    }
    return params
