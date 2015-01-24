#-*- coding: utf-8 -*-

"""
appstore 用户评价 抓取

示例链接：https://itunes.apple.com/cn/app/shou-ji-bai-du-zui-hao-yong/id382201985?mt=8
元素 div class="customer-reviews"

"""
import urllib2
import re

#评论信息类
class ReviewInfo :
        def __init__(self):
                self.title=""
                self.user=""
                self.content=""

        def getTitle(self) :
                return self.title

        def getUser(self) :
                return self.user

        def getContent(self) :
                return self.content

        def setTitle(self, title) :
                self.title = title;

        def setUser(self, user) :
                self.user = user;

        def setContent(self, content) :
                sefl.content = content;


#评论信息抓取类
class ReviewParser :

        def __init(self) :
                self.div = ""
                self.url = ""

        def setDiv(self, divClass):
                self.div = divClass

        def setURL(self, url):
                self.url = url

        #获取用户评论的所有内容
        def getContent(self) :
                print("div content %s" %(self.div) )
                req = urllib2.Request(self.url)
                global response

                try :
                        response = urllib2.urlopen(req)
                except urllib2.HTTPError, e:
                        print(e.fp.read)

                content = response.read()
                #todo search <div ></div>
                totalSize = len(content)
                beginIndex = content.find(self.div)
                if beginIndex == -1 :
                        return "not found"

                endIndex = content.find("<div metrics-loc=\"Swoosh_\"", beginIndex, totalSize-1)
                if endIndex == -1 :
                        return "not found"

                #get list of Review info
                htmlContent = content[beginIndex:endIndex-1]
                re_h=re.compile('</?\w+[^>]*>') #HTML标签
                info = re.sub(re_h, '', htmlContent)
                re_line = re.compile('\n+')
                info = re.sub(re_line, '', info)
                return info
                
        #匹配每一条评论信息
        def getReviewInfos(self) :
                return ""



if __name__ == "__main__" :
        parser = ReviewParser()
        parser.setDiv("<div class=\"customer-reviews\"")

        with open("f:\\test\\github\\url.txt") as f:
                for line in f :
                        parser.setURL(line)
                        content = parser.getContent()
                        print(content)
        
        f.close()

        """
        f = open("url.txt")
        try :
                for line in f :
                        parser.setURL(line)
                        content = parser.getContent()
                        print(content)
        except:
                print("read file error")
        finally:
                f.close()
        """

        """
        com.voxlearning.teacher
        com.voxlearning.teacherLaunchActivity
        """
