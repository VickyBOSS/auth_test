from user import User
class UserRepos:
    users = [
        User("ashok", "ashok@gmail.com","11223344" ),
        User("bandu", "bandu@gmail.com","11223344"),
        User("chunilal", "chunilal@gmail.com","11223344")
    ]

    def __init__(self): # user_repos
        pass


    # userRepos = UserRepos()
    # userRepos.signInWithEmailAndPassword("bandu@gmail.com","11223344")


    def signInWithEmailAndPassword(self, email, password):

        # email = "bandu@gmail.com"
        # password = "11223344"

        currentUser = None

        for user in self.users: # # user_repos.users
            print(user.name)
            if user.email== email and user.password == password:
                currentUser = user;
                break

        # for loop 1st time
        #    user = User("ashok", "ashok@gmail.com","11223344" )
        #    if "ashok@gmail.com"=="bandu@gmail.com"

        # for loop 2nd time
        #   user = User("bandu", "bandu@gmail.com","11223344")
        #    if "bandu@gmail.com"=="bandu@gmail.com"

        return currentUser;
