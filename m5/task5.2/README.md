# Task2

## 1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are present in it, what users exist on the system? Specify several pseudo-users, how to define them?

```
cat /etc/passwd
```
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/1.jpg?raw=true)

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

Most Linux distributions reserve the first 100 UIDs for special system users (sometimes called pseudo-users), such as wheel, daemon, lp, operator, news, mail, etc. Pseudo users usually do not need or cannot log in to the system and don't have home directory.These users are administrators who do not need total root powers, but who perform some administrative tasks and thus need more privileges than those given to ordinary users. New users are assigned UIDs starting from 500 or 1000.

```
cat /etc/group
```
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/2.jpg?raw=true)

Each line of the /etc/group file contains four comma-separated fields:

```
adm:x:4:syslog,ubuntu
[-] - [-] [--------]
|   |  |    |  
|   |  |    | 
|   |  |    | 
|   |  |    | 
|   |  |    +-----------------------------> 4. List of users
|   |  +----------------------------------> 3. GID
|   +--------------------------------------> 2. Password
+--------------------------------------------> 1. Group name
```

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/3.jpg?raw=true)


## 2) What are the uid ranges? What is UID? How to define it?

UIS is a user identifier - number assigned by Linux to every user to identify them and determine which system resourses they can use.
Uid ranges are standardized UID values used by system. UID 0 (zero) is reserved for the root. In the range 0 to 99 UIDs should be statically allocated by the system, and shall not be created by applications, while UIDs from 100 to 499(999) should be reserved for dynamic allocation by system administrators and post install scripts.

We can define UID by lookin at /ect/passwd file or with id command.

## 3) What is GID? How to define it?

GID is a group identifier - number assigned by Linux to every group to identify which system resourses group users can use.

We can define GID by lookin at /etc/group file or with group command.

## 4) How to determine belonging of user to the specific group?

```
groups [user]
```
```
cat /etc/group | grep [user]
```

## 5) What are the commands for adding a user to the system? What are the basic parameters required to create a user?

Defult way to add user is using the useradd command ```useradd [options] USERNAME```

This will create a user, but it's a limited operation and will not create other useful things like their home directory or password.
In order to create a user with the default home directory we have to use -m parameter.
Also we can specify the shell, that user will use by adding -s paramentr and the path to the shell in the system.
To set the password we have to use passwd command.


The second way to create a user is to use more modern utility adduser, that will ask series of questions about user in interactive way. 

```adduser USERNAME```

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/4.jpg?raw=true)

## 6) How do I change the name (account name) of an existing user?

* usermod: Modifies a user account.

	- -l Change a user's name:

```usermod -l newname user```


## 7) What is skell_dir? What is its structure?

/etc/skel/ directory in Linux- is a skeleton directory which contains the default files that would automatically get copied to newly created users’ HOME directory.

We can change the default location /etc/skel to any other location in the /etc/defualt/useradd file.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/5.jpg?raw=true)

## 8) How to remove a user from the system (including his mailbox)?

```sudo userdel -r user```



## 9) What commands and keys should be used to lock and unlock a user account?

Best way to lock user is using usermod command

* To lock the user, we can use the -L option:
```usermod -L user```
* To unlock the user, we can use the -U option:
```usermod -U user```

We can also lock user with passwd, but it won't prevent the login via SSH keys if login via SSH key is set.

* To lock a user with the passwd command, we can use the option -l or –lock:
```passwd -l user_name```
* To unlock the user with passwd command, we can use the option -u or –unlock:
```passwd -u user_name```


## 10) How to remove a user's password and provide him with a password-free login for  password change?

```sudo passwd -de user```

## 11) Display the extended format of information about the directory, tell about the information columns displayed on the terminal.

```ls- l```

When the long listing format is used, we can see the following file information:

1. The file type.
1. The file permissions.
1. Number of hard links to the file.
1. File owner.
1. File group.
1. File size.
1. Date and Time.
1. File name.
                                                       
```drwxrwxr-x 2 ubuntu ubuntu 4096 Dec  8 22:31 Korchevskiy```


## 12) What access rights exist and for whom (i. e., describe the main roles)? Briefly describe the acronym for access rights.

In Linux access rights works by associating each system file with an owner and a group and assigning permission access rights for three different classes of users:

* The file owner.
* The group members.
* Others (everybody else).

Three file permissions types apply to each class of users:

* The read permission.
* The write permission.
* The execute permission.

To view the file permissions, use the ls command:

	ls -a
	
drwxr-xr-x 7 ubuntu ubuntu 4096 Dec  8 22:44 

Here we have w-write, x-execute, r-read rights for owner; x-execute, r-read rights for group members and x-execute for others

## 13) What is the sequence of defining the relationship between the file and the user?

First we look if the user is the owner of the file, then is he the part of the file's acces group and if both are not, then the rights for user is rights in others part.

## 14) What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal.

The chown command allows us to change the user and/or group ownership of a given file, directory, or symbolic link.

Permissions can be changed using the chmod command.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/6.jpg?raw=true)

## 15) What is an example of octal representation of access rights? Describe the umask command.

Each write, read, and execute permissions have the following number value:
* r (read) = 4
* w (write) = 2
* x (execute) = 1
* no permissions = 0

To find out the file’s permissions in numeric mode, simply calculate the totals for all users' classes.

For example rwxr-xr-- is 754; 7(4+2+1)5(4+0+1)4(4+0+0)


The umask utility allows to view or to set the file mode creation mask, which determines the permissions bits for newly created files or directories. It is used by mkdir, touch, tee and other commands that create new files and directories. 

To calculate the umask value, simply subtract the desired permissions from the default one:

Umask value for directiries: 777-754 = 023
Umask value for files: 666-644=022

Linux does not allow a file to be created with execute permissions.


## 16) Give definitions of sticky bits and mechanism of identifier substitution. Give an example of files and directories with these attributes.

A Sticky bit is a permission bit that is set on a file or a directory that lets only the owner of the file/directory or the root user to delete or rename the file. No other user is given privileges to delete the file created by some other user. Sticky bit is mainly used on folders in order to avoid deletion of a folder and it’s content by other users though they having write permissions on the folder contents.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.2/Screenshots/7.jpg?raw=true)

## 17) What file attributes should be present in the command script?

To be exetuted the command script should has an execute permission in attributes - x.

