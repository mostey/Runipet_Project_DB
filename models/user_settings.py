"""
UserSettings 테이블 모델
: 사용자별 앱 환경 및 알림 설정 저장
"""

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from . import Base

class UserSettings(Base):
    __tablename__ = 'user_settings'

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        primary_key=True,
        comment="User 테이블의 id 참조"
    )  # 1:1 관계

    goal_steps = Column(
        Integer,
        default=10000,
        comment="하루 목표 걸음 수"
    )

    theme_id = Column(
        Integer,
        ForeignKey('theme.id'),
        comment="선택된 테마 ID"
    )

    today_steps = Column(
        Integer,
        default=0,
        comment="금일 누적 걸음 수"
    )

    hunger_notify = Column(
        Boolean,
        default=True,
        comment="배고픔 알림 여부"
    )

    growth_notify = Column(
        Boolean,
        default=True,
        comment="성장 알림 여부"
    )

    motivation_notify = Column(
        Boolean,
        default=True,
        comment="동기부여 메시지 수신 여부"
    )

    friend_notify = Column(
        Boolean,
        default=True,
        comment="친구 요청 알림 여부"
    )

    leaderboard_notify = Column(
        Boolean,
        default=True,
        comment="리더보드 알림 여부"
    )

    bgm_enabled = Column(
        Boolean,
        default=True,
        comment="배경 음악 활성화 여부"
    )