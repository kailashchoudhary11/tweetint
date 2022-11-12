import config

class Twitter():
    userid : int
    username : str
    name : str
    api = config.api
    client = config.client

    def __init__(self, args):
        if args.userid:
            self.userid = args.userid
        if args.username:
            self.username = args.username
        if args.name:
            self.name = args.name
    
    def search_by_name(self):
        q = f"{self.name}"

        response = Twitter.api.search_users(q=q, count=20)
        for user in response:
            print(user.screen_name)
            # print(user.id, user.screen_name)
            # print(user.name, user.followers_count)
    
    def search_by_username(self):
        response = Twitter.client.get_user(username=self.username, user_fields=[
                                "profile_image_url", "description", "created_at", "location", "protected", "public_metrics", "url"])
        user = response.data
        self._print_user_details(user)

    def search_by_id(self):
        response = Twitter.client.get_user(id=self.userid, user_fields=[
                                "profile_image_url", "description", "created_at", "location", "protected", "public_metrics", "url"])
        user = response.data
        self._print_user_details(user)
    
    def _print_user_details(self, user):
        for key, value in user.items():
            key = str(key).replace("_", " ").capitalize()
            print(f"{key} - {value}")