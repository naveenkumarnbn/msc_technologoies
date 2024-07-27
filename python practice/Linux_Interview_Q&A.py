## Linux online editor link
link-1 ==> https://linuxcontainers.org/lxd/try-it/
           https://www.tutorialspoint.com/execute_bash_online.php

# What is SSH command ?
    1. Using ssh command we can connect remote machine.
    2. Syntax:- ssh user_name@23.43.23.234

# What is SCP command ?
    1. Using scp command we can copy file from remote host to local and local to remote.
    ## Copy file form local host to remote host 
    scp local_file.txt uname@10.126.78.229:/home/logs/
    ## Copy file from remote host to local host
    scp uname@remote_host:remote_file_path local_dir

# Use of grep command ?
    1. The grep command which stands for “global regular expression print,” processes text line by line and prints any lines which match a specified pattern.
    2. The grep command is used to search text or searches the given file for lines containing a match to the given strings.
    ## Example # https://www.geeksforgeeks.org/grep-command-in-unixlinux/
    * grep sriram today.txt # To print which lines contains sriram word in today.txt
    * grep -o sriram today.txt # Tpo print only sriram word how many times occured in a today.txt

# Use of find command ?
    1. It can be used to find files and directories.
    ## Example # https://www.tecmint.com/35-practical-examples-of-linux-find-command/

# Use of chmod command ?
    1. The chmod command is used to change the permissions of files or directories..
    ## Example # https://www.geeksforgeeks.org/chmod-command-linux/
    4 stands for "read",
    2 stands for "write",
    1 stands for "execute", and
    0 stands for "no permission."
    * ==> To give all permissions recursively  
    Chmod 777 -R folder name
    * Read by owner only
        chmod 400 sample.txt 
    * Read by group only
        chmod 040 sample.txt 
    * Read by anyone
        chmod 004 sample.txt 
    * Write by owner only
        chmod 200 sample.txt 
    * Deny execute permission to everyone.
        chmod a-x sample.txt 
    * Allow read permission to everyone.
        $ chmod a+r sample.txt 
    * Make a file readable and writable by the group and others.
        $ chmod go+rw sample.txt 

# Use of ls command ?
    1. ls is a Linux shell command that lists directory contents of files and directories.
    ## https://www.geeksforgeeks.org/practical-applications-ls-command-linux/

# Use of ll or ls -l command ?
    1. shows file or directory, size, modified date and time, file or folder name and owner of file and its permission.

# Use of pwd commnad ?
    1. To know the current working directory

# Use of cp command ?
    1. cp stands for copy. This command is used to copy files or group of files or directory
    ## https://www.geeksforgeeks.org/cp-command-linux-examples/
    * recursive copying of directories.
        cp -R Src_directory Dest_directory

# Use of mv command ?
    1. mv stands for move. mv is used to move one or more files or directories from one place to another in file system like UNIX.
    ## https://www.geeksforgeeks.org/mv-command-linux-examples/

# Use of rm command ?
    1. rm stands for remove here. rm command is used to remove files and directories.
    * -r (Recursive Deletion): With -r(or -R) # TO remove recursively

# Use of ps command ?
    1. Linux provides us a utility called ps for viewing information related with the processes on a system which stands as abbreviation for “Process Status”. ps command is used to list the currently running processes and their PIDs along with some other information depends on different options
    ## https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/

# Use of AWK command ?
    1. Awk is a scripting language used for manipulating data and generating reports.
    ## Awk is a scripting language used for manipulating data and generating reports.
    *  ps aux | grep 'hpsum_service' | awk 'NR == 1' | awk '{print $2}'   --> To get value bases on column and based on row

# Use of hostory command ?
    1. history command is used to view the previously executed command

# Use of du commnad ?
    1. du command, short for disk usage, is used to estimate file space usage.
    2. The du command can be used to track the files and directories which are consuming excessive amount of space on hard disk drive.
    ## https://www.geeksforgeeks.org/du-command-linux-examples/

# Use of cat command ?
    1. Cat(concatenate) command is very frequently used in Linux. It reads data from the file and gives their content as output. It helps us to create, view, concatenate files.
    ## https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/

# What is vi editor ?
    1. The default editor that comes with the UNIX operating system is called vi (visual editor). Using vi editor, we can edit an existing file or create a new file from scratch. we can also use this editor to just read a text file.
    ## https://www.geeksforgeeks.org/vi-editor-unix/


# Do you have experience on Linux ?
    1. Yes, I have experience on linux. I have worked on all linux basic commands like...grep, find, chmod, ps, du...
    2. I have worked on redhat version 6.5

# How do you know the version in linux ?
    1. cat /etc/*release or  cat /etc/redhat-release

# How to konw IP address in linux ?
    1. Using ifconfig

# How do you know the host name in linux ?
    1. Using 'hostname' command

# How to get hidden files in linux ?
    1. Using ls -a 

# How do you create a directory in Linux ?
    1. Usind mkdir command

# How do you remove a directory in Linux ?
    1. Usind rmdir command

# How do you create a empty file in Linux ?
    1. Usind touch command
    ## example: touch file1.txt file2.txt

# How do you kill process in linux ?
    1. Using kill command 
    ## example : kill -9 9876(Proceess id )