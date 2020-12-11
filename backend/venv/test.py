import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# สร้างคลาสแบบจำลองพื้นฐาน
Base = declarative_base()

# สร้างคลาสตารางฐานข้อมูลนักเรียน
class ACCOUNT(Base):
    __tablename__ = 'ACCOUNT'
    ssn = sqlalchemy.Column('ssn', sqlalchemy.String(13) ,primary_key=True)
    fname = sqlalchemy.Column('fname', sqlalchemy.String(10) )
    lname = sqlalchemy.Column('lname', sqlalchemy.String(10) )
    username = sqlalchemy.Column('username', sqlalchemy.String(15) )
    password = sqlalchemy.Column('password', sqlalchemy.String(15) )
    address = sqlalchemy.Column('address', sqlalchemy.String(50) )
    email = sqlalchemy.Column('email', sqlalchemy.String(30) )
    phoneNumber = sqlalchemy.Column('phoneNumber', sqlalchemy.String(10) )
    birthDay = sqlalchemy.Column('birthDay', sqlalchemy.String(10) )


# สร้างตัวเชื่อมต่อกับฐานข้อมูล sqlite ในไฟล์ yurudata.db
engine = sqlalchemy.create_engine('postgres://dasiycerkxnazb:e5c496715a3797a8e8490793ebba9c051ba9b8264c796ca685842e892dc6c705@ec2-3-224-188-122.compute-1.amazonaws.com:5432/devetqre66pt27')

# ทำการสร้างตารางขึ้นมาในฐานข้อมูล sql จริงๆ
Base.metadata.create_all(engine)

# สร้างเซชชัน
sm = sessionmaker(engine)
session = sm()


# เข้าสู่ขั้นตอนใช้งาน

# สร้างออบเจ็กต์นักเรียนคนแรก
acccount = ACCOUNT(ssn='2321262412421',fname="TestF",lname="TestL", username="tsds",password="fsd",address="dsds",email="sda",phoneNumber="sdasd",birthDay="sds")
# ใส่นักเรียนคนแรกลงในฐานข้อมูล
session.add(acccount)

# บันทึกความเปลี่ยนแปลงลงในฐานข้อมูลจริงๆ
session.commit()