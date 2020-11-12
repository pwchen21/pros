import http.client
conn = http.client.HTTPConnection("www.google.com")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason, r1.msg)
