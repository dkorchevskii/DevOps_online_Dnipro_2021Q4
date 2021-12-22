# Task 6.2. Configuring DHCP, DNS servers and dynamic routing using OSPF protocol


## 1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal, VM2, VM3 – internal only interfaces.

I added 3rd VM with internal interface to scheme from previous task.

## 2. Install and configure DHCP server on VM1. (3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER). You should use at least 2 of them.

DNSMASQ DHCP + DNS:

Ubuntu 18.04+ comes with systemd-resolve which we need to disable since it binds to port 53 which will conflict with Dnsmasq port and remove the symlinked resolv.conf file

```
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
sudo rm /etc/resolv.conf
```

Let's create new resolv.conf file.

```echo "nameserver 1.1.1.1\nnameserver 9.9.9.9" | sudo tee /etc/resolv.conf```

Install dnsmasq: 

```sudo apt install dnsmasq -y```   

/etc/dnsmasq.conf :
```
domain-needed
bogus-priv
strict-order
interface=enp0s8
expand-hosts
domain=local.korch
dhcp-range=10.10.10.20,10.10.10.40,12h
dhcp-host=ubuntusrv2
dhcp-host=ubuntusrv3
dhcp-option=option:router,10.10.10.10
dhcp-leasefile=/var/lib/misc/dnsmasq.leases
```

/etc/hosts
```
127.0.0.1 localhost
10.10.10.10 ubuntusrv1
10.10.10.20 ubuntusrv2
10.10.10.30 ubuntusrv3
```

ISC DHCP:

``` sudo apt install isc-dhcp-server -y```

/etc/dhcp/dhcpd.conf :
```option domain-name "local.korch";
option domain-name-servers 10.10.10.10;
option routers 10.10.10.10;
default-lease-time 600;
max-lease-time 7200;
ddns-update-style none;
authoritative;
subnet 10.10.10.0 netmask 255.255.255.0 {}
subnet 10.10.10.0 netmask 255.255.255.0 {
range 10.10.10.100 10.10.10.200;
}
host ubuntusrv2 {
  hardware ethernet 08:00:27:0d:15:c5;
  fixed-address 10.10.10.20;
}
host ubuntusrv3 {
  hardware ethernet 08:00:27:31:a5:db;
  fixed-address 10.10.10.30;
}
```

## 3. Check VM2 and VM3 for obtaining network addresses from DHCP server.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/2.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/3.jpg?raw=true)


## 4. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. (You can use DNSMASQ, BIND9 or something else).

DNSMASQ DNS:

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/4.jpg?raw=true)

BIND9 DNS server default configuration acts as a caching server. We simply uncomment and edit /etc/bind/named.conf.options to set the IP addresses of authoritative DNS servers:

```forwarders 
	{
     1.1.1.1;
     9.9.9.9;
	};
```


## 5. Check VM2 and VM3 for gaining access to DNS server (naming services).

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/5.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/6.jpg?raw=true)


## 6. *** Using the scheme which follows, configure dynamic routing using OSPF protocol.

I used Quagga to configure OSPF.

I installed & configured it on all VMs:

```
sudo apt update && sudo apt upgrade && sudo apt install quagga -y
sudo touch /etc/quagga/zebra.conf && sudo touch /etc/quagga/ospfd.conf
sudo mkdir /var/log/quagga
sudo chown -R quagga:quagga /etc/quagga && sudo chown -R quagga:quagga /var/log/quagga
sudo service zebra restart
sudo service ospfd restart
```
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/7.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/8.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/9.jpg?raw=true)

## 7. Check results

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/10.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/11.jpg?raw=true)
![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/12.jpg?raw=true)

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m6/task6.2/Screenshots/13.jpg?raw=true)

