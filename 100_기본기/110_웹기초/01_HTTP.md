# HTTP(Hyper Text Transfer Protocol)  
* 그냥 문자가 아닌 Hyper 텍스트를 전송하는데 활용하는 프로토콜
* 요청과 응답이 정의됨.

## HTTP Request 메시지 스펙

- 첫째줄: 요청라인(HTTP 메서드(GET, PUT, POST 등)
  - POST : Body로만 통신하자
  - GET : query String으로만 통신하자. 
- 두번째줄부터 줄바꿈 나오기 전까지: Header(User-Agent, Accept 등)
- 헤더에서 줄바꿈 이후: Request Body

```java
POST /create-developer HTTP/1.1
Content-Type: application/json
Accept: application/json

{
  "age" : "24",
  "name" : "MS",
  "id" : JuniorMSG      
}
```

## HTTP Response 메시지 스펙
- 첫째줄: 상태라인(200, 500, 등)
- 두번째줄부터 줄바꿈 나오기 전까지: Header
- 헤더에서 줄바꿈 이후: Request Body

```
HTTP/1.1 200 OK
Content-Type: application/json
Transfer-Encoding: chunked
Date: Sat, 17 Jul 2021 15:33:34 GMT
Keep-Alive: timeout=60
Connection: keep-alive

{
  "age" : "24",
  "name" : "MS",
  "id" : JuniorMSG      
}
```



### Reference
***[wiki](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)***  
***[mozilla](https://developer.mozilla.org/ko/docs/Web/HTTP/Messages)***
