## nvm 명령어 

nvm -v			        # nvm 설치되었는지 버전 확인  
nvm list available 	    # 사용가능한 node 버전 확인 (너무 많아서 황급히 껐다)  
nvm list 		        # 설치된 모든 node 버전 확인  
nvm install 16.13.0 	# 특정 node 버전 설치  
nvm use 20.12.2 	    # 사이드 메인 노드
nvm use 16.20.2         # 회사 메인 노드
nvm use 18.18.0         # desktop_ssr 메인 노드
node -v 		        # node 버전 확인  

##
yarn build:development
yarn build:production

rm -rf node_modules yarn.lock
yarn install


