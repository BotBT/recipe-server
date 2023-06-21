class Config :
   # DB 관련 정보
   HOST = 'yhdb-0609-start.c2hddgxuy03m.ap-northeast-2.rds.amazonaws.com'
   DATABASE = 'recipe_db'
   USER = 'recipe_db_user'
   DB_PASSWORD = '1234'
   
   # 비번 암호화
   SALT = '0417' # password는 config 안에 넣어준다.

   # JWT 변수 셋팅
   JWT_SECRET_KEY = 'hello~!by@'
   JWT_SCCESS_TOKEN_EXPIRES = False
   PROPAGATE_EXCEPTTIONS = True
   