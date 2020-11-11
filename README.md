# generic-ca


## 参考サイト
|||
|--|--|
|https://docs.djangoproject.com/en/3.1/|Django 3.1|
|https://channels.readthedocs.io/en/stable/index.html|Django Channels|
|https://github.com/xtermjs/xterm.js/|xterm.js|
|https://github.com/huashengdun/webssh|WebSSH|


## 環境
```bash
$ sw_vers
ProductName:    Mac OS X
ProductVersion: 10.15.7
BuildVersion:   19H15

$ source ./env/bin/activate
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
- python 追加module
```bash
$ pip install websockets==8.1
```

|Path||
|--|--|
|[xteam_sample/sample1.html](xteam_sample/sample1.html)|最も簡単なxterm.js|
|[xteam_sample/sample2.html](xteam_sample/sample2.html)|key入力を受け付けるxterm.js|
|[websocket_sample/client.html](websocket_sample/client.html)|websocket確認用のclient html|
|[websocket_sample/websocket_server.py](websocket_sample/websocket_server.py)|websocket server|