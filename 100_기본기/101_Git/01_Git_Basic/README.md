# 깃 / 깃허브 ~
* [01. 깃을 사용하는 이유 & 기본 셋팅](git을-왜-사용하는가)
* [02. 기본적인 명령어](기본-명령어)
* [03. branch](branch)


[뒤로](../../README.md)  


## Git을 왜 사용하는가?
    작업한 코드를 기록, 보관 가능
    과거로 되돌리기 가능.
    히스토리 보기 가능!
    범인찾기 가능!(-_-)


### 기본 셋팅
https://git-scm.com/

    여차저차! 설치를 하고~~

### 이메일 및 이름 등록
    git config --global user.email myEmail.naver.com
    git config --global user.name UserName
    


## 기본 명령어
    git add -> staging area -> git commit -> push -> repository 
![img.png](img.png)

### add
|기능|명령어|
|---|---|
|전체추가| git add .|
|파일추가| git add . app.txt|
|복수 파일 추가 |git add app.txt txt.txt|

### commit 
    git commit -m '수정본'

### add + commit
    git commit -a -m '수정본'
    
### 상태보기 
    git status

### 로그보기
    git log --all --oneline

### 기존 버전과 차이점 보기
    개인적으로 이건 불편해서 못쓰겠다.!..
    git diff
    git difftool
#### 툴을 이용하자. 
    git diff, git difftool은 보기 너무 불편해서..
    툴을 이용하는게 좋지 않을까?
    다양한 툴이 있고.. 툴을 사용하면 더 편하게 볼 수 있다.

#### PyCharm, Git
![img_1.png](img_1.png)
![img_2.png](img_2.png)

#### GitKraKen
![img_3.png](img_3.png)

## branch

