from revChatGPT.revChatGPT import Chatbot
import itchat
from itchat.content import *


#配置你的openAI登录凭证

#第一种用邮箱和密码

# config = {
    # "email": "",
    # "password": ""
# }

# 如果不行就第二种
config = {

    "session_token": ""
}

# 初始化
chatbot = Chatbot(config, conversation_id=None)


#监听微信收到的文字信息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    # returns {'message':message, 'conversation_id':self.conversation_id, 'parent_id':self.parent_id}
    msg_content = msg.text
    print(msg_content)
    #将微信收到的信息提交到openAI接口
    response = chatbot.get_chat_response(msg_content, output="text")
    print(response["message"])
    #将接收到的答案格式化并通过转发给自己
    msg.user.send(response["message"])
    msg.user.send("元数边界测试接口~")

#微信登录并监听
itchat.auto_login(True)
itchat.run(True)
