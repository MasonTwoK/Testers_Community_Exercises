import pytest


@pytest.fixture(scope="function")
def function_scope():
    print("setup function scope")
    yield
    print("teardown function scope")


@pytest.fixture(scope="class")
def class_scope():
    print("setup class scope")
    yield
    print("teardown class scope")


@pytest.fixture(scope="module")
def module_scope():
    print("setup module scope")
    yield
    print("teardown module scope")


@pytest.fixture(scope="package")
def package_scope():
    print("setup package scope")
    yield
    print("teardown package scope")


@pytest.fixture(scope="session")
def session_scope():
    print("setup session scope")
    yield
    print("teardown session scope")
