"""
Leaderboard 테이블 모델
: 사용자 순위 정보를 저장
"""

from sqlalchemy import Column, Integer, ForeignKey
from . import Base

class Leaderboard(Base):
    __tablename__ = 'leaderboard'

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        primary_key=True,
        comment="User 테이블의 id 참조"
    )  # 1:1 순위 정보 저장

    rank = Column(
        Integer,
        nullable=False,
        comment="현재 순위"
    )

    total_steps = Column(
        Integer,
        nullable=False,
        comment="총 걸음 수"
    )