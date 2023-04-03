import pytest
import os
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def get_general_params():
    load_dotenv()
    params = {"access_token": os.getenv('SERVICE_ACCESS_KEY'),
              "v": os.getenv('GLOBAL_VERSION_API_VK')}
    return params
