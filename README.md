# virtual environment
#### Capstone design project
#### Linux 용 Python 환경 분리 프로그램

-----
- 가상환경 생성/관리/삭제
- package 설치 및 관리 (충돌방지)
- 리소스 공유 (중복 설치 제거)

-----
### Default Settings
- bashrc 에 다음 내용 추가

      vi ~/.bashrc
      export PATH=$PATH:{프로그램 경로}
      alias consh='/usr/bin/python {프로그램 경로}/consh.py'


-----
### 사용방법
- 환경 출력

      consh env list
      
- 환경 만들기 / 삭제

      consh env create NAME [option python==version]
      consh env remove NAME
      
      
- 환경 활성화 / 비활성화

      source activate NAME
      source deactivate
      
      
- 패키지 설치/삭제

- 패키지 업데이트/선택

- 파이썬 설치/선택  




