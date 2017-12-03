#coding=utf8
import requests
import itchat

from itchat.content import *

itchat.auto_login()

@itchat.msg_register
def general_reply(msg):
    return 'I received a %s' % msg['Type']

@itchat.msg_register(TEXT)
def text_reply(msg):
    return '因为工作的关系，曾面对无数好友呼叫不能回应，最痛苦的事莫过于此。如果给我一次机会，我要说三个字：我离开。如果一定要给这三个字加个期限，我希望是：一会儿！' 


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动

itchat.auto_login(hotReload=True)
itchat.run()
