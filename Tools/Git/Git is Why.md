## Git은 무엇인가?
    깃(ɡɪt)은 프로그램 등의 소스 코드 관리를 위한 분산 버전 관리 시스템이다. 
    여러명의 개발자가 특정 프로젝트를 자신의 컴퓨터로 협업하여 개발하면서 버전을 관리할 수 있는 시스템이다.
    과거엔 SVN도 있었다.

### 왜 사용하는가 ?

    작업한 코드를 기록, 보관 가능
    과거로 되돌리기 가능.
    히스토리 보기 가능!
    범인찾기 가능!(-_-)

### 기본 셋팅

https://git-scm.com/

    여차저차! 설치를 하고~~

### 이메일 및 이름 등록

```
git config --global user.email myEmail.naver.com
git config --global user.name UserName
```

### 메인 브렌치 설정

```
git branch -M main
```

### 원격 Repository

    git이 파일 기록하는 장소 .git 폴더에서 관리함
    1. 컴퓨터가 고장나도 안전
    2. 협업에서 필수 

![image](https://user-images.githubusercontent.com/22822369/184626026-fb5694f9-7274-466b-a974-8f011faa466f.png)
![img_15](https://user-images.githubusercontent.com/22822369/184626044-0678f456-a30c-48db-bf2d-1204cfc48f3c.png)

### 기타 사용하기 편리하게 해주는 툴
    Source Tree
    GitKraken
    Fork

![image](https://user-images.githubusercontent.com/22822369/184628489-7f0d8486-214f-4b4d-8f38-e7ee221f6e7f.png)
![image](https://user-images.githubusercontent.com/22822369/184628601-8a377b9c-5563-4503-b74f-5b23a81c5cf2.png)

## 기본 명령어

    git add -> staging area -> git commit -> push -> repository 

![img](https://user-images.githubusercontent.com/22822369/184626073-d25fd5e0-669e-4ed4-98f3-261538d425bd.png)

### 상태보기

    git status

![image](https://user-images.githubusercontent.com/22822369/184629483-620b7b7c-7892-40fc-b862-cf86734f8b96.png)

### add

| 기능       | 명령어                     |
|----------|-------------------------|
| 전체추가     | git add .               |
| 파일추가     | git add . app.txt       |
| 복수 파일 추가 | git add app.txt txt.txt |

![image](https://user-images.githubusercontent.com/22822369/184629608-bf188e55-7caa-4c40-a2f2-e04ee8b96386.png)

### commit

    git commit -m '수정본'

![image](https://user-images.githubusercontent.com/22822369/184629723-1605f9e5-bc24-4792-a0ae-9fe7d4729c60.png)

### add + commit

    git commit -a -m '수정본'

### push

    git push -u 저장소주소 브랜치명
    여러명이 작업할 경우 남이 먼저 push했을 경우 push를 할 수 없다.

![image](https://user-images.githubusercontent.com/22822369/184629774-709dda76-cf4b-492c-bd47-6d5bd583e021.png)

### 되돌리기

| 기능                        | 명령어                            | 주의사항     |
|---------------------------|--------------------------------|----------|
| 최근 커밋시점으로 이동              | git restore                    |          |
| 특정 커밋시점으로 이동              | git restore --source commitID  |          |
| 스테이징 취소                   | git restore --staged aaa.py    |          |
| 커밋 취소                     | git revert commitID1 commitID2 |          |
| 방금 커밋 취소                  | git revert HEAD                |          |
| 특정 시점으로 돌아가며 코드 전부 초기화    | git reset --hard commitID      | 협업시 사용금지 |
| 리셋인데 변동사항 지우지 말고 스테이징 상태  | git reset --soft commitID      |          |
| 리셋인데 변동사항 지우지 말고 언스테이징 상태 | git reset --mixed commitID     |          |

### pull

    git pull 
    git fetch + git merge 라고 생각하면 편함

    fetch - 원격저장소 신규 commit 가져오기
    최신 원격저장소 데이터를 가져온다. 충돌나면 해결은 수동으로.. 

![image](https://user-images.githubusercontent.com/22822369/184629941-e2832e2e-381e-4439-957d-3b45c6fb1c6d.png)

#### 협업

    Settings - Collaborators에 등록해줘야함

![img_16](https://user-images.githubusercontent.com/22822369/184626092-598ee763-c07a-4534-9a0e-ffbd9eeb4cb9.png)

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

![img_1](https://user-images.githubusercontent.com/22822369/184626102-552fa4cc-07db-4057-827b-a928be4b72bb.png)
![img_2](https://user-images.githubusercontent.com/22822369/184626111-75f09a77-6ef6-4e0f-9460-03d3a48ed6bb.png)

#### GitKraKen

![img_3](https://user-images.githubusercontent.com/22822369/184626118-8cd2adbf-78d7-45b4-b055-e1011bf32e6d.png)

[뒤로](README.md)  / [위로](#깃-기본-사용법)

## branch

    기존 코드를 변경하지 않고 복사본을 만들고 작업한다고 생각하면 된다.

### 명령어

| 기능 | 명령어                      |
|----|--------------------------|
| 추가 | git branch feature-#2    |
| 이동 | git switch feature-#2    |
| 삭제 | git branch -d feature-#2 |   

![img_5](https://user-images.githubusercontent.com/22822369/184626135-052e1446-f5e5-451f-a56c-26cc91b0d572.png)

#### 다른 툴에서 보기

![img_6](https://user-images.githubusercontent.com/22822369/184626147-49d02461-3778-4d10-bd15-fe4d20cbd7a5.png)

### 병렬로 진행 후

![img_7](https://user-images.githubusercontent.com/22822369/184626156-8b2beafd-b8fe-40a4-b95a-4d158dcfcbaa.png)

### pull-request

    git push origin pullRequest

![img_17](https://user-images.githubusercontent.com/22822369/184626211-3ef0df7f-6743-4942-ab8d-e7201274a680.png)
![img_18](https://user-images.githubusercontent.com/22822369/184626217-ba3a53f7-08f9-4654-82a9-39c792f5d11c.png)
![img_19](https://user-images.githubusercontent.com/22822369/184626227-6bdfba05-0019-4a28-abed-0c243f805455.png)
![img_20](https://user-images.githubusercontent.com/22822369/184626234-d518600e-2b43-4391-a7c5-3dc17ebf790e.png)

### GitFlow 전략

| 브랜치 종류  | 용도                           | 주의사항 |
|---------|------------------------------|------|
| main    | 나는 메인                        |
| develop | 개발용                          |
| feature | develop에 기능 추가용              |
| release | develop -> main 최종 테스트       |
| hotfix  | main 브랜치에서 버그 발생시 빠른 해결을 위해서 |

<img src="https://user-images.githubusercontent.com/22822369/184626291-63289ed0-bab7-4d3d-a6bb-b09673a91580.png" width="100%" height="100%"/>  

### Trunk - Based 전략

    테스트 코드를 잘 만들어야함. (바로바로 올리니까!..)

<img src="https://user-images.githubusercontent.com/22822369/184626302-eaabd329-d71c-4376-ac65-7047b97c0c08.png" width="100%" height="100%"/>

### CI/CD

    최근 많이 나오는 CI/CD 형식으로 개발하는 곳에서 trunk-based 개발방식을 적용하고..
    그만큼 테스트 코드를 잔뜩 만듭니다.

## Merge

    git branch main
    git merge feature-#2
    다른 파일 수정시 - 정상 엔딩
    같은 파일의 같을 줄 수정시 - 충돌 엔딩 (수동으로 해결해야 한다.)

![img_8](https://user-images.githubusercontent.com/22822369/184626252-897e184a-2dc3-4d28-8f25-0464f271cc62.png)

### 1. 3-way merge

![img_10](https://user-images.githubusercontent.com/22822369/184626263-bed812d4-6b76-4bab-9dd5-bf4e17ddaf3d.png)

### 2. fast-forward merge

![img_11](https://user-images.githubusercontent.com/22822369/184626271-24132037-b39d-45da-a439-15e34f5eddad.png)

### 3. rebase & fast-forward merge

    git branch feature-#2
    git merge main

![img_12](https://user-images.githubusercontent.com/22822369/184626279-7616cb3e-7092-4da3-ae13-cdba215391bb.png)

#### 사용이유

    3-way merge가 너무 많아지면 로그가 복잡하기 때문에..
    간단하고 짧은 브랜치들은 깔끔하게 정리 가능하다. 
    Conflict 가 자주 발생한다.

### 4. squash and merge

    git merge --squash 새브랜치

![img_13](https://user-images.githubusercontent.com/22822369/184626284-8afce76a-c9d3-4abc-9493-abd11116e3a8.png)

#### 사용이유

    로그가 복잡해지기 때문에 사용하는거고..
    간단하고 짧은 브랜치들은 깔끔하게 정리 가능하다. 

### 언제 사용하면 될까요

    프로젝트 가이드에 따라서 사용하면 된다.
    branching/merge 가이드
    안중요한 브랜치는 squash
    feature / develop 브랜치는 3-way merge



## Switch
* 브렌치 변경
    * git switch <브랜치 이름>
* 새로운 브랜치 생성
    * git switch -c <새로운 브랜치 이름> <기준 브랜치 이름>
* 브렌치 삭제
    * git switch -D <삭제할 브랜치 이름>
* 특정 커밋으로 이동
    * git switch <커밋 해시>
* switch 옵션들
    * -c: 새로운 브랜치를 생성할 때 기준 브랜치를 지정합니다.
    * -D: 브랜치를 삭제합니다.
    * -f: 이미 존재하는 브랜치를 강제로 변경합니다.
    * --create-branch: 이미 존재하는 브랜치가 아니라면 새로운 브랜치를 생성합니다.
    * --no-create-branch: 이미 존재하는 브랜치만 변경합니다.

## Stash
git stash  # 변경 사항을 스태싱하기
git rebase branch_name  # 리베이스 수행
git stash pop  # 스태싱된 변경 사항 복원

### Remote 명령어
git remote add msg https://github.com/JuniorMSG/xxx