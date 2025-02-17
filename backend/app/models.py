from sqlalchemy import (
    Column, Integer, String, Text, Boolean, Date, TIMESTAMP, JSON, Enum
)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'

    article_id = Column(Integer, primary_key=True, autoincrement=True, comment='외부문서 고유 ID')
    title = Column(String(100), nullable=False, comment='문서 제목')
    article_type = Column(String(10), comment='NEWS, JOURNAL')
    tags = Column(JSON, comment='태그')
    summary = Column(Text, comment='문서 정보 및 요약')
    source_name = Column(String(100), comment='출처')
    source_url = Column(String(200), comment='출처 url')
    member_id = Column(Integer, nullable=False, comment='작성자 ID')
    published_at = Column(Date, nullable=False, comment='발행일')
    is_public = Column(Boolean, nullable=False, default=True, comment='공개여부')
    is_deleted = Column(Boolean, nullable=False, default=False, comment='삭제여부')
    created_at = Column(TIMESTAMP, nullable=False, comment='등록일시')


class Brand(Base):
    __tablename__ = 'brand'

    brand_id = Column(Integer, primary_key=True, autoincrement=True, comment='브랜드 고유 ID')
    img_id = Column(Integer, nullable=False, comment='이미지 고유 ID')
    brand_eng = Column(String(50), nullable=False, comment='브랜드명(영어)')
    brand_kor = Column(String(50), nullable=False, comment='브랜드명(한글)')
    brand_intro = Column(String(20), comment='한줄 설명')
    brand_description = Column(String(100), comment='소개글')
    company_type = Column(String(3), nullable=False, comment='APG, APC')
    brand_site_url = Column(String(100), comment='브랜드 사이트 url')
    founded_year = Column(Year, comment='설립연도')
    created_at = Column(TIMESTAMP, nullable=False, comment='등록일시')


class Cosmetic(Base):
    __tablename__ = 'cosmetic'

    cosmetic_id = Column(Integer, primary_key=True, autoincrement=True, comment='화장품 고유 ID')
    brand_id = Column(Integer, nullable=False, comment='브랜드 고유 ID')
    img_id = Column(Integer, nullable=False, comment='이미지 고유 ID')
    product_name = Column(String(100), nullable=False, comment='제품이름')
    product_info = Column(String(100), comment='제품정보')
    capacity = Column(String(30), nullable=False, comment='제품중량')
    specification = Column(String(100), nullable=False, comment='제품 주요 사양')
    expiration_date = Column(String(100), nullable=False, comment='제품 사용기한')
    use_period = Column(Text, nullable=False, comment='사용방법')
    ingredients = Column(JSON, nullable=False, comment='제품 구성성분')
    precaution = Column(String(200), nullable=False, comment='주의사항')
    price = Column(Integer, nullable=False, default=0, comment='제품가격')
    manufacture = Column(String(20), nullable=False, comment='제조사')
    quality_standards = Column(String(100), nullable=False, comment='품질보증기준')
    mfds = Column(String(20), nullable=False, comment='식약처 심사여부')
    created_at = Column(TIMESTAMP, nullable=False, comment='등록일시')


class CosmeticExternal(Base):
    __tablename__ = 'cosmetic_external'

    cometic_id = Column(Integer, primary_key=True, autoincrement=True, comment='화장품 고유 ID')
    img_id = Column(Integer, nullable=False, comment='이미지 고유 ID')
    product_name = Column(String(100), nullable=False, comment='상품명')
    product_info = Column(String(100), comment='제품정보')
    capacity = Column(String(30), nullable=False, comment='제품 중량')
    specification = Column(String(100), nullable=False, comment='제품 주요 사양')
    expiration_date = Column(String(100), comment='제품 사용기한')
    use_period = Column(Text, nullable=False, comment='사용방법')
    ingredients = Column(JSON, nullable=False, comment='제품 구성성분')
    precaution = Column(String(100), nullable=False, comment='주의사항')
    price = Column(Integer, default=0, comment='제품 가격')
    manufacture = Column(String(20), comment='제조사')
    quality_standards = Column(String(100), comment='품질보증기준')
    mfds = Column(String(20), comment='식약처 심사여부')
    created_at = Column(TIMESTAMP, nullable=False, comment='등록일시')

