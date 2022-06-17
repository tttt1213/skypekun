#! /usr/bin/env python3

from skpy import Skype
from getpass import getpass
import cgi
import codecs
import movepage
import json 

#JSON読み込み
settings = open('cgi-bin/settings.json' , 'r') 
settings = json.load(settings) 

#環境設定
mode = settings["PRODUCTION"]["test"]


print(mode["targetgroup"])
username = settings["PRODUCTION"]["PROFILE"]["username"]#ログインネーム
password = settings["PRODUCTION"]["PROFILE"]["password"]#ログインパスワード
sk = Skype(username,password)#ログイン

group_dict=settings["PRODUCTION"]["GROUPID"]#グループ辞書
user_dict = settings["PRODUCTION"]["USERID"]#ユーザー辞書


#グループ指定
targetgroupid = group_dict[mode["targetgroup"]]
channel = sk.chats.chat(targetgroupid,)

#メンション相手指定
targetusers = mode["targetusers"]
msg=""
for user in targetusers:
    msg +=  '<at id=\"{}\">{}</at> '.format(user_dict[user],user)

#本文指定
msg += mode["message"]

#送信
channel.sendMsg(msg,rich=True)

#index.html移動
movepage.html()


