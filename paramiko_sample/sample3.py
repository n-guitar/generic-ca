# paramiko==2.7.2
from paramiko import SSHClient, AutoAddPolicy
import time

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(hostname='ip address',username='user',password='password',port=22)
channel = client.invoke_shell()
while not channel.recv_ready():
    time.sleep(0.1)


# login
buff = ''
resp = channel.recv(1024).decode('utf-8')
buff += resp
print(resp)

def send_command(cmd):
    buff = ''
    while not buff.endswith(']# '):
        channel.send(cmd + '\n')
        resp = channel.recv(1024).decode('utf-8')
        buff += resp
        print(resp)

send_command('uname -a')

client.close()
print('Connection closed.')
