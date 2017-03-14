## Python爬虫

- 自带爬虫方法  

- BeautifulSoup4插件解析html https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5 

> BeautifulSoup4语法
Html网页-》创建BeautifulSoup对象-》搜索节点find_all,find(按照节点名称、属性值、文字搜索)-》访问节点（名称、属性、文字）

### 说明

spider_main.py 总调度程序  
url_manager.py url管理程序  
html_downloader.py html下载器  
html_parser.py html解析器  
html_outputer.py 输出内容  