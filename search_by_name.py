import config

api = config.api

q = "kai"
response = api.search_users(q=q, count=20)
for user in response:
    print(user.id, user.screen_name)
    print(user.name, user.followers_count)