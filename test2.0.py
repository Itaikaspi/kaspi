import httpx

result = httpx.get("http://ifconfig.co/ip")
print(result.text)
