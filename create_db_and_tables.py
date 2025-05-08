"""
MySQL 정보를 입력받아 데이터베이스와 테이블을 생성하는 스크립트
"""
import os
import sys
import getpass

# 프로젝트 루트 경로를 sys.path에 추가
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root_dir)

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from models import Base


def main():
    print("=== Runipet_DB DB 및 테이블 생성 ===")
    host = input("MySQL 호스트 (예: localhost): ").strip()
    port = input("MySQL 포트 (기본 3306): ").strip() or "3306"
    user = input("MySQL 사용자명: ").strip()
    password = getpass.getpass("MySQL 비밀번호: ")
    db_name = input("생성할 데이터베이스명: ").strip()

    # DB 생성
    try:
        url0 = f"mysql+pymysql://{user}:{password}@{host}:{port}/"
        engine0 = create_engine(url0)
        with engine0.connect() as conn:
            conn.execute(
                f"CREATE DATABASE IF NOT EXISTS `{db_name}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
            )
        print(f"- 데이터베이스 '{db_name}' 생성 또는 확인 완료.")
    except SQLAlchemyError as e:
        print("[오류] 데이터베이스 생성 실패:", e)
        return

    # 테이블 생성
    try:
        url1 = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
        engine1 = create_engine(url1)
        Base.metadata.create_all(engine1)
        print("- 모든 테이블 생성 완료.")
    except SQLAlchemyError as e:
        print("[오류] 테이블 생성 실패:", e)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()