from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

# 开始抓包，捕获 10 个数据包
sniff(prn=packet_callback, count=10)