import os
from dotenv import load_dotenv

load_dotenv()
a= os.getenv('KAFKA_SERVER')
print(a)