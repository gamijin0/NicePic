from selenium import webdriver
import requests
import time
import os
from bs4 import BeautifulSoup as BS
class MyPic:
    driver = webdriver.PhantomJS()
    img_urls_list = list()
    #download the image for judge
    def GetImg(self,Page_url):

        picpath = '%s' % (Page_url[Page_url.find('http')+7:Page_url.find('com')+3]) # 下载到的本地目录
        if not os.path.exists(picpath):  # 路径不存在时创建一个
            os.makedirs(picpath)

        urls_list=self.GetImgUrls(Page_url)#获取该页面图片列表
        self.img_urls_list = urls_list  #存储列表

        print("数量:"+str(len(urls_list)))
        i=0
        for url in urls_list:
            i += 1
            print(url)
            if((url[-3:]!='jpg') or url[:4]!='http'):
                print('Not a valid url.')
                continue
            else:
                #print(i)
                filename = ".//"+picpath+"//"+url[-17:-4]+"_"+str(i)+'.'+url[-3:]
                print(filename)
                img = requests.get(url)
                with open(filename,mode='wb') as f:
                    f.write(img.content)

        print("Done.")
        return None

    #detect the url in one page
    def GetImgUrls(self,Page_url):

        try:
            self.driver.get(Page_url)
            time.sleep(1)
            html = self.driver.page_source
            #print(html)

            bs = BS(html )
            img_list = bs.find_all('img')
            url_list = list()

            for tag in img_list:
                #print(tag['src'])
                #url_list.append(tag.attrs['src'])
                url_list.append(tag.attrs['data-original'])
            return url_list
        except:
            return url_list

    def Judge(self):
        return None

if __name__=="__main__":
    for i in range(2,30):
        one = MyPic()
        url = "http://www.mzitu.com/xinggan/page/"+str(i)
        print(url)
        one.GetImg(url)