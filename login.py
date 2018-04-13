# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2017-06-03 14:55:17
# @Last Modified by:   Marte
# @Last Modified time: 2018-04-13 15:56:47
#coding=utf-8
# -*-coding:utf-8-*-

import sys
import os
import requests
import re
import execjs
import time
#def login(loginName,strToken,loginType,isCheckCode,checkCode,historyUrl,lang):


#def GetStrToekn(key,token):


#def GetToekn(tokenid,passwd):

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




if __name__ == '__main__':
    print('loading')
    loginurl = 'http://bwgl.minghuaetc.com/home/login.mooc'
    loginheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Language':'zh-CN',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive'}
    req=requests.get(loginurl,headers=loginheaders)
    t=time.time()
    t=int(round(t * 1000))
    html=req.text
    lang="zh_CN"
    Exponents=str(GetExponent(html).encode(),encoding='utf-8')
    Moduluss=str(GetModulus(html).encode(),encoding='utf-8')
    Tokenid=str(GetTokenID(html).encode(),encoding='utf-8')
    id=input("账号:")
    passwd=input("密码:")
    Token=Tokenid+"/\n"
    print("时间戳校准"+str(t))
    check=input("输入目录下验证码:")
    print('Rsaing the Key')
    jsstr = get_js()
    ctx = execjs.compile(jsstr)
    datakey=ctx.call("RSAKeyToken",Token,Exponents,"",Moduluss)
    loginurl="http://bwgl.minghuaetc.com/home/doLogin.mooc"
    d={
    'loginName':id,
    'strToken':datakey,
    'loginType':1,
    'isCheckCode':0,
    'checkCode':check,
    'historyUrl':'null',
    'lang':lang
    }
    req=requests.post(loginurl,headers=loginheaders,data=d)
    html=req.text
    print(html)
    input("按回车退出")





#def init():
#    print('2')
#    return;

#def two():
#    print('3')
#    return;

#print('1')
#init()
#two()
#list = ['a','b','c','d','e']
#par = {'1','2','3','4'}
#print(list[4]);
#if ('超星' in par):
#    print('在');
#else:
#    print('N');

#a=set('aaaavbbbbb')
#b=set('dcaaaaaaa')

#print(a-b)

#a='aaaa'
#print(a.capitalize())  #转大写
#
#a, b = 0, 1
#while b < 10:
#    print(b)
#   a, b = b, a+b
#

#age=int(input("输入点什么"))

#print("")
#if age>=10:
#    print("你输入的数字加10 = ",age+10)
#else:
#    print("你输入的数字*20= ",age*20)

#input("敲下ENTER退出")
#
#

#sites = ["Baidu", "Google","Runoob","Taobao"]
#for site in sites:
#    if site == "Runoob":
#        break
#    print(site)
#
#
#sites = ["Baidu", "Google","Runoob","Taobao"]
#for site in sites:
#    if site == "Runoob":
#        print("菜鸟教程!")
#        break
#    print("循环数据 " + site)
#else:
#    print("没有循环数据!")
#print("完成循环!for i in range(5):

#    print(i)
#
#for i in range(-12,2):
#    print(i)
#
