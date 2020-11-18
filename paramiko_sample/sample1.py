from paramiko import SSHClient, AutoAddPolicy

def sshFunc(hostname, username, password='pwd', port=22,):
    hostname = hostname
    username = username
    password = password
    port = port
    remote_command = 'cd /;ls -l'
    with SSHClient() as ssh:
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(remote_command)
        remote_command_result =[]
        # for line in stdout:
        #     remote_command_result.append(line)
        remote_command_result = stdout.read().decode()
        print(remote_command_result)

sshFunc(hostname='ip address',username='user',password='password',port=22)