import logging
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
import sys
import os

from DM_Users import SlackInfoGetter

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.

slack_app_token = sys.argv[1]

info_getter = SlackInfoGetter(app_token=slack_app_token)

logger = logging.getLogger(__name__)


assginees = os.environ.get('CI_MERGE_REQUEST_ASSIGNEES', '')
project, merge_id = os.environ.get('CI_OPEN_MERGE_REQUESTS', '').split('!')
print(assginees)
print(os.environ.get('CI_OPEN_MERGE_REQUESTS', ''))
assginees = [x.replace('and', '').strip() for x in assginees.split(',')]


text = '您有新的MR需要Review哦! https://gitlab.veevadev.com/{}/-/merge_requests/{}'.format(project, merge_id)
print(text)
for assignee in assginees:
    result = info_getter.client.chat_postMessage(
        channel=info_getter.get_user_id_by_name(assignee),
        text=text
    )
    logger.info(result)
