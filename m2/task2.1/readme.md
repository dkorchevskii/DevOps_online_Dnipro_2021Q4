# TASK 2.1 

# PART 1. HYPERVISORS 
The most popular hypervisors for infrastructure virtualization are: 
	1. VMware vSphere / ESXi
	2. Microsoft Hyper-V
	3. Xen / Citrix XenServer
	4. Red Hat Enterprise Virtualization (RHEV)
	5.  KVM

The first main difference of the most popular hypervisors is type. 	
There are two types:
	- Type-1, native or bare-metal hypervisors and 
	- Type-2 or hosted hypervisors
Type 1 hypervisors are running directly on hardware and type 2 are just like regular software are running on OS.
For enteprise goals mostly used type 1 HV, so lets talk about differences between them.

   VMWare Vsphere is the leader in the type 1 hypervisors. VMware led the market in developing innovative features such as memory overcommitment, vMotion, Storage vMotion, Fault Tolerance, and more. 
Works with all server platforms, has its own kernel similar to Linux, but with own CLI commands and utilites. Most suitable for big infrastructures.

   Microsoft Hyper-V is Microsoft’s solution for virtualized systems. In modern windows systems along with server editions, Hyper-V can be utilized to virtualize other operating systems. Microsoft also offers a free edition of their hypervisor. May not offer as many features as VMware vSphere package, but you still get live migration, replication of virtual machines, dynamic memory and many other features.

   KVM (Kernel-based Virtual Machine) is Hypervisor based on Linux is an open source hypervisor. KVM can run on Linux operating systems like SUSE, Ubuntu and Red Hat Enterprise Linux. Apart from these, Windows and Solaris are some Linux operating systems supported. With KVM, Linux turns into a hypervisor that enables host computer to run and support several other virtual machines or guests.

   Red Hat Enterprise Virtualization (RHEV) built on Kernel-based Virtual Machine (KVM), it benefits users as an easy to set up, use and manage alternative. An open source hypervisor, Red Hat Enterprise is made in such a way that it can work with anything but it is also tested on many hardware and servers. RHEV is an affordable solution as the total cost of owning it is low while performance is outstanding.

   Citrix XenServer is a commercial solution provided by Citrix present in 4 editions. Just as Red Hat Enterprise Virtualization uses KVM. Features offered are power management, memory optimization, monitoring and alerting, conversion tools, live storage migration etc. XenServer started as an open source project and today it has labelled their proprietary solutions namely XenDesktop and XenApp with the name of Xen.

# PART 2. WORK WITH VIRTUALBOX

![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/3.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/5.jpg?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/1.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/2.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/4.JPG?raw=true)
 
# PART 3. WORK WITH VAGRANT 

![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/7.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/8.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/9.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/11.JPG?raw=true)
![alt text](https://github.com/DevOps_online_Dnipro_2021Q4/blob/main/m2/task2.1/Screenshots/12.JPG?raw=true)



