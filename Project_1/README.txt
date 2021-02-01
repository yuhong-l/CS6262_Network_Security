Name:
GT Login ID:

Task 1: 
<Your Explanation>
Used "arp -a" to list all addresses found in the arp cache. ARP stands for address resolution protocol, i.e. displays all the active IP addresses connected to the local network

https://www.dnsstuff.com/scan-network-for-device-ip-address


#4 used nmap -p- 10.0.2.4 to scan all ports

then used netcat <ip> <port> to connect to port on host via tcp and get response
Task 2:
<Your Explanation>
used curl with modifying the head user agent and sent it the script to execute
https://www.sevenlayers.com/index.php/125-exploiting-shellshock


Task 3:
<Your Explanation>
found exploit using search shellshock
exploit is - exploit/multi/http/apache_mod_cgi_bash_env_exec

then searched payloads with "show payloads"
used linux/x86/shell_reverse_tcp  

then set the targeruri to be the /cgi-bin/shellshock.cgi

set the host to host found in previous step

then ran "check" , which returns if host is vulnerable to shellsock

then ran "exploit" and followed directions

cite: https://null-byte.wonderhowto.com/how-to/exploit-shellshock-web-server-using-metasploit-0186084/


Task 4:
<Your Explanation>

Task 5:
<Your Explanation>