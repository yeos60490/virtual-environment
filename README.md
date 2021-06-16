## virtual_environment
##### Capstone design project
##### Linux 용 Python 환경 분리 프로그램

-----
- package 충돌 방지 
- 리소스 공유 

-----
### Default Settings
- bashrc 에 다음 내용 추가

      vi /root/.bashrc
      export PATH=$PATH:{프로그램 경로}
      alias consh='/usr/bin/python {프로그램 경로}/consh.py'


-----
### 사용방법
- 환경 출력

      consh env list
      
- 환경 만들기 / 삭제

      consh env create NAME [-option python==version]
      consh env remove NAME
      
      
- 환경 활성화 / 비활성화

      source activate NAME
      source deactivate
      

      

