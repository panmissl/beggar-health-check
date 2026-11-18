import urllib.request
import json

def handler(event, context):
    print(f"start to check beggar")
  
    url = "https://beggar.onrender.com/keepalive"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            code = resp.getcode()
            body = resp.read().decode("utf-8", errors="ignore")
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"ok": True, "status": code, "resp": body})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"ok": False, "error": str(e)})
        }
