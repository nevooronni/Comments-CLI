user_list = []

class User:

	def __init__(self):

		self.users = user_list

	def save_user(self, author, comment, now):

		comment = {"author": author,
				"comment_id": len(self.users)+1,
				"comment": comment,
				"timestamp": now.strftime("%Y-%m-%d %H:%M")}    

		print(comment)
		self.users.append(comment)
		return self.users


	def edit(self, author, comment, now):

		comment = {"author": author,
				"comment_id": len(self.users)+1,
				"comment": comment,
				"timestamp": now.strftime("%Y-%m-%d %H:%M")}
		print(comment)
		self.users.append(comment)
		return self.users