"""
PetStatusMessage 테이블 모델
: 성장 단계별 상태 메시지를 저장
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class PetStatusMessage(Base):
    __tablename__ = 'pet_status_message'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="메시지 고유 ID"
    )

    stage_id = Column(
        Integer,
        ForeignKey('pet_stage.id'),
        nullable=False,
        comment="PetStage 테이블의 id 참조"
    )

    message = Column(
        String(255),
        nullable=False,
        comment="펫 상태에 따른 출력 메시지"
    )