# 간단한 계산기 구현하기
    파라미터를 넘기는 다양한 방법 테스트 해보기


![img_6](https://user-images.githubusercontent.com/22822369/188320108-b60185c1-1a92-4f77-a4a1-8a1bd90abfd5.png)

![image](https://user-images.githubusercontent.com/22822369/188320099-95864b81-bd85-4826-b00e-f5b3a188e68d.png)



## URL로 request 메시지에 담아서 보내는 방법

### routes.rb
```ruby
# URL로 request 메시지에 담아서 보내는 방법
get 'plus/:num1/:num2' => 'home#plus'
```

### home_controller.rb

```ruby
def plus
    @plus_result = params[:num1].to_i + params[:num2].to_i
end
```

### page
![image](https://user-images.githubusercontent.com/22822369/188321064-b027edf3-efcc-4706-a6c2-461c4280a4e4.png)