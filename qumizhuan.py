import requests
import time
import random  # 导入这个库

def version():
    txt = requests.get("https://gitee.com/jd_688/zi/raw/master/ziiii.txt").text
    print(txt)
class yuanshen():  # 定义一个类
    def __init__(self) -> None:  # 初始化
        # 这里需要获取时间戳
        self.time = str(int(time.time()))  # 这个是十位时间戳的生成办法
        self.headers1 = {
            "Host": "api.quzanmi.com",
            "Content-Length": "20",
            "x-qzm-time": f"{self.time}",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "Sec-Fetch-Site": "same-site",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "cors",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://h5.quzanmi.com",
            "x-qzm-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3ODM4NSwib3MiOiJpb3MiLCJ0b2tlbl90aW1lIjoxNzE0MjkxMjQ4LCJpYXQiOjE3MTQyOTEyNDgsInN1YiI6InF6bSJ9.4cGJAuTgMcp2H7yj2vYJgIYGfr4cYl43sWA2UMWQrE0",
            "x-qzm-device": "iphone",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) qzm",
            "Referer": "https://h5.quzanmi.com/",
            "x-qzm-bundle": "com.ownershipfre.cn|iPhone14,2|17.3.1|1.1",
            "Sec-Fetch-Dest": "empty",
            "x-qzm-idfa": "2DF76403-7ECB-48F6-8F65-EDB028E55AC9"
        }  # 请求头

        self.headers2 = {
            "Host": "api.quzanmi.com",
            "x-qzm-time": f"{self.time}",
            "Accept": "application/json, text/plain, */*",
            "Sec-Fetch-Site": "same-site",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Mode": "cors",
            "Connection": "keep-alive",
            "Origin": "https://h5.quzanmi.com",
            "x-qzm-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3ODM4NSwib3MiOiJpb3MiLCJ0b2tlbl90aW1lIjoxNzE0MjkxMjQ4LCJpYXQiOjE3MTQyOTEyNDgsInN1YiI6InF6bSJ9.4cGJAuTgMcp2H7yj2vYJgIYGfr4cYl43sWA2UMWQrE0",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) qzm",
            "Referer": "https://h5.quzanmi.com/",
            "x-qzm-bundle": "com.ownershipfre.cn|iPhone14,2|17.3.1|1.1",
            "x-qzm-idfa": "2DF76403-7ECB-48F6-8F65-EDB028E55AC9",
            "Sec-Fetch-Dest": "empty",
            "x-qzm-device": "iphone"
        }


    def watch(self):
        data_list = ["videoad", "videoad2", "videoad3"]
        a = 1
        for i in data_list:
            url = "https://api.quzanmi.com/api/ad/task/reward"
            data = {"source": f"{i}"}
            r = requests.post(url, headers=self.headers1, json=data).json()
            if r['code'] == 2000:
                print(f"🎉 第{a}次用观看视频成功")
            else:
                print(f"❌ 第{a}次观看视频失败---[{r['msg']}]")
            time.sleep(random.randint(30, 60))
            a += 1

    def user(self):
        url = "https://api.quzanmi.com/api/user/info/mine"
        r = requests.get(url, headers=self.headers2).json()
        if r["code"] == 2000:
            coins = int(r["data"]["point"])
            print(f"🎉 今日收益为:{float(r['data']["today_income"])}元\n🎉 当前余额为:{float(r['data']["balance"])}元\n🎉 当前金币剩余:", coins)
            return coins
        else:
            return None
    def trade(self):
        coins = self.user()
        url = "https://api.quzanmi.com/api/user/point/trade"
        data = {"point": coins}
        if coins is not None:
            r = requests.post(url, headers=self.headers2, json=data).json()
            if r["code"] == 2000:
                print(f"🎉 金币兑换成功")
            else:
                print(f"❌ 金币兑换失败---{r['msg']}")
        else:
            print(f"❌ 获取金币信息失败")

version()
main = yuanshen()
#main.watch()
main.trade()