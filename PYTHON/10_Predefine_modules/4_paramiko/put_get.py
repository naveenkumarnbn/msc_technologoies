import paramiko

# To create ssh object
ssh = paramiko.SSHClient()

## To Add unknown host automaticllay
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# To create a connection on remote machine
ssh.connect('hostname', username='Admin', password='Admin123')

## Create FTP object to copy file from local to remote and remote to local
ftp = ssh.open_sftp()

## Copy file from remote machine to local machine
ftp.get('/root/RRR.py', r'C:\modules\paramiko\RRR.py')

## Copy file from local machine to remote machine
ftp.put(r'C:\modules\paramiko\RRR.py', '/root/RRR.py')

# close ftp and ssh connections
ftp.close()
ssh.close()


