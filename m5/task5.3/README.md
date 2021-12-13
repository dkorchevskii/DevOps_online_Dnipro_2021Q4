# TASK5.3 Part1

# 1. How many states could has a process in Linux?

During execution, a process changes from one state to another depending on its environment/circumstances. In Linux, a process has the following possible states:

- Running – here it’s either running (it is the current process in the system) or it’s ready to run (it’s waiting to be assigned to one of the CPUs).
- Waiting – in this state, a process is waiting for an event to occur or for a system resource. Additionally, the kernel also differentiates between two types of waiting processes; interruptible waiting processes – can be interrupted by signals and uninterruptible waiting processes – are waiting directly on hardware conditions and cannot be interrupted by any event/signal.
- Stopped – in this state, a process has been stopped, usually by receiving a signal. For instance, a process that is being debugged.
- Zombie – here, a process is dead, it has been halted but it’s still has an entry in the process table.

If we use ps utilty to report a snapshot of the current processes we can see this state of a process:

	D    uninterruptible sleep (usually IO)
	I    Idle kernel thread
	R    running or runnable (on run queue)
	S    interruptible sleep (waiting for an event to complete)
	T    stopped by job control signal
	t    stopped by debugger during the tracing
	W    paging (not valid since the 2.6.xx kernel)
	X    dead (should never be seen)
	Z    defunct ("zombie") process, terminated but not reaped by its parent

For BSD formats and when the stat keyword is used, additional characters may be displayed:

	<    high-priority (not nice to other users)
	N    low-priority (nice to other users)
	L    has pages locked into memory (for real-time and custom IO)
	s    is a session leader
	l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
	+    is in the foreground process group

# 2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/1.jpg?raw=true)

# 3. What is a proc file system?

The /proc/ directory — also called the proc file system — contains a hierarchy of special files which represent the current state of the kernel — allowing applications and users to peer into the kernel's view of the system. 

It  provides access to the state of each active process and thread in the system. The name of each entry in the /proc file system is a decimal number corresponding to the process ID.

The proc file system acts as an interface to internal data structures in the kernel. It can be used to obtain information about the system and to change certain kernel parameters at runtime (sysctl).

It is not a true filesystem that is consuming storage. The files and directories in /proc are entry points into kernel tables, such as the open file table or the process table. 

# 4. Print information about the processor (its type, supported technologies, etc.).

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/2.jpg?raw=true)

# 5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/3.jpg?raw=true)

# 6. How to define kernel processes and user processes?

Kernel processes (or "kernel threads") are children of PID 2 (kthreadd), so we can filter processes by ppid


# 7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/4.jpg?raw=true)


# 8. Display only the processes of a specific user.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/5.jpg?raw=true)

# 9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/6.jpg?raw=true)

# 10. What information does top command display?

top display dynamic real-time information about running processes.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/7.jpg?raw=true)

# 12. Display the processes of the specific user using the top command.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/8.jpg?raw=true)

# 12. What interactive commands can be used to control the top command? Give a couple of examples.

There are dozens of command, lets describe some of them.

c : toggles the COMMAND column between displaying the process name and the full command line.

V : see a “tree” of processes that were launched or spawned by other processes.

u : see the processes for a single user. You’ll be prompted for the name or UID.

i : sgows only active tasks

n : limit the display to a certain number of lines, regardless of whether the tasks are active. 

r : change the nice value (priority) for a process. 

k : kill a process

Sorting by:
 
* P: The %CPU column.
* M: The %MEM column.
* N: The PID column.
* T: The TIME+ column.	

Changing the Summary Contents:

* E : With this command you can cycle through the available summary area memory scaling which ranges from KiB through EiB
* l : Toggle the load summary line (the first line) on or off.
* t : This command serves as a 4-way toggle, cycling through these modes:
      	1. detailed percentages by category
      	2. abbreviated user/system and total % + bar graph
      	3. abbreviated user/system and total % + block graph
      	4. turn off task and cpu states display
* m : This command serves as a 4-way toggle, cycling through these modes:
        1. detailed percentages by memory type
        2. abbreviated % used/total available + bar graph
        3. abbreviated % used/total available + block graph
        4. turn off memory display
		
W: Save your settings and customizations so they’ll still be in effect when you next start top.


# 13. Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.)

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/9.jpg?raw=true)

# 14. Concept of priority, what commands are used to set priority?

Every process requires a certain amount of system resources, like central processing unit (CPU) time and random access memory (RAM), to be able to perform its tasks. Each process is assigned a process priority, which determines how much CPU or processor time is allocated to it for execution.

The priority value is the process’s actual priority which is used by the Linux kernel to schedule a task.

Nice values are user-space values that we can use to control the priority of a process. The nice value range is -20 to +19 where -20 is highest, 0 default and +19 is lowest.

The relation between nice value and priority is as such -Priority_value = Nice_value + 20

To set the priority for a new process we have to use nice command. 

	nice -n niceness_value command

To change the priority of existing process use renice command.

	renice -n niceness_value -p pid


# 15. Can I change the priority of a process using the top command? If so, how?

Yes. According to top manual we have to use interactive command r.

	r  :Renice-a-Task
		You will be prompted for a PID and then the value to nice it to.

# 16. Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals.

Terminate a program using the default SIGTERM (terminate) signal:
    kill process_id


List available signal names:
    kill -l

Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating:
    ```kill -1|HUP process_id```

Terminate a program using the SIGINT (interrupt) signal. This is typically initiated by the user pressing `Ctrl + C`:
    ```kill -2|INT process_id```

Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):
    ```kill -9|KILL process_id```

Signal the operating system to pause a program until a SIGCONT ("continue") signal is received:
    ```kill -19|STOP process_id```


# 17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to demonstrate the process control mechanism with fg, bg.

Those are Linux job control commands. 

jobs: Display a list of the jobs with their status
fg: Move a background job into the foreground
bg: Resume suspended jobs by running them as background jobs
nohup: Run COMMAND, ignoring hangup signals. A llows a process to continue running even after logout or disconnection from current shell/

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/10.jpg?raw=true)


# TASK5.3 Part2

# 1. Check the implementability of the most frequently used OPENSSH commands in the MS Windows operating system. (Description of the expected result of the commands + screenshots: command – result should be presented)

* ssh user@host - connect to a remote host
* ssh-keygen -t keytype - generate authentication key pair
* ssh user@host COMMAND- execute command on remote host

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/11.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/12.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/13.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/14.jpg?raw=true)

# 2. Implement basic SSH settings to increase the security of the client-server connection

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/15.jpg?raw=true)

# 3. List the options for choosing keys for encryption in SSH. Implement 3 of them.

ssh-keygen -t protocol
| Protocol|Generation |
| --------|:---------:|
|  RSA    | 1         |
|  DSA    | 2     	  |
|  ECDSA  | 3 		  |
| ed25519 | 4         |


# 4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m5/task5.3/Screenshots/16.jpg?raw=true)

# 5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result.


Telnet and Rlogin was created at a time when security wasn’t really a major problem, thus it does not use encryption and all the traffic is sent in plain text. 

SSH is a cryptographic network protocol and it sends all traffic throuht encrypted channel.