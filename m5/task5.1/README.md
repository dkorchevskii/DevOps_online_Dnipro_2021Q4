# Task1. Part1

## 1) Log in to the system as root.

```
sudo su
```

## 2) Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change?

Passwd is a tool used to change a user's password.

 
  
In older Linux systems, the user’s encrypted password was stored in the /etc/passwd file. On most modern systems, this field is set to x, and the user password is stored in the /etc/shadow file.
    


## 3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?


The /etc/passwd file is a text file with one entry per line, representing a user account. To view the contents of the file, use a text editor or a command such as cat :

```
cat /etc/passwd
```
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/1.jpg?raw=true)

Each line of the /etc/passwd file contains seven comma-separated fields:


```
korch:x:1001:1001:Dmytro,,,:/home/korch:/bin/bash
[---] - [--] [--] [--------] [--------] [--------]
|     |   |    |        |         |        |
|     |   |    |        |         |        +-> 7. Login shell
|     |   |    |        |         +----------> 6. Home directory
|     |   |    |        +--------------------> 5. GECOS
|     |   |    +-----------------------------> 4. GID
|     |   +----------------------------------> 3. UID
|     +--------------------------------------> 2. Password
+--------------------------------------------> 1. Username
```
## 4) Change personal information about yourself.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/2.jpg?raw=true)

## 5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.

>passwd
  - passwd -S: Get the current status of the user
    

  - passwd -d: Make the password of the account blank (it will set the named account passwordless)
  
>finger
  - finger -s: Display the user's login name, real name, terminal name, and other information

  - finger -l: Produce multiline output format displaying same information as `-s` as well as user's home directory, home phone number, login shell, mail status, etc.


## 6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

>Less  is  a  program  similar  to more (1), but it has many more features.  Less does not have to read the entire input file before starting, so with large input files it starts upfaster than text editors like vi (1).  
>Less uses termcap (or terminfo on some systems), so it can run on a variety of terminals.  There is even limited support for hardcopy  terminals.


![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/3.jpg?raw=true)



## 7) * Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.

We are working on getting familiar with commands using linux help system and implementing them in real life.

## 8) * List the contents of the home directory using the ls command, define its files and directories. 

```
ls -la 
```


![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/4.jpg?raw=true)

# Task1.Part2

## 1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.
```
sudo tree / -L 2 -P *de* --prune

```
>tree - list contents of directories in a tree-like format.

-L level Max display depth of the directory tree.

-P pattern List  only  those files that match the wild-card pattern.
 
 --prune Makes tree prune empty directories from the output
 
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/5.jpg?raw=true)
 
## 2) What command can be used to determine the type of file (for example, text or binary)? Give an example.

>file — determine file type

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/6.jpg?raw=true)



## 3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

```cd ~```

## 4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/7.jpg?raw=true)


- ls - list directory contents

- -a, --all do not ignore entries starting with .

- -l use a long listing format

- -h, --human-readable sizes

- -t sort by modification time, newest first

- -r, --reverse reverse order while sorting



## 5) Perform the following sequence of operations:
- create a subdirectory in the home directory;
- in this subdirectory create a file containing information about directories
located in the root directory (using I/O redirection operations);
- view the created file;
- copy the created file to your home directory using relative and absolute
addressing.
- delete the previously created subdirectory with the file requesting removal;
- delete the file copied to the home directory.

```
mkdir ~/subdir; cd ~/subdir
tree / -d -L 1 > root_dir.txt
cat root_dir.txt
cp root_dir.txt ~ 
cp root_dir.txt ..
cp root_dir.txt /home/korch/
rm -ri ~/subdir/
rm ~/root_dir.txt
```

## 6) Perform the following sequence of operations:
- create a subdirectory test in the home directory;
- copy the .bash_history file to this directory while changing its name to
labwork2;
- create a hard and soft link to the labwork2 file in the test subdirectory;
- how to define soft and hard link, what do these
concepts;
- change the data by opening a symbolic link. What changes will happen and
why
- rename the hard link file to hard_lnk_labwork2;
- rename the soft link file to symb_lnk_labwork2 file;
- then delete the labwork2. What changes have occurred and why?

```
~$ mkdir test
cp .bash_history test/labwork2
ln ~/test/labwork2 ~/hardlink
ln -s ~/test/labwork2 ~/symlink
vim symlink
mv hardlink hard_lnk_labwork2; mv symlink symb_lnk_labwork2
rm ~/test/labwork2 
```

Hard and soft links behave differently when the source of the link (what is being linked to) is moved or removed. Symbolic links are not updated (they merely contain a string which is the path name of its target); hard links always refer to the source, even if moved or removed. 

Each hard linked file is assigned the same Inode value as the original, therefore they reference the same physical file location. Hard links more flexible and remain linked even if the original or linked files are moved throughout the file system, although hard links are unable to cross different file systems.

A soft link is similar to the file shortcut feature which is used in Windows Operating systems. Each soft linked file contains a separate Inode value that points to the original file. As similar to hard links, any changes to the data in either file is reflected in the other. Soft links can be linked across different file systems, although if the original file is deleted or moved, the soft linked file will not work correctly (called hanging link).

## 7) Using the locate utility, find all files that contain the squid and traceroute sequence.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/8.jpg?raw=true)

## 8) Determine which partitions are mounted in the system, as well as the types of these partitions.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/9.jpg?raw=true)

## 9) Count the number of lines containing a given sequence of characters in a given file.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/10.jpg?raw=true)


## 10) Using the find command, find all files in the /etc directory containing the host character sequence.

```~/Korchevskiy$ sudo find /etc/ -type f -iname *host*```

## 11) List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/11.jpg?raw=true)

## 12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.

```ls -a /etc | less```


## 13) What are the types of devices and how to determine the type of device? Give examples.


When we connect a device to machine, it generally needs a device driver to function properly. Also we can interact with device drivers through device files or device nodes, these are special files that look like regular files. Since these device files are just like regular files, we can use programs such as ls, cat, etc to interact with them. These device files are generally stored in the /dev directory.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.1/Screenshots/12.jpg?raw=true)

In the ls command we can see the type of file with the first bit on each line. Device files are denoted as the following:

c - character
b - block
p - pipe
s - socket

Character Device

These devices transfer data, but one a character at a time. We can see a lot of pseudo devices (/dev/null) as character devices, these devices aren't really physically connected to the machine, but they allow the operating system greater functionality.

Block Device

These devices transfer data, but in large fixed-sized blocks. We'll most commonly see devices that utilize data blocks as block devices, such as harddrives, filesystems, etc.

Pipe Device

Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

Socket Device

Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.


## 14) How to determine the type of file in the system, what types of files are there?

There are following type of files:

- Regular files – Images/scripts/configuration and Data files

- Directory – Type of files which saves other files and directories

* Special files – have other types:
	- Character Files – Represent devices – like Mouse and keyboards
	- Block Files – Represent block devices that writes data in chunk to the devices like HDD and RAM
	- Links – Hard links and Soft Links
	- Socket Files – enables the commnuication between 2 process
	- Named Pipes – passes data from one process to another



Use ls -l command to get the file type. First character represents the file type:


| Identifier| File Type |
| ----------|:---------:|
|  d  | Directory       |
|  -  | Regular File    |
|  c  | Character Device|
|  l  | Link            |
|  s  | Socket File     |
|  p  | Pipe            |
|  b  | Block Device    |


Also we can use file command to determine a file type.

## 15) * List the first 5 directory files that were recently accessed in the /etc directory.

```ls -lt /etc | head -n 5```
