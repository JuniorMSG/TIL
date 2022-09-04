# 기본 페이지 호출하기
    HTML / CSS / JavaScript
    Model / Controller / View 
    
## 기본적인 페이지 구성 
    3가지가 중요하다. 
    
    Controller
    View 

### routes.rb
    # 주소로 처음 들어가면 HomeController 에서 index 엑션에 연결해주세요
    root 'home#index'
    get '/' => 'home#index'
![image](https://user-images.githubusercontent.com/22822369/186712294-89592117-051d-4f0e-9da7-0e364e4c387d.png)  
![image](https://user-images.githubusercontent.com/22822369/186714624-a9c35f07-4da4-484d-ad00-449fcbaa944c.png)  
### Controller 생성
    rails generate controller home
![image](https://user-images.githubusercontent.com/22822369/186712667-c617aee1-4c36-44ca-a9a0-b42323d7be5e.png)  

#### 코드
    class HomeController < ApplicationController
        # index 라는 엑션을 만든 것
        def index
        end
        
        def hi
            @message = "돔황챠~"
            @showMessage = "사랑해~"
        end
    end


#### 위치
    app/controllers/xxx_controller.rb 형태로 존재
![image](https://user-images.githubusercontent.com/22822369/186712803-364d4c58-23b1-4dcc-a511-65f749fd66af.png)

### View
    app/views/xxx.erb 형태로 존재
![image](https://user-images.githubusercontent.com/22822369/186713524-932ed7a0-a9e2-498b-8362-c93b8f6c146b.png)

#### index.erb
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello World</title>
    </head>
    <body>
      Hello Ruby On Rails World
    </body>
    </html>

#### hi.erb
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>HIHI</title>
    </head>
    <body>
      HIHI~ Ruby On Rails World
      <p><%= @message %></p>
    
    <% if true %>
      <p>  <%= @shoeMessage %> </p>
      <% end %>
    </body>
    </html>

## 결과
![image](https://user-images.githubusercontent.com/22822369/186714414-068ec61e-4243-4541-a0af-fbc9d217c78d.png)
![image](https://user-images.githubusercontent.com/22822369/186715363-e33c4668-d50c-4ad5-87bc-d7ca0734b647.png)