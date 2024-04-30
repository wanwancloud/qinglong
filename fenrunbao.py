import requests, os, time, random, re


class yuanshen():
    def __init__(self) -> None:
        self.headers = {
            "Host": "lfb.ihuju.cn",
            "Connection": "keep-alive",
            "Content-Length": "188",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://lfb.ihuju.cn",
            "Referer": "http://lfb.ihuju.cn/index.php/Home/Fenrun/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        self.cookies = {
            "BJYADMIN": "lhdgqh13qlms2d1to95kge52j6",
            "token": "a9a863f54dfe55e9cb82e538269f6f64"
        }
        self.getkey()

    def getkey(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "http://lfb.ihuju.cn/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        }
        url = "http://lfb.ihuju.cn/index.php/Home/Fenrun/index.html"
        r = requests.get(url, headers=headers, cookies=self.cookies)  # 获取页面内容
        if r.status_code == 200:
            rule = r'\$\.\w+\(url,{([^:]+)'  # 匹配以字母或下划线开头的变量名，冒号，以及冒号后的内容（直到逗号或右括号为止）
            match = re.search(rule, r.text)
            if match:
                key = match.group(1)
                print("匹配到的key：", key)
                self.key = key
            else:
                print("未找到匹配的key")
        else:
            print("请求失败，状态码：", r.status_code)

    def watch_video(self):  # 看广告
        i = 1
        while True:
            url = "http://lfb.ihuju.cn/index.php/Home/Fenrun/sign.html"  # 广告页面url
            data = f"{self.key}={i}"
            r = requests.post(url, headers=self.headers, data=data, cookies=self.cookies).json()  # 提交广告请求
            if r['status'] == 1:
                print(f"领取第[{i}]级奖励成功")
            else:
                print(f"领取第[{i}]级奖励失败----[{r['info']}]")
                if r['info'] != "请在刷新页面重试":
                    break
            time.sleep(random.randint(65, 80))
            i += 1
            if i == 39:  # 最多38次 第39次就没了
                break


main = yuanshen()
main.watch_video()
