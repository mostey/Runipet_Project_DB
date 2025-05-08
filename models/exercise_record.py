"""
ExerciseRecord 테이블 모델
: 사용자의 운동 기록을 저장
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from . import Base

class ExerciseRecord(Base):
    __tablename__ = 'exercise_record'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="운동 기록 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="사용자 ID 참조"
    )

    steps = Column(
        Integer,
        nullable=False,
        comment="걸음 수"
    )

    calories_burned = Column(
        Float,
        nullable=False,
        comment="소모 칼로리"
    )

    recorded_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="기록 시각"
    )