import time
import urllib.request

def health_check():
    print(f"start to check beggar")
  
    url = "https://beggar.onrender.com/health"
    while True:
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                status_code = resp.getcode()
                body = resp.read().decode("utf-8", errors="ignore")
                print(f"[{time.ctime()}] 请求成功，状态码：{status_code}, 响应：{body}")
        except Exception as e:
            print(f"[{time.ctime()}] 请求异常：{str(e)}")
        # 等待60秒
        time.sleep(60)

if __name__ == "__main__":
    health_check()
