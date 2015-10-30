# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
class One:
    def __init__(self) :
        self.page = 1
        self.cur_url = "http://wufazhuce.com/one/vol.{page}"
    def get_page(self, cur_page) :
        url = self.cur_url
        try :
            my_page = urllib2.urlopen(url.format(page = cur_page)).read().decode("utf-8")
        except urllib2.URLError, e :
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return my_page
    def saveImg(self,my_page) :
        pattern = re.compile('<div class="one-imagen".*?>(.*?)alt',re.S)
        content = re.search(pattern,my_page)
        pattern = re.compile('img src="(.*?)"',re.S)
        patternImg = re.findall(pattern,content.group(1))
        for img in patternImg :
            u = urllib.urlopen(img)
            data = u.read()
            fileName = "One" + "/" + str(self.page)+".jpg"
            f = open(fileName, 'wb')
            f.write(data)
            f.close()
    def mkdir(self):
        path = "One"
        path = path.strip()
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False
    def start_pic(self) :
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        print "loading..."
        while self.page <= 1117 :
            self.mkdir()
            my_page = self.get_page(self.page)
            self.saveImg(my_page)
            self.page += 1
def main() :
    print "Loading..."
    onepic = One()
    onepic.start_pic()
    print "END..."

if __name__ == '__main__':
    main()