# @Time    : 2022/7/31 16:24
# @Author  : Huchao Wei

from slack_sdk import WebClient

class SlackInfoGetter(object):
    def __init__(self, app_token):
        self.app_token = app_token
        self.client = WebClient(token=self.app_token)

    def get_user_id_by_name(self, user_name):
        result = self.client.users_list()
        for item in result.data['members']:
            if item['name'] == user_name:
                return item['id']
        return ''


    def get_user_id_by_email(self, email):
        result = self.client.users_list()
        for item in result.data['members']:
            if email == '{}@veeva.com'.format(item['name']):
                return item['id']
        return ''
