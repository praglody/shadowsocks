客户端负载均衡
--------------

主要是添加了upstream这个配置项，upstream里必须包含 server、server_port、password、weight 等配置，目前还不支持动态修改加密方式。

这个主要是用来做同一服务器的多端口负载均衡，让流量分散到不同的端口，降低服务器端口被封的风险。

```
{
    "upstream": [
    	{"server":"45.76.102.109", "server_port":30,    "password":"your password", "weight":1},
        {"server":"45.63.56.112",  "server_port":30001, "password":"your password", "weight":1}
    ],
    "local_address":"0.0.0.0",
    "local_port":14213,
    "method":"aes-256-cfb",
    "timeout":600,
    "fast_open":false,
    "tunnel_remote":"8.8.8.8",
    "dns_server":["8.8.8.8", "8.8.4.4"],
    "tunnel_remote_port":53,
    "tunnel_port":53
}
```

运行

```
python shadowsocks/local.py -c config.json
```


日志展示

```
默认显示 INFO 级别以上的日志

-v        显示 DEBUG 级别日志信息
-vv       显示 VERBOSE 级别日志信息
-q        显示 WARNING 级别日志信息
-qq       显示 ERROR 级别日志信息
```






shadowsocks
===========

[![PyPI version]][PyPI]
[![Build Status]][Travis CI]

A fast tunnel proxy that helps you bypass firewalls.

Features:
- TCP & UDP support
- User management API
- TCP Fast Open
- Workers and graceful restart
- Destination IP blacklist

Server
------

### Install

Debian / Ubuntu:

    apt-get install python-pip
    pip install git+https://github.com/shadowsocks/shadowsocks.git@master

CentOS:

    yum install python-setuptools && easy_install pip
    pip install git+https://github.com/shadowsocks/shadowsocks.git@master

For CentOS 7, if you need AEAD ciphers, you need install libsodium
```
dnf install libsodium python34-pip
pip3 install  git+https://github.com/shadowsocks/shadowsocks.git@master
```
Linux distributions with [snap](http://snapcraft.io/):

    snap install shadowsocks

Windows:

See [Install Shadowsocks Server on Windows](https://github.com/shadowsocks/shadowsocks/wiki/Install-Shadowsocks-Server-on-Windows).

### Usage

    ssserver -p 443 -k password -m aes-256-cfb

To run in the background:

    sudo ssserver -p 443 -k password -m aes-256-cfb --user nobody -d start

To stop:

    sudo ssserver -d stop

To check the log:

    sudo less /var/log/shadowsocks.log

Check all the options via `-h`. You can also use a [Configuration] file
instead.

If you installed the [snap](http://snapcraft.io/) package, you have to prefix the commands with `shadowsocks.`,
like this:

    shadowsocks.ssserver -p 443 -k password -m aes-256-cfb
    
### Usage with Config File

[Create configuration file and run](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)

To start:

    ssserver -c /etc/shadowsocks.json


Documentation
-------------

You can find all the documentation in the [Wiki](https://github.com/shadowsocks/shadowsocks/wiki).

License
-------

Apache License







[Build Status]:      https://img.shields.io/travis/shadowsocks/shadowsocks/master.svg?style=flat
[PyPI]:              https://pypi.python.org/pypi/shadowsocks
[PyPI version]:      https://img.shields.io/pypi/v/shadowsocks.svg?style=flat
[Travis CI]:         https://travis-ci.org/shadowsocks/shadowsocks
