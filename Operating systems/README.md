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
15. `mv \blue_document.txt yellow_document.txt` &#8594; move command, used to rename file.  
16. `mv .\yellow_document.txt ~\Desktop` or `mv *_document.txt C:\Users\tanmay\Documents` &#8594; move multiple files using wildcard.  
17. `rm ~/file.extension` &#8594; remove file or dir (permanent del).  
18. `cat file.extension` &#8594; open text file.  
19. `Select-String word file.extension`&#8594; search for word in file.extension.  
20. `ls 'C:\Program Files\' -Recurse -Filter *.exe` &#8594; look for all the .exe files in the given directory and subdirectories.  
21. `Get-LocalGroup` &#8594; shows all the user groups.
22. `Get-LocalGroupMember Administrators` &#8594; Lists all the users in the specific groups (administrators in this case).  



# commands in Linux:  
1. `ls`/ &#8594; list files in current directory  
2. `ls --help` &#8594; gets help about ls(change ls with required parameter)  
3. `man ls` &#8594; gets same info like with `--help` but with a little more details
4. `ls -l /` &#8594; shows additional info about directory and files & folders in them (in the below order)  
> file permissions | no of links that file has | file owner & group | size | last modification | file/dir name  
5. `ls -la /` or `ls -l -a /` &#8594; `-a` flag shows all files including hidden ones
6. `pwd` &#8594; print working dir(same as windows)  
7. `cd ../documents` &#8594; navigate around (to documents dir here)  
8. `cd ~\Desktop` &#8594; go to mentioned directory from anywhere(press tab after pressing first letter to see recommendations from that name)(same as windows)  
9. `mkdir "my cool folder"` or `mkdir my\ cool\ folder` &#8594; make a dir (\\ is the escape character here)  
10. `history` or **ctrl-r** &#8594; presents command history(same as windows)  
11. `clear` &#8594; clears the output screen(same as windows)  
12. `cp mycoolfile.text ~/Desktop` &#8594; copy the file to desktop (in this case)(same as windows)  
13. `cp *.jpg ~/Desktop` &#8594; copies all the files with mentioned extension(* takes anything for name with .jpg in this case)(same as windows)  
14. `cp -r "my cool folder" ~/Desktop` &#8594; copies the specified folder along with all files inside and sub-folders.(same as windows)  
15. `mv red_document.txt blue_document.txt` &#8594; rename file(same  as windows)
16. `mv blue_document.txt ~/Documents` or `mv *_document.txt ~/Desktop` &#8594; move file(same  as windows)  
17. `grep cow *.txt` &#8594; search for the word "cow" in all the files with .txt extension.    
18. `cat /etc/group` &#8594; See user groups (replace group with 'passwd' to see information about users).  
19. 


# Tips for Linux  
###### root directory =>  
* /bin &#8594; essential binaries and programs like `ls` command(like `program files` dir in windows)  
* /etc &#8594; system configuration files  
* /home &#8594; personal dir, holds user docs, pics etc.(like `user` dir in windows)  
* /proc &#8594; contains info about currently running processes  
* /usr &#8594; contains user installed softwares  
* /var &#8594; systems logs and constantly changing files  
* `.filename` &#8594; "." is used to hide a file/dir  
