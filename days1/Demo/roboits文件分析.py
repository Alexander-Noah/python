# from urllib.robotparser import RobotFileParser
# rp=RobotFileParser()
# rp.set_url('https://www.baidu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('Baiduspider','https://www.baidu.com'))
# print(rp.can_fetch('Baiduspider','https://www.baidu.com/homepage'))
# print(rp.can_fetch('Googlebot','https://www.baidu.com/homepage/'))
from urllib.robotparser import RobotFileParser
rp =RobotFileParser()
rp = RobotFileParser('https://wwww.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider','https://www.baidu.com/homepage/'))
print(rp.can_fetch('Baiduspider','https://www.baidu.com'))
print(rp.can_fetch('Googlebot','https://www.baidu.com/homepage/'))