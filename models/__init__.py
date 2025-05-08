"""
models/__init__.py
: SQLAlchemy Base 선언 및 모델 임포트 파일
"""

from sqlalchemy.orm import declarative_base

# 모든 모델 클래스의 베이스가 되는 객체
Base = declarative_base()

# 테이블 모델 임포트 (추가/삭제 시 여기서 관리)
from .user import User
from .user_settings import UserSettings
from .theme import Theme
from .pet import Pet
from .pet_stage import PetStage
from .pet_status_message import PetStatusMessage
from .exercise_record import ExerciseRecord
from .achievement import Achievement
from .leaderboard import Leaderboard
from .social_relation import SocialRelation
from .pitstop import Pitstop
from .pitstop_visit import PitstopVisit
from .item import Item
from .user_item import UserItem
from .notice import Notice
from .inquiry import Inquiry
from .admin_log import AdminLog