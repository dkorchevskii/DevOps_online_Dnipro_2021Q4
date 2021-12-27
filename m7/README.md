# Linux administration with bash. Home task

## A. Create a script that uses the following keys:

1. When starting without parameters, it will display a list of possible keys and their description.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/1.jpg?raw=true)

2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/2.jpg?raw=true)

3. The --target key displays a list of open system TCP ports.

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/3.jpg?raw=true)


The code that performs the functionality of each of the subtasks must be placed in a separate function

```

#!/bin/bash

display_usage() {
        echo -e "Usage:  $0 [arguments]
        $0 --all <target>: Displays the IP addresses and symbolic names of all hosts in the current subnet.
        $0 --target <target>: Displays a list of open system TCP ports on a <target> host IP."
        }
# if no arguments supplied, display usage
        if [  $# -lt 1 ]
        then
                display_usage
                exit 1
        fi

# check whether user had supplied correct arguments. If yes display usage

        if [[  $1 == "--help" ||  $1 == "-h" ]]
        then
                display_usage
                exit 0
        elif [[ $1 != "--all" && $1 != "--target" ]]
        then
                echo "option not present or invalid $1"
                display_usage
                exit 1
        fi

# check if nmap installed and install if it's not

nmapcheck() {
        if ! [ -e /usr/bin/nmap ]
        then
                echo this scrip requiers nmap, installing...
                sudo apt install nmap -y
        fi
        }

all() {
        nmap -sn "$1" | grep report | awk '{print $5 $6}'
        }
target() {
         nmap -sT -p- "$1" | grep open | awk '{print $1, $2}'
        }

nmapcheck

case $1 in
  --all) all "$2" ;;
  --target) target "$2" ;;
esac

```

## B. Using Apache log example create a script to answer the following questions:

1. From which ip were the most requests?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/4.jpg?raw=true)

2. What is the most requested page?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/5.jpg?raw=true)

3. How many requests were there from each ip?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/6.jpg?raw=true)

4. What non-existent pages were clients referred to?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/7.jpg?raw=true)

5. What time did site get the most requests?

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/8.jpg?raw=true)

6. What search bots have accessed the site? (UA + IP)

![alt text](https://github.com/dkorchevskii/DevOps_online_Dnipro_2021Q4/blob/main/m7/Screenshots/9.jpg?raw=true)


```
#!/bin/bash
display_usage() { 
	echo -e "Usage:  $0 <filename>"
	}
	
	if [  $# -lt 1 ] 
	then 
		display_usage
		exit 1
	fi 

echo 1. From which ip were the most requests?
awk '{ print $1 }' $1 | sort -g | uniq -c | sort -nr | head -1| awk '{ print "IP:"$2 " " "Requests:"$1}'
echo
echo 2. What is the most requested page?
awk '{ print $7 }' $1 | sort | uniq -c | sort -nr | head -1 | awk '{ print "Page:"$2 " " "Requests:"$1}'
echo
echo 3. How many requests were there from each ip?
awk '{ print $1 }' $1 | sort -g | uniq -c | sort -nr
echo
echo 4. What non-existent pages were clients referred to?
awk '$9 == "404" { print $7 }' $1 | sort | uniq
echo
echo 5. What time did site get the most requests?
cut apache_logs.txt -d ":" -f2,3 | uniq -c | sort -gr | head -1 | awk '{ print "Time: "$2 " " "Requests:"$1}'  
echo
echo 6. What search bots have accessed the site?
awk -F'"' '{print $6,$1}' $1 | grep bot | cut  -d"-" -f1 | sort | uniq
```

## C. Create a data backup script that takes the following data as parameters:

1. Path to the syncing directory.
2. The path to the directory where the copies of the files will be stored.
In case of adding new or deleting old files, the script must add a corresponding entry to the log file
indicating the time, type of operation and file name. The command to run the script must be added to crontab with a run frequency of one minute

crontab -e

	* * * * * /home/korch/backup /home/korch/src/ /home/korch/dst/
	
```
#!/bin/bash
rsync -av --delete $1 $2 --log-file=bulog.log
```


