# -*- coding: utf-8 -*-
import paramiko
import os, sys
import requests
import time

if len(sys.argv) == 4:
    ssh_host = sys.argv[1]
    ssh_port = 22
    user = sys.argv[2]
    password = sys.argv[3]
    ssh = paramiko.SSHClient()  # 绑定一个实例
    ssh.load_system_host_keys()  # 加载known_hosts文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, ssh_port, user, password, timeout=10)
    hostname = ssh.exec_command('hostname')[1].read()
    ssh.exec_command('service mysqld stop')
    time.sleep(5)
    file_sys = ssh.exec_command('service mysqld status')
    if "inactive" in file_sys[1].read():
        print "已停止主机{0}的mysql服务".format(hostname)
    else:
        print "主机{0}的mysql服务未正常停止，请管理员确认!".format(hostname)
        sys.exit(1)

else:
    print "参数输入有误，请确认后再执行！"
    sys.exit(1)  # 错误的方式退出


if len(sys.argv) == 4:
    ssh_host = sys.argv[1]
    ssh_port = 22
    user = sys.argv[2]
    password = sys.argv[3]
    ssh = paramiko.SSHClient()  # 绑定一个实例
    ssh.load_system_host_keys()  # 加载known_hosts文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, ssh_port, user, password, timeout=10)
    hostname = ssh.exec_command('hostname')[1].read()
    ssh.exec_command('service nfs stop')
    time.sleep(5)
    file_sys = ssh.exec_command('service nfs status')
    if "inactive" in file_sys[1].read():
        print "已停止主机{0}的nfs服务".format(hostname)
    else:
        print "主机{0}的nfs服务未正常停止，请管理员确认!".format(hostname)
        sys.exit(1)

else:
    print "参数输入有误，请确认后再执行！"
    sys.exit(1)  # 错误的方式退出