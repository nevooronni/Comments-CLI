from app.v1.models.models import User

def create_user(self, name, username, password):

	print("Enter first name")
	name = input()

	print("Enter username")
	username = input()

	print("Enter password")
	password = input()	

	new_user = User.save_user(name, username, password)
	return new_user

def login_user(self, username, password):

	print("Enter username")
	username = input()

	print("Enter password")
	password = input()

	login_user(username, password)

	return User.user_exists(username, password)