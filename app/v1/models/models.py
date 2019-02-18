users = []

class User:

	def __init__():

		self.user_list = users
	def save_user(self):

		new_user = {
		"name": name,
		"username": username,
		"password": password
		}

		self.user_list.append(new_user)
		return self.user_list

	def user_exists(self):

		for user in users:
			if user.username == username and user.password == password:
				return True