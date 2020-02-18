# -*- coding:utf-8 -*-
import paramiko

import datetime

import os

hostname = '192.168.102.227'
username = 'root'
password = '1qaz@WSX'
port = 22




def upload(local_dir, remote_dir):
    try:
        transp_obj = paramiko.Transport((hostname, port))
        transp_obj.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transp_obj)
        print('upload file start %s ' % str(datetime.datetime.now()).split('.')[0])
        try:
            sftp.put(local_dir, remote_dir)
        except Exception as e:
            sftp.mkdir(os.path.split(remote_dir)[0])
            sftp.put(local_dir, remote_dir)
        # for root, dirs, files in os.walk(local_dir):
        #     for file in files:
        #         local_file_path = os.path.join(root, file)
        #         node_path = local_file_path.replace(local_dir, '').replace('\\', '/').lstrip('/')
        #
        #         remote_file_path = os.path.join(remote_dir, node_path)
        #         print(local_file_path)
        #         print(remote_file_path)
        #         print('------------------------------')
        #         try:
        #             sftp.put(local_file_path, remote_file_path)
        #         except Exception as e:
        #             sftp.mkdir(os.path.split(remote_file_path)[0])
        #             sftp.put(local_file_path, remote_file_path)

        print('upload file success %s ' % str(datetime.datetime.now()).split('.')[0])
        transp_obj.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    local_dir = r'D:\test\test.zip'
    remote_dir = '/data/test/test.zip'
    upload(local_dir, remote_dir)






# for root,dirs,files in os.walk('D:\python',topdown=False):
    # print(root)
    # print dirs
    # print(files)
    # for name in files:
    #     print(os.path.join(root, name))
