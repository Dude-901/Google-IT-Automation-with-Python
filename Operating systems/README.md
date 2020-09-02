# Basic commands for windows(powershell for now):  
###### home directory => C:\
1. `ls C:\` &#8594; lists all the files & folders in C:\ root folder  
2. `ls -Force C:\` &#8594; includes hidden files too in the previous list  
3. `Get-Help ls` &#8594; gets help(change ls with required parameter)  
4. `Get-Help ls -Full` &#8594; gets detailed help about ls  


# commands in Linux:  
1. `ls`/ &#8594; list files in current directory  
2. `ls --help` &#8594; gets help about ls(change ls with required parameter)  
3. `man ls` &#8594; gets same info like with `--help` but with a little more details
4. `ls -l /` &#8594; shows additional info about directory and files & folders in them (in the below order)  
> file permissions | no of links that file has | file owner & group | size | last modification | file/dir name  
5. `ls -la /` or `ls -l -a /` &#8594; `-a` flag shows all files including hidden ones


# Tips for Linux  
###### root directory =>  
* /bin &#8594; essential binaries and programs like `ls` command(like `program files` dir in windows)  
* /etc &#8594; system configuration files  
* /home &#8594; personal dir, holds user docs, pics etc.(like `user` dir in windows)  
* /proc &#8594; contains info about currently running processes  
* /usr &#8594; contains user installed softwares  
* /var &#8594; systems logs and constantly changing files  
* `.filename` &#8594; used to hide a file/dir  
