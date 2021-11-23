
Task 3.1 - Creating networks Home Office, Enterprise, Data Center.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/1_1.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/1_2.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/1_3.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/1_4.jpg?raw=true)


Additional task: Study the package structure with the help of Wireshark analyzer

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/1+.jpg?raw=true)



Task 3.2 - Connecting individual networks over the Internet and setting up VLAN.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/2_1.jpg?raw=true)

When we change subnet mask to /26 computers in Data Center network are in different subnets and tracert shows that pings agre going through network router.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/2_2.jpg?raw=true)

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/2_3.jpg?raw=true)


If we create different Vlans for each computer on the network we'll see that we cant ping other copmuters. Because every active ports on switch are on different Vlans the icpm frame won't go anywhere.
The Switch floods the frame to all ports in the same VLAN except the receiving port. 


Additional task: Configure routing between VLAN

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/2+.jpg?raw=true)



Task 3.3 - Setting up routing.

Static routing

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/3_1.jpg?raw=true)


Additional task: Dynamic routing

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/3+.jpg?raw=true)



Task 3.4 - Setting up DHCP, DNS, NAT

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/4_1.jpg?raw=true)


Additional task: Port Forwarding on Home Router

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m3/Screenshots/4+.jpg?raw=true)





