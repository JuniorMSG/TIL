## Error
git add . not use
git status 
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  (commit or discard the untracked or modified content in submodules)
        modified:   01_StudyBasic/Lotto (modified content)


![image](https://user-images.githubusercontent.com/22822369/149666700-364d6979-61eb-45d1-b0fe-636d6f583417.png)


## Fix
```
// .git 파일 찾기

    find . -name '.git'             // ALL
    find . -mindepth 2 -name '.git' // Level 2 ~ ALL 
```
![image](https://user-images.githubusercontent.com/22822369/149666745-d9cc3eab-e1ac-4df9-a584-f3ff272c8732.png)

```
    // 하위 .git 폴더 삭제
    find ./ -mindepth 2 -name '.git' -prune -exec rm -rf {} +
 ```