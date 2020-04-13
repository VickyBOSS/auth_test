from user_repos import UserRepos

email = input("enter ur email : ")
password = input("enter ur password : ")

user_repos = UserRepos() # UserRepo.__init__(user_repos)

user = user_repos.signInWithEmailAndPassword(email, password) # User / None
if user == None:
    print("You email or pass is wrong")
else :
    print("Congratulations ! You are signed in as {}".format(user.name))