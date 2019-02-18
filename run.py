import datetime
now = datetime.datetime.now()

users_list = [{"username": "Harun", "password": "sensei", "role": "admin"}]
comments = []
initial_message = "Are you happy?"

class Comments():
	def __init__(self):
		self.users = users_list
		#self.username = login_func

	def new_comment(self):
		author = input("Enter username: ")
		comment_id = input("Enter password: ")
		message = input("Enter message: ")    

		comment = {"author": author,
				"comment_id": len(comments)+1,
				"comment": message,
				"timestamp": now.strftime("%Y-%m-%d %H:%M")}    

		print(comment)
		comments.append(comment)
		return True


class UserLogin():
	def login_func(self):
		log = input("Enter username: " )
		password= input("Enter password: " )

		for user in users_list:
			if user["username"] == log:
				if user["password"] == password:
					username = log
					print("You have logged in Succesfully")
					return Comments().new_comment()

			else:
				print ("Log in Unsuccessful")




if __name__ == '__main__':
	UserLogin().login_func()
