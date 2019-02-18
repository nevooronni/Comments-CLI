import datetime
now = datetime.datetime.now()

from app.v1.models.models import User, user_list
users_list = [{"username": "Harun", "password": "sensei", "role": "admin"}]
comments = []
initial_message = "Are you happy?"

class Comments():

	def new_comment(self):

		author = input("Enter author name: ")
		comment = input("Enter message: ")    

		comment = User().save_user(author, comment, now)
		return comment

	def edit_comment(self):

		author = input("Enter new author name: ")
		comment = input("Enter new message: ")

		new_comment = User().edit(author, comment, now)
		return new_comment





class UserLogin():
	def login_func(self):
		log = input("Enter username: " )
		password= input("Enter password: " )

		for user in users_list:
			if user["username"] == log:
				if user["password"] == password:
					username = log
					print("You have logged in Succesfully")
					Comments().new_comment()
					Comments().edit_comment()
					print ("comment updated Succesfully!")

			else:
				print ("Log in Unsuccessful")




if __name__ == '__main__':
	UserLogin().login_func()
