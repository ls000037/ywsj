request_address: 172.16.1.211:59251
response_address: 113.107.216.27:80
GET /n/report/report.xml HTTP/1.1
Host: i.kpzip.com
Accept: */*

HTTP/1.1 404 Not Found
Server: NWS_TCloud_S2
Connection: keep-alive
Date: Mon, 09 Apr 2018 06:47:42 GMT
Content-Type: text/html
Content-Length: 71
X-NWS-LOG-UUID: 570b3600-e167-445a-be93-f1bad98ce5cc f4775dcd310710e28b8931edc24b0d7f
X-Cache-Lookup: Hit From 404 Cache 

The requested URL '/n/report/report.xml' was not found on this server.



