## MAC
### OO 포트로 시작하는 프로세스 찾기 & 죽이기
    sudo lsof -i :3000  
    sudo kill -9 6918 

## MAC 응용 프로그램 종료
CMD + OPT + ESC

## ps 명령어
ps aux | grep sidekiq


## lsof 명령어
lsof -i :포트번호
kill -9 포트번호로 강제 종료 가능 

