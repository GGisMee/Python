# 61__zip_function
# aggregerar händelser från en samling(ex. List, tuple, sets, dictionary, etc)
def show(samling):
    if type(samling) == dict:
        for key,value in samling.items():
            print(key+" : "+value)
    elif type(samling) == list:
        for item in samling:
            print(item) 
# ---------------------

usernames = ["Dude", "GGisMee", "Kgamstedt"]
passwords = ["password", "112233", "abc123"]
login_date = ["1/1/2022", "1/2/2022", "1/3/2022"]

users = (zip(usernames, passwords))

print(type(users)) # egen typ för kombineringar

show(dict(users))

print()
print()

users_ = zip(usernames, passwords, login_date)
show(list(users_))

