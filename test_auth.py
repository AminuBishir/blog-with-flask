from auth import *
import pytest

#set user_id fixture
@pytest.fixture(scope='module')
def user_id():
	return 'my_id'

#set user_name fixture
@pytest.fixture(scope='module')
def user_name():
	return 'my_name'
	
'''GIVEN: set_secure_val function
	WHEN: new secure val is set
	THEN: check that the val is used in creating the secure val and that encryption was made'''
def test_secure_val(user_id):
	secure_val = set_secure_val(user_id)
	secured = secure_val.split('|')
	assert secured[0] == user_id
	assert secured[1] != user_id

'''GIVEN: check_secure_val function
	WHEN: a secure_val is being checked for encryption
	THEN: check that user_id has a valid secure_val'''
def test_check_secure_val(user_id):
	secured = set_secure_val(user_id)
	is_secured = check_secure_val(secured)
	assert is_secured == True
	
'''GIVEN: a salt for password encryption
	WHEN: a custome length of the salt is supllied
	THEN: check that the length is same as the custome one'''
def test_custom_salt():
	salt = make_salt(20)
	assert len(salt)==20
	
'''
GIVEN: a salt for password encryption
WHEN: no salt length is given
THEN: check that salt is created with default length 5'''
def test_default_salt():
	salt = make_salt()
	assert len(salt) == 5
	
