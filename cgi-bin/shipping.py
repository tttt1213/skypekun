from skpy import Skype
from getpass import getpass
import cgi
import codecs
import movepage

#本番ユーザー
myusername = 'mori@systemworks.co.jp'
mypassword = 'SystemWorks'

sk = Skype(myusername,mypassword)
groupid='19:0523eac33ce74ddf9e41ff98c2e3f7a5@thread.skype'#SWC_出荷グループID
channel = sk.chats.chat(groupid,)
Msg=""


#宮崎さん、中西さん、梱包にメンション
channel.sendMsg('<at id="8:live:.cid.8d6854d7c89c09a1">miyazaki</at> <at id="8:live:.cid.3c7cbe1df3af80b8"> nakanishi </at> <at id="8:live:.cid.2f70515510ed9b39"> kompo </at> テスト完了品の準備ができました。 ', rich=True)

movepage.html()