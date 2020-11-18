# generic-ca


## 参考サイト
|URL||
|--|--|
|https://docs.djangoproject.com/en/3.1/|Django 3.1|
|https://channels.readthedocs.io/en/stable/index.html|Django Channels|
|https://github.com/xtermjs/xterm.js/|xterm.js|
|https://github.com/huashengdun/webssh|WebSSH|


## 動作確認済環境
```bash
$ sw_vers
ProductName:    Mac OS X
ProductVersion: 10.15.7
BuildVersion:   19H15

$ python --version
Python 3.7.3
```

## 以下本source code上に含まれているため不要
- node.jsでxterm.jsをインストールしている
- node_modules folderを参照
```bash
$ npm install --save xterm
$ npm install --save xterm-addon-attach
$ npm install --save xterm-addon-fit
$ npm install --save xterm-addon-search
$ npm install --save xterm-addon-web-links
```
## 以下pip installを行うか、[setup.sh](setup.sh)を実行する
- python 追加module
```bash
$ pip install websockets==8.1
$ pip install paramiko==2.7.2
$ pip install scp==0.13.3
```

|No|Path||
|---|--|--|
|1|[xteam_sample/sample1.html](xteam_sample/sample1.html)|最も簡単なxterm.js|
|2|[xteam_sample/sample2.html](xteam_sample/sample2.html)|key入力を受け付けるxterm.js|
|3|[websocket_sample/client.html](websocket_sample/client.html)|websocket確認用のclient html|
|4|[websocket_sample/websocket_server.py](websocket_sample/websocket_server.py)|websocket server|
|5|[paramiko_sample/sample1.py](paramiko_sample/sample1.py)|簡単なparamiko 単一commandを実行する|
|6|[paramiko_sample/sample2.py](paramiko_sample/sample2.py)|簡単なparamikoとscpを行う|
|7|[paramiko_sample/sample3.py](paramiko_sample/sample3.py)|対話型を行うparamiko|
|8|[websocket_sample/websocket_ssh_server.py](websocket_sample/websocket_ssh_server.py)|websocketで待受し、paramikoで自信したメッセージをssh先に送信する|
|9|[xteam_sample/sample3.html](xteam_sample/sample3.html)|No8に対してwebsocket通信し、terminalからのcommandを送信する。</br> 残念ながらEnterを2回押下しないとデータを表示できない|