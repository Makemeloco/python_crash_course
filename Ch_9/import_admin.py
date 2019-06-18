from Privileges import Admin


user = Admin('emma', 'stone', 26, 89595554455)

user.describe_user()
user.greet_user()
user.privileges.show_privileges()
