import requests

BASE_URL = "https://graph.facebook.com/v2.12/"


class ExtractData:
    def __init__(self, token):
        self.token = token

    def get_friends(self, userID):
        f_url = BASE_URL + userID + "/friends?access_token={}".format(self.token)
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


my_token = "EAACEdEose0cBAJDFWZBLIcZBL6Nu0MTsrGtRFoaI4LiecVk5uKcpAYBkoj2KooG9S6cCdLtoCe6ankdLszJuZAo380xqIv2L4XNvAD2j5ZCxy4RV9tJL0S0qY2gIFHvnjqYug82hvVFjFPIE2BgzdHvRRTf3HrDq1FReaxXSQZC95tRrMndFbxbV4MfLBvY8ZD"
extra = ExtractData(token=my_token)

print(extra.get_posts("661094353948044"))
