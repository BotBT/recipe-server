from passlib.hash import pbkdf2_sha256

from config import Config

# 1. 원문 비밀번호를, 단방향으로 암호화 하는 함수.
def hash_password(original_password):
    password = pbkdf2_sha256.hash(original_password + Config.SALT) 
    # .hash() 암호화 할떄는 해쉬를 적어 괄호안에 넣어준다.
    return password

# 2. 유저가 입력한 비번이, 맞는지 체크하는 함수.
def check_password(original_password, hashed_password):
    check = pbkdf2_sha256.verify(original_password + Config.SALT, hashed_password)
    # verify 검정하는 함수.
    return check

