# coding:utf8
import urllib2, cookielib

url = "http://www.baidu.com"

print "第一种方法"
### 打开网页返回response
response1 = urllib2.urlopen(url)
### 返回response 状态码 200表示成功
print response1.getcode()
### 返回内容的长度
print len(response1.read())

print "第二种方法"
### 获得请求 以便添加内容 request.add_data('a','1')添加数据
request = urllib2.Request(url)
### 添加头文件 伪装成浏览器
request.add_header("user-agent", "Mozilla/5.0")
### 发送请求得到response
response2 = urllib2.urlopen(request)
### 返回response 状态码
print response2.getcode()
### 返回内容的长度
print len(response2.read())

print "第三种方法"
### 增加cookie处理能力 还有其他ProxyHandler,HTTPSHandler,HTTPReadirectHandler
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
### 返回response 状态码
print response3.getcode()
### 返回cookie内容
print cj
### 返回网页内容
print response3.read()


