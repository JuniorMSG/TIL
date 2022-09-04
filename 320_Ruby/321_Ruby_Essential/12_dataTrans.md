# 데이터를 전달하는 방법
    1. 변수를 이용해서 전달
    2. form 태그로 request 메시지에 담아서 보낸다.
    3. params로 읽는다.
    4. URL 로 request 메시지에 담아서 보낸다.


## 변수를 이용해서 전달

## form 태그로 전달
    <form method="post" action="/login">
        <input type="text" name="id">
        <input type="password" name="pw">
        <input type="checkbox" name="remember">
        <input type="submit"> 
    </form>

### Method
    Get : URL에 데이터가 노출된다. 보안에 취약
    Post : URL에 데이터가 노출되지 않는다.  
    PUT / Patch :  데이터 수정 (Update)
    Delete: 데이터 삭제 (DELETE)

![image](https://user-images.githubusercontent.com/22822369/186718090-2f264dbe-17ff-45ef-bd1b-7700908cf869.png)


### params로 전달
![img_1](https://user-images.githubusercontent.com/22822369/186719355-fb53505f-b58e-4073-9bf9-caf5c58c786a.png)
## reference 
https://www.youtube.com/watch?v=CegDZIFu9MU
https://www.w3schools.com/html/html_form_input_types.asp
