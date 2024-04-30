import requests, os, time, random, re

def version():
    txt = requests.get("https://gitee.com/jd_688/zi/raw/master/ziiii.txt").text
    print(txt)

class yuanshen():
    def __init__(self) -> None:
        self.headers = {
            "Host": "lfb.ihuju.cn",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
            "Referer": "http://lfb.ihuju.cn/index.php/Home/My/index.html",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Accept-Encoding": "gzip, deflate"
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
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1"
        }
        url = "http://lfb.ihuju.cn/index.php/Home/Fenrun/index.html"
        r = requests.get(url, headers=headers, cookies=self.cookies)
        if r.status_code == 200:
            rule = r'\$\.\w+\(url,{([^:]+)'
            match = re.search(rule, r.text)
            if match:
                key = match.group(1)
                print("匹配到的key：", key)
                self.key = key
            else:
                print("未找到匹配的key")
        else:
            print("请求失败，状态码：", r.status_code)

    def watch_video(self):
        i = 1
        while True:
            url = "http://lfb.ihuju.cn/index.php/Home/Fenrun/sign.html"
            data = f"{self.key}={i}"
            r = requests.post(url, headers=self.headers, data=data, cookies=self.cookies).json()
            if r['status'] == 1:
                print(f"🎉 领取第[{i}]级奖励成功")
            else:
                print(f"🎉 领取第[{i}]级奖励失败----[{r['info']}]")
                if r['info'] != "请在刷新页面重试":
                    break
            time.sleep(random.randint(65, 80))
            i += 1
            if i == 39:
                break

version()
main = yuanshen()
main.watch_video()
