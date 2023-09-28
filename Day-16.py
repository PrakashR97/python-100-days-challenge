class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user = User('Prakash', 123)
print(user.user_name)

user_1 = User("001","angela")
user_2 = User("002","jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




# user_1 = User()
# user_1.name = 'Prakash'
# user_1.id = 26

# user_2 = User()
# user_2.name = 'Emma'
# user_2.id = 30
