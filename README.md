## 1 创建Slack APP并配置

https://api.slack.com/apps?new_app=1&ref=bolt_start_hub

### 1.1 配置Token Scopes

在`OAuth & Permissions`中找到`Bot Token Scopes`

选择以下两个权限:

1. `incoming-webhook`, Gitlab Webhook给Slack发送消息的权限
2. `chat:write`, 脚本给Slack发消息的权限


### 1.2 Install to Workspace

可以`OAuth & Permissions`中找到`OAuth Tokens for Your Workspace`点击`Install to Workspace`

选择安装到Workspace后, 在跳转回来的地址可以找到 `Bot User OAuth Token`

### 1.3 获取Webhook URL

在`Incoming Webhooks`中找到`Webhook URL`

## 2 给Slack Channel发送消息

在Gitlab的Settings中的integrations设置Slack notifications

主要填写以下信息:

1. 勾选启用集成
2. 勾选合并请求
3. 填写Webhook

## 3 给Reviewer的Slack发送消息

### 3.1 采用CI/CD触发的方式

在仓库中新增`.gitlab-ci.yml`

新增`DM.py`

### 3.2 服务接受Gitlab Webhook的方式

#### 3.2.1 配置Token Scopes

在`OAuth & Permissions`中找到`Bot Token Scopes`

选择以下权限:

1. `users:read`

#### 3.2.2 配置Gitlab

在Gitlab的Settings的Webhooks中新增一个Webhook, 配置可以为:

1. 网址
2. 勾选Merge Request

#### 3.2.3 启动服务

```bash
export BOT_USER_OAUTH_TOKEN=''
export FLASK_TOKEN=''
export FLASK_APP=app.py
flask run
```

