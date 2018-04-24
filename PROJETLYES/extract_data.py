import requests
import json
BASE_URL = "https://graph.facebook.com/v2.12/"
TOKEN = "EAACEdEose0cBAJhyT1s1ue5GIaZAHnEhWBWabfSyIg6usN3XqbcRiK1NN0XZBIRWlFiYj4lZCrQFCbryVahXg8DRNtUNMqTwL7uqdWdrmP5OEEsVaGAZCpEd48yp2v1EJBGMwwKTQIUn8LSOyXdnlGunXqZBrfm4uRqlOnPRgykC6i5ZCBaZCITSSiVUpqm9Rm0wBToGn9mHAZDZD"

class ExtractData:
    def __init__(self, token):
        self.token = token


    def get_friends(self, userID):
        f_url = BASE_URL + userID + "/friends?access_token={}".format(self.token)
        r = requests.get(url=f_url)
        return r.json()


    def get_user(self, userID):
        f_url = BASE_URL + userID + "/?access_token={}".format(self.token)
        r = requests.get(url=f_url)
        return r.json()

    def get_likes(self, user_id):
        f_url = BASE_URL + user_id + "/likes?access_token={}".format(self.token)
        r = requests.get(url=f_url)
        return r.json()

    def get_posts(self, user_id):
        f_url = BASE_URL + user_id + "/posts?access_token={}".format(self.token)
        r = requests.get(url=f_url)
        return r.json()

    def get_graph_likes(self, user_id):
        list_likes = self.get_likes(user_id)['data'][:5]
        user_actual = self.get_user(user_id)
        print(user_actual)
        return_list = []
        lists = []
        for page in list_likes:
            l = self.get_likes(page["id"])['data'][:5]
            return_list.append({
                'id': page['id'],
                'name': page['name'],
                'like_pages': l
            })
        return_list.append({
            'id': user_actual['id'],
            'name': user_actual['name'],
            'like_pages': list_likes
        })
        print(json.dumps(return_list))
        return return_list


extra = ExtractData(token=TOKEN)

print(extra.get_likes("113822656146338"))