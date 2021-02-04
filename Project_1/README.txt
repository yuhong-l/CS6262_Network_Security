Name:
imalik30

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
Found exploit using search shellshock
exploit is - exploit/multi/http/apache_mod_cgi_bash_env_exec

Then searched payloads with "show payloads"
used linux/x86/shell_reverse_tcp  



Task 4:
<Your Explanation>

  Command : ls -lArt /usr/bin | grep "rws"   OR    find /usr/bin -perm -u=s -type f

-looked in /usr/bin for programs with setuid bit set
-also used  find /usr/bin -perm -u=s -type f , which finds files with setuid and permission as root

-find can be used to execute commands with exec 

cite: https://gtfobins.github.io/gtfobins/find/#shell


Task 5:
<Your Explanation>

Output the has for task51 to task51hash: 

"zip2john" task51.zip >> task51hash"

then ran
"john --incremental task51hash"
to decrypt and get the password

ran  
"unzip task51.zip"  and entered password found above
ran python file with user id and got hash


use cewl to get wordlist from all author links and run that with john the ripper to get the password

ran "gpg --decrypt task52.pyc.gpg" and entered password found above
ran python file with user id and got hash
