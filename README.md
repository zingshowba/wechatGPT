# wechatGPT
微信摸鱼神器：一个调用openAI_chatGPT接口的微信机器人

### 新建一个python项目并安装需要的库

#### pip3 install revChatGPT --upgrade

#### pip install itchat

### 配置你的openAI登录凭证

#### 第一种用邮箱和密码

config = {
     "email": "",
     "password": ""
 }

#### 如果不行就第二种
config = {
    "session_token": ""
}

#### token获取办法：

打开https://chat.openai.com/chat 并登录 >按一下F12 > 点到 Application 标签 > Cookies

![image](https://user-images.githubusercontent.com/39222460/206840255-7940339f-98b7-4732-8ec9-2ccaabf5b6d4.png)

复制图中的值 __Secure-next-auth.session-token > 复制到项目里
![image](https://user-images.githubusercontent.com/39222460/206840261-9ce0680f-abee-4535-8ad3-20ad348bcb0b.png)

### 直接运行程序，enjoy!

![image](https://user-images.githubusercontent.com/39222460/206840660-14ef46cd-ffb4-4478-91d8-e471fa5340a1.png)
