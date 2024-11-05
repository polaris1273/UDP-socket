import socket#导入socket模块，用于建立套接字网络通讯
import os#导入os模块，用于从主机上读取文件

# 创建UDP套接字AF_INET表示使用IPv4地址，SOCK_DGRAM表示使用Udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口，这里固定为guest的ip，和端口号
server_address = ('192.168.229.129', 8888)
#确定服务区的地址和端口，是服务器监听特定的UDP数据
server_socket.bind(server_address)
#反馈server已经启动
print("服务器已启动，等待client发送")

# 接收文件名，从客服端每次接受最大为1024字节的内容
file_name, client_address = server_socket.recvfrom(1024)
#将接受的第一批内容解码为文件名
file_name = file_name.decode()

# 打开文件写入，文件存在直接写入，不存在创建打开写入
with open(file_name, 'wb') as file:
    #反馈server进程状态
    print(f"正在接收文件：{file_name}")
    #开始循环接收每一组数据，直到接收结束
    while True:
        #关键的接收套接字
        data, client_address = server_socket.recvfrom(1024)
        #如果数据读取结束，没有数据之后结束循环，结束读取
        if data == b'EOF':
            break
            #将接收的内容写入到刚才的file中
        file.write(data)
#反馈接收结束
print(f"文件接收完成：{file_name}")

# 关闭套接字
server_socket.close()
