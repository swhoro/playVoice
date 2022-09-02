# playVoice

与 Voicemeeter Banana 搭配，用于游戏内放语音包

## Voicemeeter Banana 设置:

(这里只讲在游戏内放语音最基础的用法，如果想知道原理、其他用法，可以先看看这个入门：https://blog.csdn.net/klb5555/article/details/108340578)

### 方法一(简单，但游戏内无法说话，部分游戏不能调麦克风无法用这种设置):

![未标题-1](https://user-images.githubusercontent.com/34229589/188122150-b7d7fe8d-06d7-4ef3-89c2-48d1d038b067.png)

输出设备A1请选择 MME 开头设备，否则可能有奇怪的问题

图中红框所示，A1打上勾就可以自己听到语音包声音，B1打勾就可以把语音包声音输入进麦克风

进入系统的语音设置，不要让 Voicemeeter 抢占了你原本的输入输出设备的默认设置：

![未标题-1](https://user-images.githubusercontent.com/34229589/188123028-ff9ed6d7-fb39-4f25-958e-834aa61cb267.png)

![2](https://user-images.githubusercontent.com/34229589/188123205-2eb03621-a517-4617-aed0-89539458dcbf.png)

### 方法二(复杂一点，但是游戏内可以边放语音包边讲话，适用于所有游戏):

![3](https://user-images.githubusercontent.com/34229589/188124125-4bb43b96-06bd-4d48-8229-aff8ace37e95.png)

上面红框勾上自己的麦克风，下面红框去掉A1（否则二级内会传出麦克风），勾上B1（游戏内可以说话）

![image](https://user-images.githubusercontent.com/34229589/188124296-ef85b9dc-4716-4200-a791-5329e18f3508.png)

在系统声音设置的录制中把Voicemeeter Output设为默认设备和默认通信设备，注意是不带AUX的选项

## 软件设置：

### 我是小白：

前往https://github.com/swhoro/playVoice/releases，下载名为playVoice.exe的软件

下载完成后在与软件相同目录下新建voice文件夹，新建config.txt:

![image](https://user-images.githubusercontent.com/34229589/188124999-3eb72dfa-6bd8-4cc8-a9a0-e23ee93f1262.png)

voice文件夹下存放语音包，注意因为限制，**只能播放wav格式语音包**

config.txt用于存放配置，格式为 [快捷键] [语音包名字]:

![image](https://user-images.githubusercontent.com/34229589/188125401-b85bea8b-0700-4f0e-aaf5-cc8a149fc7a0.png)

运行软件，按提示播放语音，esc键退出

### 我会python:

下载源码，安装依赖

按上文配置voice文件夹、config.txt文件

直接运行脚本即可，-c 命令可用于手动选择语音播放设备(默认为 Voicemeeter Input)

按提示播放语音，esc键退出
