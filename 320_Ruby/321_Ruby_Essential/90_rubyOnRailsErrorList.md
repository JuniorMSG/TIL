# Error List를 만들어보자
* [TZInfo::DataSourceNotFound](#tzinfodatasourcenotfound)
* [Routing Error](#routing-error)
* [03. ](#3)
    001 - TZInfo::DataSourceNotFound
    
## TZInfo::DataSourceNotFound
### 발생경위 및 메세지  
    Window에서 실행시 발생하는 에러로 보인다.
    `rescue in create_default_data_source': tzinfo-data is not present.
    Please add gem 'tzinfo-data' to your Gemfile and run bundle install (TZInfo::DataSourceNotFound)

### 해결방법
    # Windows does not include zoneinfo files, so bundle the tzinfo-data gem
    Gemfile의 tzinfo, tzinfo-datad를 아래처럼 수정해준뒤 
    gem 'tzinfo'
    gem "tzinfo-data"
    실행하면 잘 된다.
![img_1](https://user-images.githubusercontent.com/22822369/186692001-70083037-994c-4703-a51a-549c9f981384.png)




## Routing Error
![image](https://user-images.githubusercontent.com/22822369/188320192-92d7709b-4606-4c92-834b-1f724cb8253e.png)


### 발생경위 및 메세지  
    No route matches [POST] "/result"
    GET만 만들고 POST를 만들지 않아서 생기는 에러

### 해결방법
     routes.rb 파일에 post를 추가한다.
![image](https://user-images.githubusercontent.com/22822369/188320568-d56a9772-189f-4d62-8dcb-7c19828842c3.png)

## InvalidAuthenticityToken
![image](https://user-images.githubusercontent.com/22822369/188320530-aa53d9ae-1b2e-4107-9347-a8adda321426.png)
### 발생경위 및 메세지  
    Can't verify CSRF token authenticity.
    raise ActionController::InvalidAuthenticityToken, warning_message
    ruby에서 post를 사용할 경우 토큰이 없을경우 기본적으로 에러를 발생하게 한다.

### 해결방법
    1. 토큰을 만들어서 전달한다.
    2. application_controller.rb 파일에 코드를 추가한다.

```ruby
# application_controller.rb 파일
class ApplicationController < ActionController::Base
  skip_before_action :verify_authenticity_token, raise: false
end
```
![image](https://user-images.githubusercontent.com/22822369/188320638-02810b80-66fc-43d0-81b0-dc08c42144d6.png)