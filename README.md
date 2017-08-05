# Pepper相关应用的开发

本教程根据ALDebaran官方文档进行完善，同时在学习的过程中的问题，进行分享

## 入门

### 下载和安装ALDebaran开发工具
1. 确保您的NAO已经在ALDebaran Community用户账户上注册。
2. 访问ALDebaran社区网站的软件资源
3. 使用您的ALDebaran Community用户账户凭据登录显示所有可用的软件
### Hello word!
- 确保您有一个可以使用的机器人
- 确保您的计算机上安装了Python和Python SDK

1. 打开您的编辑器，我这里使用的是Visual Studio Code
2. 新建一个文件
3. 复制以下代码
```markdown
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech","<IP of your robot>",9559)
tts.say("Hello,world!")
```
4. 把<IP of your robot>替换成您的机器人IP
  如果您不知道您的机器人IP，请按机器人胸前的按钮
5. 保存文件
6. 运行
- 结果
你的机器人说"Hello,world!"
- 它如何工作
此脚本使用ALTextToSpeech模块。ALTextToSpeech是Naoqi关于说话方面的模块。
```markdown
from naoqi import ALProxy
导入模块ALProxy
```

```markdown
tts = ALProxy("ALTextToSpeech","<IP of your robot>",9559)
创建一个名为tts的对象，该对象发送到Naoqi
- tts是我们给对象实例的名称
- ALProxy()是一类对象，允许您访问所有的模块
- ALTextToSpeech是我们想要使用的Naoqi模块名称。
- 还指定了机器人的IP和端口（9559）
```
```markdown
tts.say("Hello,world!")
- tts是我们使用的对象
- say()是方法
- "Hello Word!"是参数
```
