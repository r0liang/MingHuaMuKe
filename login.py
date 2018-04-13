# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-03 14:55:17
# @Last Modified by:   Marte
# @Last Modified time: 2018-04-13 16:15:52
#coding=utf-8
# -*-coding:utf-8-*-

import sys
import os
import requests
import re
import execjs
import time

def GetModulus(html):
    left=id='"modulus" value="'
    right='\"/>'
    Modulus=re.findall(left+'(.*?)'+right,html)
    print('Modulus:'+Modulus[0])
    return(Modulus[0])

def GetExponent(html):
    left=id='"exponent" value="'
    right='\"/>'
    exponent=re.findall(left+'(.*?)'+right,html)
    print('exponent:'+exponent[0])
    return(exponent[0])

def GetTokenID(html):
    left=id='"tokenId" value="'
    right='\"/>'
    exponent=re.findall(left+'(.*?)'+right,html)
    print('Toeknid:'+exponent[0])
    return(exponent[0])

def get_js():
    # f = open("D:/WorkSpace/MyWorkSpace/jsdemo/js/des_rsa.js",'r',encoding='UTF-8')
    f = open("./rsa.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def login(id,token,type,is,code,lang):
    loginurl="http://bwgl.minghuaetc.com/home/doLogin.mooc"
    d={
    'loginName':id,
    'strToken':token,
    'loginType':type,
    'isCheckCode':0,
    'checkCode':code,
    'historyUrl':'null',
    'lang':lang
    }
    req=requests.post(loginurl,headers=loginheaders,data=d)
    html=req.text
    return(html)



if __name__ == '__main__':
    print('loading')
    lang="zh_CN"
    loginurl = 'http://bwgl.minghuaetc.com/home/login.mooc'
    loginheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Language':'zh-CN',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive'}
    req=requests.get(loginurl,headers=loginheaders)
    t=time.time()
    t=int(round(t * 1000))
    html=req.text
    Exponents=str(GetExponent(html).encode(),encoding='utf-8')
    Moduluss=str(GetModulus(html).encode(),encoding='utf-8')
    Tokenid=str(GetTokenID(html).encode(),encoding='utf-8')
    id=input("账号:")
    passwd=input("密码:")
    Token=Tokenid+"/\n"+passwd
    check=input("输入目录下验证码:")
    print('Rsaing the Key')
    jsstr = get_js()
    ctx = execjs.compile(jsstr)
    datakey=ctx.call("RSAKeyToken",Token,Exponents,"",Moduluss)
    print(html)
    input("按回车退出")