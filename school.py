# -*- coding:utf-8 -*-
# @Time:2020/7/27 13:55
# @Author:xu
# @File:school.py.py
import requests
import random
# s=requests.session()
# "account":"admin"
# "pwd":"660B8D2D5359FF6F94F8D3345698F88C"

class School():
    def __init__(self,s):
        self.s = s

    def login(self,user,pwd):

        url_login="http://192.168.5.128:9930/recruit.students/login/in"
        h={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.50 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        }
        body={
            "account":user,
            "pwd":pwd
        }

        r=self.s.get(url=url_login,headers=h,params=body)
        return r

    def addschool(self, name, type, canRecruit):

        url_addschool = "http://192.168.5.128:9930/recruit.students/school/manage/addSchoolInfo"
        body = {
            "schoolName": name,
            "listSchoolType[0].id": type,
            "canRecruit": canRecruit,
            "remark": "",
        }

        r = self.s.post(url=url_addschool, data=body)
        return r

    # print(r.text)
if __name__ == '__main__':
    s=requests.session()
    p=School(s)
    p.login("admin","660B8D2D5359FF6F94F8D3345698F88C")  #登录
    # print(r.text)
# schoolName":name,
# listSchoolType[0].id":"2",
# "canRecruit":"0",

    name = random.randint(3000, 7000000)
    r = p.addschool(name,"2", "0")
    print(r.text)

