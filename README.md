# Subdomain-Scan 

## Description

Subdomain-Scan is a simple python tool designed to find subdomains using bruteforce techniques.
This recon tool can help you to spot hidden subdomains from your target.

## Useful Features:

<b>Multi-Threading:</b> [<i>up to <b>222</b> threads</i>] This feature makes Subdomain-Scan faster than the majority of subdomain enumeration tools available.

<b>Recursive Mode:</b> With this, you can go further in your target, finding more elaborate subdomain names.

## Dependencies

* <b>Python3</b>

    ```sudo apt-get install python3.6```

* <b>Host</b>:

    ```sudo apt-get install host```
    
* <b>Used Python Libs</b>
    ```
    subprocess
    argparse 
    threading
    queue
    time
    sys
    ```

## Setup

```git clone https://github.com/RafaelSantos025/DNS-Scan.git```

```cd Subdomain-Scan/```

```chmod +x dns_scan```

## How To Use

<b>Basic Usage</b>

```./dns_scan <domain> <wordlist>```

<b>Help: </b>

```./dns_scan -h```

<b>Using Threads: </b>

```./dns_scan <domain> <wordlist> [-t 222]```

The maximum number of threads is 222 [1 - 222].

<b>Recursive Mode: </b>

```./dns_scan <domain> <wordlist> [-r]```

<b>Example: </b> ```./dns_scan google.com subdomains.txt -t 55 -r```
This command will scan all *.google.com subdomains in the passed wordlist.

![alt text](https://i.ibb.co/dMcR8vp/dns.png)

## Recommended Wordlists

The following repository contains a lot of useful wordlists for subdomain enumeration: https://github.com/rbsec/dnscan
