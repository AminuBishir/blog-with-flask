import pytest

#create fixtures common to User and a Blog
@pytest.fixture(scope='module')
def user_name():
	return 'sadarwa'

@pytest.fixture(scope='module')
def password():
	return '123'
@pytest.fixture(scope='module')
def create_date():
	return '2019-11-28'
@pytest.fixture(scope='module')
def post_id():
	return '3'
@pytest.fixture(scope='module')
def email():
	return 'aminubishir@gmail.com'