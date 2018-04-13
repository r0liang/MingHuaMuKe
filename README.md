# 名华慕课网模拟登陆、刷课、做题，新坑

###项目所用版本：Python3

###项目所需库
> * requests
> * execjs
> * ctypes

###项目进度
- [x] Python使用网页JS的TOKEN模拟计算
- [x] JS做了点轻微改造能够直接计算STR TOKEN
- [x] Python稳定模拟访问
- [x] 模拟JS观看过程的二倍速和静音处理
- [x] 代码模块化
- [ ] 自动刷课
- [ ] 自动做题
- [ ] 登陆以后获取课程列表（未上传）
- [ ] 登陆以后进入课程
- [ ] 登陆以后课程模拟观看(调用DLL，未上传）
- [ ] SSESION验证码获取
- [ ] Cookie和验证码变化规律

###名华慕课播放器操作JS
```
$(".jwmute").find("button").trigger("click") #静音
$jwplayer().getState() #获取播放状态
$jwplayer().getDuration() #获取总时长
$("#mediaplayer_controlbar_rate_option_2").trigger("click") #调速
```