class ImageArticle(Base):
    __tablename__ = 'image_article'
    
    img_id = Column(Integer, primary_key=True, autoincrement=True, comment='이미지 고유 ID')
    article_id = Column(Integer, nullable=False, comment='문서 ID')
    file_path = Column(String(100), nullable=False, comment='파일경로')
    file_name = Column(String(50), nullable=False, comment='파일이름')
    file_extension = Column(String(10), nullable=False, comment='확장자')
    img_type = Column(String(10), nullable=False, comment='THUMBNAIL, CONTENT')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일시')


class ImageBrand(Base):
    __tablename__ = 'image_brand'
    
    img_id = Column(Integer, primary_key=True, autoincrement=True, comment='이미지 고유 ID')
    brand_id = Column(Integer, nullable=False, comment='브랜드 고유 ID')
    file_path = Column(String(100), nullable=False, comment='파일경로')
    file_name = Column(String(50), nullable=False, comment='파일이름')
    file_extension = Column(String(10), nullable=False, comment='확장자')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일시')


class ImageCosmetic(Base):
    __tablename__ = 'image_cosmetic'
    
    img_id = Column(Integer, primary_key=True, autoincrement=True, comment='이미지 고유 ID')
    file_path = Column(String(100), nullable=False, comment='파일경로')
    file_name = Column(String(100), nullable=False, comment='파일이름')
    file_extension = Column(String(10), nullable=False, comment='확장자')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일시')


class ImageDoc(Base):
    __tablename__ = 'image_doc'
    
    img_id = Column(Integer, primary_key=True, autoincrement=True, comment='이미지 고유 ID')
    doc_id = Column(Integer, nullable=False, comment='문서 ID')
    file_path = Column(String(100), nullable=False, comment='파일 경로')
    file_name = Column(String(100), nullable=False, comment='파일명')
    file_extension = Column(String(20), nullable=True, comment='파일 확장자')
    img_type = Column(String(10), nullable=False, comment='THUMBNAIL, CONTENT')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일')


class Ingredient(Base):
    __tablename__ = 'ingredient'
    
    ingred_id = Column(Integer, primary_key=True, autoincrement=True, comment='성분 고유 ID')
    ingred_kor = Column(String(100), nullable=False, comment='성분명(한글)')
    ingred_eng = Column(String(100), nullable=False, comment='성분명(영어)')
    cas_no = Column(String(12), nullable=False, comment='CAS No.')
    definition = Column(Text, nullable=False, comment='정의 및 기원')
    synonym = Column(String(100), nullable=True, comment='이명')
    uses = Column(Text, nullable=True, comment='용도')
    caution = Column(Text, nullable=True, comment='주의사항')
    effect = Column(String(20), nullable=True, comment='기능 및 효능')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일시')


class Member(Base):
    __tablename__ = 'member'
    
    member_id = Column(Integer, primary_key=True, autoincrement=True, comment='회원 고유 ID')
    emp_no = Column(String(8), unique_key=True, nullable=False, comment='사원번호호')
    password = Column(String(100), nullable=False, comment='비밀번호')
    name = Column(String(20), nullable=False, comment='직원이름')
    role = Column(INT, nullable=False, comment='시스템관리자-3, 관리자-2, 일반-1')
    position = Column(String(3), nullable=False, comment='회장, 사장, 임원, 과장, 팀장, 대리, 사원, 기타타')
    phone = Column(String(11), nullable=False, comment='휴대폰번호')
    birth_date = Column(Date, nullable=False, comment='생년월일')
    hire_date = Column(Date, nullable=False, comment='입사일')
    employment_status = Column(String(2), nullable=False, default='재직', comment='재직, 휴직, 정직, 퇴직')
    resign_date = Column(Date, nullable=True, comment='퇴사일')
    resign_reason = Column(String(100), nullable=True, comment='퇴사 사유')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, comment='등록일시')
    
# if __name__ == "__main__":