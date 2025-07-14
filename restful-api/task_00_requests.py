1.A brief summary explaining the differences between HTTP and HTTPS: HTTPS differ from HTTP with its secure concept that defined with s it means secure. HTTPS secured with ssl/tls encryption for keeping communication secret.
HTTP is not secure so it is vulnerable to evasdropping and other communication attacs.
2.A depiction or outline of the structure of an HTTP request and response: firstly client open tcp connection for sending request to server or intermediate proxy. In this http messages are directly readable by human but http/2 is not readable that is sent to server with same structure for instance
GET / HTTP/1.1
Host: developer.firefox.org
Accept-language: tr
After this action server send a response message to the client like following
HTTP/1.1 200 OK
Date: Sun, 12 Nov 2011 19:50:03 GMT
Server: Apache
Last-Modified: Fri, 03 Jan 2019 20:10:10 GMT
ETag: "gawro-gopakgo-prkkgds-oaktwreop"
Accept-Ranges: bytes
Content-Length: 37287
Content-Type: text/html

<!doctype html>… (here come th37287 bytes of the requested web page)
After response message by server if client wants to end or keep for reusing
3.Lists of common HTTP methods and status codes with their descriptions and possible use cases. For example:

