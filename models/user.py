"""
User 테이블 모델
: 사용자 계정 정보를 저장
"""

from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, LargeBinary
from sqlalchemy.sql import func
from . import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="사용자 고유 ID"
    )  # 시스템 내부에서 사용자 식별에 사용

    username = Column(
        String(50),
        unique=True,
        nullable=False,
        comment="로그인 아이디"
    )

    password = Column(
        String(255),
        nullable=False,
        comment="해시 처리된 비밀번호"
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        comment="인증/복구용 이메일"
    )

    nickname = Column(
        String(50),
        nullable=False,
        comment="앱 내 표시 닉네임"
    )

    profile_image = Column(
        LargeBinary,
        nullable=True,
        comment="프로필 이미지(binary)"
    )

    coins = Column(
        Integer,
        default=0,
        nullable=False,
        comment="보유 코인 수"
    )

    role = Column(
        Enum('USER','ADMIN'),
        nullable=False,
        comment="계정 권한"
    )

    is_linked_external = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="외부 서비스 연동 여부"
    )

    registered_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="가입 시각"
    )  # 기본값: 현재 시각