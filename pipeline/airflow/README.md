
# Package install
'''
pip install apache-airflow
'''


# 컨테이너와 마운팅될 디렉토리 생성
'''
mkdir -p ./dags ./logs ./plugins
'''
# 호스트, 컨테이너 파일 권한 설정
'''
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
'''
# DB 계정 생성, 초기화
'''
docker-compose up airflow-init
'''