#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/2 11:25
# @Author  : Huchao Wei

import os
from slack_sdk import WebClient
from flask import Flask
from flask import request

app = Flask(__name__)

slack_token = os.environ["BOT_USER_OAUTH_TOKEN"]
flask_token = os.environ["FLASK_TOKEN"]

client = WebClient(token=slack_token)
user_data = {}


def get_user_id_by_name(user_name):
    if user_name not in user_data:
        for item in client.users_list().data['members']:
            user_data[item['name']] = item['id']
    return user_data[user_name]


@app.route("/slack/push/<token>", methods=["POST"])
def post_install(token):
    if token != flask_token:
        return '403'
    data = request.get_json()
    text = '您有新的MR需要Review哦! {}'.format(data['object_attributes']['url'])
    for assignee in data['assignees']:
        client.chat_postMessage(channel=get_user_id_by_name(assignee['username']), text=text)
    return '200'
