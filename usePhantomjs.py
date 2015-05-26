#coding=utf-8

'''
当我访问百度后输入关键词搜索后
答应出如下结果:

包含推广链接有4条
标题 域名

主要用到 selenium 和 xpath.【school/class[number='0302']/master : 找出班级编号为"0302"的班级的班主任】
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys

reload(sys)
sys.setdefaultencoding('utf8')#更改默认编码为 utf8


firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference('permissions.default.image',2)
#firefox_profile.set_preference('permissions.default.stylesheet',2)#禁用css
#firefox_profile.set_preference('javascript.enabled',False)#禁用 js

#browser = webdriver.Firefox(firefox_profile=firefox_profile)


#---------------------------------------------------------
#添加浏览器参数以防无法find和click.
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
#---------------------------------------------------------




browser = webdriver.PhantomJS(executable_path='/opt/local/bin/phantomjs', desired_capabilities=dcap)
#browser.set_window_size(1124, 850)#可以设定 phantomjs 窗口大小
browser.get("https://www.baidu.com")

browser.find_element_by_id("kw").send_keys(u"运动鞋")
browser.save_screenshot('./baidu.png')#打印此时的页面包括js渲染结果

#print browser.page_source
browser.find_element_by_id("su").click()

browser.save_screenshot('./baidu2.png')
browser.implicitly_wait(6)
browser.save_screenshot('./baidu3.png')

tuiguang = browser.find_elements_by_xpath("//a[@href='http://e.baidu.com/?id=1']")#获得带“推广”小标签的链接
print "包含推广链接有 "+ str(len(tuiguang))+" 条" +"\n"
browser.save_screenshot('./baidu4.png')



i = 1
for tiao in tuiguang:
	font = tiao.find_element_by_xpath("..")# webElement 通过 xpath 方法获取上级对象
	div1 = font.find_element_by_xpath("..")# webElement 通过 xpath 方法获取上级对象
	biaot =div1.find_element_by_xpath("./div[1]")#xpath获取对象
	lianj = div1.find_element_by_xpath("./span[1]")#获取包含域名的元素
	yuming = lianj.text #获得域名
	btw = biaot.get_attribute("data-tools")#获取包含标题的元素属性
	wei ="\",\"url"#定位字符
	weiz = btw.find(wei)#获取属性字符串中标题开始位置
	biaoti = btw[10:weiz]#获取标题
 	
 	
 	print i
 	print "标题 " + biaoti
 	print "域名 " + yuming + "\n"
 	i = i + 1
browser.close()
