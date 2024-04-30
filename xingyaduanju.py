import requests
#import time
import random

def version():
    txt = requests.get("https://gitee.com/jd_688/zi/raw/master/ziiii.txt").text
    print(txt)
class yuanshen():
    def __init__(self) -> None:
        self.headres = {
            "Host": "app.whjzjx.cn",
            "X-Jiuzhou-Service": "SpeciesBackAdmin",
            "User-Agent": "DreamVideo/2.8.1 (iPhone; iOS 17.3.1; Scale/3.00)",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "X-App-Id": "7",
            "idfa": "2DF76403-7ECB-48F6-8F65-EDB028E55AC9",
            "app_version": "2.8.1",
            "device_id": "2D9248B2-AA28-41AA-9073-1687611E4F6A",
            "channel": "APP Store",
            "uuid": "D3EA439D-84FD-454B-8D69-D9C5D1B5E22E",
            "version_name": "2.8.1",
            "manufacturer": "apple",
            "platform": "2",
            "Connection": "keep-alive",
            "oaid": "2D9248B2-AA28-41AA-9073-1687611E4F6A",
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU2NTc5MDIsIlVzZXJJZCI6NDQ3Mzg3MjMsInJlZ2lzdGVyX3RpbWUiOiIyMDI0LTA0LTI5IDExOjM3OjQ4IiwiaXNfbW9iaWxlX2JpbmQiOnRydWV9.tMIRg0NrHgGr3pmwC2uqPM_DvCwSsw5CxV_KoF1IH0M",
            "Accept-Language": "zh-Hans-CN;q=1",
            "os_version": "17.3.1",
            "device_platform": "ios",
            "Accept": "*/*",
            "device_type": "",
            "device_brand": "iPhone14,2",
            "Accept-Encoding": "gzip, deflate, br",
            "dev_token": "BW3ZBgbJQ-igyEQo5SE0bkwB4_CNK5s-IlXMLV9chWDM5kXEDpH-ryUlNpnLKNnBg8rjq-eHYe9O0_6vvgiBJ8acbXx-TU4QwVjFXNpoWNNuXbcUWtxYe0un66jr67KMOG_XU9X8kuwFGUr07JToEjn-r2T57ZYmr5D6YhUyhjkk*"
            }

        self.headres2 = {
            "Host": "speciesweb.whjzjx.cn",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Sec-Fetch-Mode": "cors",
            "app_version": "2.8.1",
            "device_id": "2D9248B2-AA28-41AA-9073-1687611E4F6A",
            "channel": "APP Store",
            "Origin": "https://h5static.jzjxwh.cn",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Site": "cross-site",
            "Content-Length": "10",
            "Connection": "keep-alive",
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU2NTc5MDIsIlVzZXJJZCI6NDQ3Mzg3MjMsInJlZ2lzdGVyX3RpbWUiOiIyMDI0LTA0LTI5IDExOjM3OjQ4IiwiaXNfbW9iaWxlX2JpbmQiOnRydWV9.tMIRg0NrHgGr3pmwC2uqPM_DvCwSsw5CxV_KoF1IH0M",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "os_version": "17.3.1",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "device_platform": "ios",
            "device_brand": "iPhone14,2",
            "device_type": "",
            "dev_token": "BW3ZBgbJQ-igyEQo5SE0bkwB4_CNK5s-IlXMLV9chWDM5kXEDpH-ryUlNpnLKNnBg8rjq-eHYe9O0_6vvgiBJ8acbXx-TU4QwVjFXNpoWNNuXbcUWtxYe0un66jr67KMOG_XU9X8kuwFGUr07JToEjn-r2T57ZYmr5D6YhUyhjkk*"
            }
    def user(self):
        url = "https://app.whjzjx.cn/v1/account/detail"
        r = requests.get(url, headers=self.headres).json()
        if r["code"] == "ok":
            print(f"🎉获取用户信息成功\n🎉当前金币数量:{r["data"]["species"]}\n🎉当前余额:{r["data"]["cash_remain"]}")
        else:
            print(f"获取用户信息失败---{r["msg"]}")

    def money(self):
        pass

version()
main = yuanshen()
main.user()


