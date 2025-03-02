# from fastapi import Depends, HTTPException
# from sqlalchemy.orm import Session
# from db.session import get_session
# from models.member import Member
# from schemas.member import MyPageUpdate, MyPasswordUpdate, MemberCreate, MemberUpdate, MembersResponse

# def update_me(data: MyPageUpdate, db: Session = Depends(get_session)):
#     db_member = db.query(Member).filter(Member.member_id == data.member_id).first()
    
#     if db_member is None:
#         raise HTTPException(status_code=404, detail="수정 실패")
        
#     db_member.phone = data.phone
#     db.commit()
#     db.refresh(db_member)
    
#     return Member.model_validate(db_member)

# def update_my_password(data: MyPasswordUpdate):
#     pass

# def add_member(data: MemberCreate):
#     with get_session() as db:
#         db_member = Member(
#             name=data.name,
#             emp_no=data.emp_no,
#             phone=data.phone,
#             company_affiliation=data.company_affiliation,
#             position=data.position,
#             employment_status=data.employment_status,
#             role=data.role,
#             birth_date=data.birth_date,
#             hire_date=data.hire_date,
#             resign_date=data.resign_date,
#             resign_reason=data.resign_reason,
#         )
#     db.add(db_member)
#     db.commit()
#     db.refresh(db_member)
#     return db_member

# def get_member(member_id:int):
#     with get_session() as db:
#          return db.query(Member).filter(Member.member_id == member_id).first()

# def get_members(skip: int = 0, limit: int = 10):
#     with get_session() as db:
#         return db.query(Member).offset(skip).limit(limit).all()

# def update_member(data: MemberUpdate):
#     with get_session() as db:
#         db_member = db.query(Member).filter(Member.member_id == data.member_id).first()
#         if not db_member:
#             return None
        
#         db_member.phone = data.phone
#         db.commit()
#         db.refresh(db_member)
#         return Member.model_validate(db_member)
