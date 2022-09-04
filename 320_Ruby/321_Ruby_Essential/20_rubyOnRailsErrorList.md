# Error List를 만들어보자
* [001 : TZInfo::DataSourceNotFound](#001---tzinfodatasourcenotfound)
* [02. ](#2)
* [03. ](#3)
    001 - TZInfo::DataSourceNotFound
    
## 001 - TZInfo::DataSourceNotFound
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

