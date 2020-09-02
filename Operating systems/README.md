# Basic commands for windows(powershell for now):  
###### home directory => C:\
1. `ls C:\` &#8594; lists all the files & folders in C:\ root folder  
2. `ls -Force C:\` &#8594; includes hidden files too in the previous list  
3. `Get-Help ls` &#8594; gets help(change ls with required parameter)  
4. `Get-Help ls -Full` &#8594; gets detailed help about ls  
5. `pwd` &#8594; print working directory  
6. `cd C:\user\Desktop` &#8594; change directory (path can be relative or absolute)  
7. `cd ..` &#8594; parent dir of current location (one level relative)
8. `cd ~\Desktop` &#8594; go to mentioned directory from anywhere  
9. `mkdir "my cool folder"` or ```mkdir my` cool` folder``` &#8594; make a directory( "\`" (backtick) is the escape character)  
10. `history` or **ctrl-R** &#8594; shows command history (start typing in case of ctrl-r shortcut method, it'll show the related previous commands.)
11. `clear` &#8594; clears the output on screen (does not clears from history)  
12. `cp mycoolfile.text C:\Users\tanmay\Desktop\` &#8594; copy the file to desktop (in this case)  
13. `cp *.jpg C:\Users\tanmay\Desktop\` &#8594; copies all the files with mentioned extension(* takes anything for name with .jpg in this case)  
14. `cp "my cool folder" C:\Users\tanmay\Desktop\ -Recurse -Verbose` &#8594; copies the specified folder along with all files inside and sub-folders  
> `-Recurse` &#8594; lists the contents of the directory and if there's any sub-directory, it lists their content too. hence copy all the files.  
> `-Verbose` &#8594; outputs one line for each file being copied showing its status  



# commands in Linux:  
1. `ls`/ &#8594; list files in current directory  
2. `ls --help` &#8594; gets help about ls(change ls with required parameter)  
3. `man ls` &#8594; gets same info like with `--help` but with a little more details
4. `ls -l /` &#8594; shows additional info about directory and files & folders in them (in the below order)  
> file permissions | no of links that file has | file owner & group | size | last modification | file/dir name  
5. `ls -la /` or `ls -l -a /` &#8594; `-a` flag shows all files including hidden ones
6. `pwd` &#8594; print working dir  
7. `cd ../documents` &#8594; navigate around (to documents dir here)  
8. `cd ~\Desktop` &#8594; go to mentioned directory from anywhere(press tab after pressing first letter to see recommendations from that name)  
9. `mkdir "my cool folder"` or `mkdir my\ cool\ folder` &#8594; make a dir (\\ is the escape character here)  
10. `history` or **ctrl-r** &#8594; presents command history  
11. `clear` &#8594; clears the output screen  
12. `cp mycoolfile.text ~/Desktop` &#8594; copy the file to desktop (in this case)  
13. `cp *.jpg ~/Desktop` &#8594; copies all the files with mentioned extension(* takes anything for name with .jpg in this case)  
14. `cp -r "my cool folder" ~/Desktop` &#8594; copies the specified folder along with all files inside and sub-folders  

# Tips for Linux  
###### root directory =>  
* /bin &#8594; essential binaries and programs like `ls` command(like `program files` dir in windows)  
* /etc &#8594; system configuration files  
* /home &#8594; personal dir, holds user docs, pics etc.(like `user` dir in windows)  
* /proc &#8594; contains info about currently running processes  
* /usr &#8594; contains user installed softwares  
* /var &#8594; systems logs and constantly changing files  
* `.filename` &#8594; "." is used to hide a file/dir  
