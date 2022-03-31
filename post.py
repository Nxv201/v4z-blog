import requests

class Post:

    def __init__(self):
        self.all_posts = self.get_all_post()

    def get_all_post(self):
        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(blog_url)
        all_post = response.json()
        return all_post

    def get_post(self, id):
        for post in self.all_posts:
            if post["id"] == id:
                return post
