#Exercise 1:
# users = {
#         "ben": {
#             "age": 23,
#             "role": "admin"
#         },
#         "sarah": {
#             "age": 24,
#             "role": "student"
#         }
#     }


# def get_user(username):

#     if username in users:

#         user = users[username]

#         return f"{username} is an {user["role"]} and is {user["age"]} years old"
    
#     return "User not found"

# def main():

#     print(get_user("ben"))
#     print(get_user("sarah"))

# main()


#Exercise 2:
# users = [
#     {"username": "ben","role": "admin"},
#     {"username": "sarah","role": "student"},
#     {"username": "alex","role": "admin"}
# ]

# def get_admins(users):

#     admins = []
   
#     for user in users:
#         if user["role"] == "admin":
#             admins.append(user["username"])
#     return {
#         "count": len(admins),
#         "admins": admins
#     }

# def main():
#     result = get_admins(users)
#     print(result)

# main()

#Exercise 3:
# users = {
#     "ben": {"age": 23, "role": "admin"},
#     "sarah": {"age": 24, "role": "student"}
# }

# def get_age(username):

#     if username in users:
#          user = users[username]

#          return users[username]["age"]
    
#     return "User not found"


# def main():
#      print(get_age("ben"))
#      print(get_age("sarah"))

# main()

#Exercise 4:
users = {
    "ben": {"age": 23, "role": "admin"},
    "sarah": {"age": 24, "role": "student"}
}

def get_age(username):

    user = users.get(username)
    
    if user is None:
        return {"error": "User not found"}
    
    return user["age"]

def main():
    print(get_age("ben"))
    print(get_age("name"))

main()

