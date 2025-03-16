from dotenv import load_dotenv  
import os  

load_dotenv()  # Load environment variables  

# Access and print the variables  
REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")  
REDSHIFT_USER = os.getenv("REDSHIFT_USER") 
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")  
REDSHIFT_DB = os.getenv("REDSHIFT_DB")  
REDSHIFT_SCHEMA = os.getenv("REDSHIFT_SCHEMA") 


print(f"REDSHIFT_HOST URL: {REDSHIFT_HOST}")  
print(f"REDSHIFT_USER: {REDSHIFT_USER}")
print(f"REDSHIFT_PASSWORD: {REDSHIFT_PASSWORD}")
print(f"REDSHIFT_DB: {REDSHIFT_DB}")
print(f"REDSHIFT_SCHEMA: {REDSHIFT_SCHEMA}")