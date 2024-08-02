class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following +=1
        user.followers += 1

user_1 = User("bob","0001")
user_2 = User("sammy","0002")

print(user_1.following)

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)


print(user_2.following)
print(user_2.followers)
