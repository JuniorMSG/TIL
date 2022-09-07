# CRUD
    회원가입 - Create
    로그인 - Read
    회원정보 수정 - Update
    회원 탈퇴 - Delete 등 
    웹에선 다양하게 사용된다.
    기록하고, 읽고, 수정하고, 삭제함.

## rails에서 모델 생성하기
    rails generate model Post를 작성하면
    rails g model post
    3가지 파일이 생선된다.
    * 모델 파일
    * 마이그레이션 파일
        실제 데이터를 넣을 형식을 결정하는 파일
    * 테스트 파일

### 할일 
    rails g model post로 파일을 생성한다.
    config/migrate 폴더의 migration 파일을 수정한다.
    rake db:migrate


## Create
    생성
## Read
    읽기
## Update
    업데이트
## Delete
    삭제
