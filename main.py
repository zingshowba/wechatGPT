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
    # "email": "d@metaborder.com",
    # "password": "zingshowba000"
    #,
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jR764L_nbm9K7SDb.W8uy6vX0nz1mzNi9XYnTBE5-do6MlybYqcIwYNIJ-OH93zmb3Sn9lOWzmH4oYgOOLlbNjBMazd7laCoTJp8_GTdmHSaF8E4VAQzO0SP6KimsbpeHtCkP1YxJqkANAV5mTjmidCQQz6tv1UP89yHc_W9i87lGxDBNGxh4T8D6r6fojrk1P2bzH6HnZvRaW89J0J__eKCgqx5ShdyzW8mIbfd_Xe2cciRnhaG4lWLuT410o9h9ewdn9K23qOY23R70ZLFFsxLovEVGJZQkbbB7aYDUVDv2qIEbISYXF_xPKkeUpKpicdYwXF3h2MJijsOYXkLI0WcWYPZCXMVqwWh74NFJK3jLM2Sle6fVYO7a4sJFsrF8HNqoVuazZ2VuXdNDq1AglmcSpbN1k083CA0KAXR_N7zEvXO8KaDBbEH1N08jNTngBrZFPf4GD6sGJLML8PNS4N4KHBJQPf6MOXaH3NO4pvkPaSKXFMx8BKlC98WIudDmABUbA8DFCNm0CxCBMdE_420M_dnGsbCiSPOIB7oKfEQr0Be8FD_B1JswomRVViAX_CzKBTJbn0E18y-V1jbCaNFDshDugz7cPHGBx3nLNNGRHwKjCk4o77szazm-l8rqdnpQrEQskpRxja6A5MHf08dbf7gzfLPwZaPBHOZVCK_hkSkoO3avWQzyugx3s6QDlE3rePvqz1CWNNboXs0NqGJtGmCWhhNx8vrMUCivVNTIlKkFLyOecu-mGXKh7m-69PfRRQ6LyIH-Rd1U3nY3wlAJmW9RZI55W4SspCa1jhR2p-jRGsnTmRtKzMrvgm4WrIlHlSjRYZ4tyWDuImOp4TbfRgdyvIdIG4ONdSjHrBL3157Chn8PVdKLVETLArEdQGTUhjxrAmLY79608gThrcGKKmYpyWUbaWWZhdX68alY2oG8xBi81RFg6twUWPyr3EgtJWBSAp7kPHspoaGqQq2E_0hZfcsnau1s2YC2xNHgRaL9TrVgmTmRvxRoMFrm-bsAM-hUggfn5o_iR3X4NihZNn34dlbHhcLWwiqP4E-XncuOK1yfYPQQR32bvsaTGgEC5MaCWOIzMrPXHG-oaNWGWVlNTGg0y_rc_QOpXBGwB4RWLvdkeAnej1RwC8d-pnzL1geNcoP2hFoiUtpiBpnov8fvSxDxbU2PBYOR8cdPOjx_kYfVCgquKVzeLniG4-iPbZdF9JO8n9HFFNYKgQw-BxIpZw7V1AlH2qKsbhoMKN38LBzpFSrfgIrQz28lZw-ALPRnmkYHpSKe3fvplGInogcJDH_duG1Z45NIVkejdq4uQZDPv_nh85yJm4BsGW4G1sNZR2wVWM29w8w_2232f-hCkJb6hHAMw6xVgNDNzj5OnhT4BVbilrY604X2qj2FeZ_bjgnkWxPY07kt99tr8ZNv8pRHXb9S5HaZWizxe2HwQ7OywffWuItbebVnhem3QwrdaEGxLgRQp8h3wWdbQpTZzJf1F_dFTEP9VazMknw853YtK7WFOqtzciJlIW4pjPshn-skDydrN6qcAiZiYugjrnQZa9lWWfnfVPpiqmPQd_Sa6HER2mJc8BXeHVMhTF9bmH4dH3FHfiRdIwjE-UOxhZOHbLL-ib0S6gn_lsNiLWUoel6wVdXh0EhFyKf2RmhAn17j5xAuaGnKEoBEfq7WgSjujDw9x2uk8k5Y7d48beTSGHKD43xJ-ftKnkvQPFfLebLCwog5ww7lMnj84xLkRl_AmyEwuHORKSI1P_A5aC30Z3tJEfQJPny05suzhjRqhNJ51_FJNFfyjsXNICmTHkEZr1m-39QmQtUOXVh2Lj7dmhVFi1MIGy2zN8cBR_GNVvyYaQEv41lALJEjoYbS-eYFqqEznOkHe19zu-v4Z047U5aKjxl3ZtYB5Z1ACw-mhKmH_QWwwiXn_bVL1Lxf0DQzRAspwQa_KDAhGVBtx8rulo0r0hriinc_z0mVDr3lwbmWizbs6lGrU6bZlxwJsthgizxdlVABeN3an1uhakLGtcEA7zx7vxP7mTNrtbYLIjlnGy7JH6hSxJYnlUaK_YwdtObnTnMeBCZuTC5sdwBI3IOxpPlwo39vuEv1Y1fnpccIddwVjna3SRhlgEXINHLjQ4xDphfTsUQUWvC6Aejvv-YB7IT35aYxsJmeJYxUpeuf7Mr95iivBNGup9hYGymqvAqzPEXuvRdE6TVc-mo9jYoTImxlf-VSd14u1pzBnUQDKSqOyPZNj18R5ytmDEa2BjCt3ZNaan3BKq75okDv5tT9sHgtKjy_C6-da27-zXwHwDhlLG9XxyqhL87gyKvIqSjvRjkITw.icPdJHtAx7YCq14TGSE6RA"
    # Deprecated. Use only if you encounter captcha with email/password
    #"proxy": "<HTTP/HTTPS_PROXY>"
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
