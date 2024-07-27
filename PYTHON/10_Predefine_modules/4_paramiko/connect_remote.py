'''
1. Praramiko module is used to do operations on remote machine.
2. used to run commands on remote host 
3. copy file from local to remote and remote to local.
1. To install Praramiko module ==> 
      python -m pip install paramiko
'''
import paramiko

# To create ssh object
ssh = paramiko.SSHClient()

## To Add unknown host automaticllay
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# To create a connection on remote machine
ssh.connect('hostname', username='Admin', password='Admin123')

# To run commnd on remote host 
stdin, stdout, stderr = ssh.exec_command('mkdir TODAY')

## To get command output
print(' \n stdout is ::', stdout.read())

## To get error message if any failures 
print(' \n stderr is ::', stderr.read())

## To write values at run time
stdin.write('YES')

ssh.close()

