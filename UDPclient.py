import socket  # 导入socket模块，用于建立套接字网络通讯
import os  # 导入os模块，用于从主机上读取文件

# 创建UDP套接字 AF_INET表示使用IPv4地址，SOCK_DGRAM表示使用Udp协议
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 手动输入服务器的IP地址和端口号
server_ip = input("请输入服务器的IP地址：")
server_port = int(input("请输入服务器的端口号："))

# 服务器地址和端口，这里不再固定为guest的ip，和端口号
server_address = (server_ip, server_port)

# 选择要发送的文件，这里要输入发送文件的目录加文件名
file_name = input("请输入要发送的文件名：")

# 检查文件是否存在
if not os.path.exists(file_name):
    # 如果文件不存在，结束程序
    print("文件不存在，请检查文件名")
    exit()
# 先发送文件名，将文件名编码为字符串，发送给server
client_socket.sendto(file_name.encode(), server_address)
# 打开文件并发送数据 以二进制读取文件
with open(file_name, 'rb') as file:
    print(f"正在发送文件：{file_name}")
    # 作了文件传输的限制，最大读取文件的前1024字节
    data = file.read(1024)
    # 开始循环发送读取的内容，直到结束
    while data:
        # 将读取文件发送给server
        client_socket.sendto(data, server_address)
        # 继续读取之后的一组（1024字节）数据
        data = file.read(1024)
# 发送结束信号(使用之前的方法无法在发送完成后自动结束，采用这种笨的方法)
client_socket.sendto(b'EOF', server_address)
# 反馈文件发送完毕
print(f"文件发送完成：{file_name}")
# 关闭套接字
client_socket.close()
