# DNS Hole
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   <img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python"> <a href='https://github.com/gdsoumya' target='_blank'><img src='https://img.shields.io/github/followers/gdsoumya.svg?label=Folow&style=social'></a><a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fgdsoumya%2Fdns_hole&text=Checkout%20this%20project%20called%20DNS%20Hole%2C%20it%20blocks%20unwanted%20ads%20and%20trackers%20and%20preserves%20your%20privacy.%20&hashtags=%23dns_hole%20%23privacy%20%23ad_blocker%20%23trackers_blocker" target="_blank">
  <img src="http://jpillora.com/github-twitter-button/img/tweet.png"
       alt="tweet button" title="Checkout this project called DNS Hole, it blocks unwanted ads and trackers and preserves your privacy. "></img>
</a>

DNS Hole is a network-level advertisement and Internet tracker blocking tool which acts as a DNS sinkhole. It comes with a tracker and advertisement block list that can be customized according to user preferences and requirements.<br><br>

<img src="https://github.com/gdsoumya/dns_hole/blob/master/dns_hole_cli.png"
       alt="DNS Hole Cli" title="DNS Hole Cli"></img>


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**DNS Hole** requires [ **Python (> Python 3.6)**](https://www.python.org/) .

### Getting the project.

```sh
$ git clone https://github.com/gdsoumya/dns_hole.git
or 
Download and extract the Zip-File
```
### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ pip install -r dependencies.txt 
```
## Starting DNS Hole
To start blocking ads and trackers run
```sh
$ python dns_hole.py
```
A DNS Server will be initialized at **0.0.0.0:53** 

### Errors 
Possible Errors :<br>
1. **Run As Root** : On linux based systems the script needs to be executed as root, on windows admin permissions will be requested.<br>
2. **Port 53 is already in use/Socket Error** : Other processes or services are using the required port(53), kill or close them before executing the script.<br>

## Using DNS Hole
To use DNS Hole you can choose one of the following options:
1. Setup DNS Hole on the Hotspot/Router.
2. Set the DNS address in your router settings to point to the DNS Hole system.
3. Setup network settings on specific devices to point their dns to the DNS Hole system. 

## Changing Block List
To change/update the block list just add or remove the necessary urls in the BlockList.txt file.

## Working Demo 
<img src="https://github.com/gdsoumya/dns_hole/blob/master/dns_hole.png"
       alt="DNS Hole Demo" title="DNS Hole Demo"></img>

## Packages Used
- **[dnslib](https://pypi.org/project/dnslib/)** : A library to encode/decode DNS wire-format packets.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
