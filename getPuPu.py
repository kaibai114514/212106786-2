from time import strftime, sleep
import requests

def getPuPu():
    #标头
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) '
                     'Chrome/53.0.2785.143 Safari/537.36 '
                     'MicroMessenger/7.0.9.501 NetType/WIFI '
                     'MiniProgramEnv/Windows WindowsWechat'
    }
    proxies={'htttp':None,'https':None}
    #要爬取的地址
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/35a6b493-9d14-4945-9f66-719a47e80210'
    #定义循环判定
    isRun=True
    #get方法发送请求,用response接收
    response=requests.get(url=url,headers=headers,proxies=proxies)
    #把接收的response用json方法转成json对象
    json_text = response.json()
    #判断是否有该产品
    if(json_text['errcode']!=400001):
        name = json_text['data']['name']
        spec = json_text['data']['name']
        price = str(int(json_text['data']['price'])/100)
        sub_title = json_text['data']['sub_title']
        market_price=str(int(json_text['data']['market_price'])/100)
        print("----------------商品名称:"+name+"----------------")
        print("规格:"+spec)
        print("价格:"+price)
        print("原价/折扣价:"+market_price+"/"+price)
        print("详细内容:"+sub_title)
        print("----------------"+name+"的价格波动"+"----------------")
    else:
        print(json_text['errmsg'])
        isRun=False
    #循环
    while(isRun):
        #发送请求
        response=requests.get(url=url,headers=headers,proxies=proxies)
        #转成json对象
        json_text = response.json()
        #判断是否有该产品
        if(json_text['errcode']!=400001):
            name = json_text['data']['name']
            price = str(int(json_text['data']['price'])/100)
            #获得当前时间
            time=strftime('%Y-%m-%D-%H:%M:%S')
            print(time+"--"+name+"--"+price+"")
            #睡眠10秒
            sleep(1)
        else:
            isRun=False
            print(json_text['errmsg'])

if __name__=="__main__":
    getPuPu()