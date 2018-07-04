import pytest

from webproject.app import create_app


@pytest.fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once
    because the decorator specifies a "session: scope. So it
    is executed once at the start of a test session to set up
    the environment with test settings.

    :return:  Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
