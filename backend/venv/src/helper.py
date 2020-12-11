from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
 
engine = create_engine("postgres://dasiycerkxnazb:e5c496715a3797a8e8490793ebba9c051ba9b8264c796ca685842e892dc6c705@ec2-3-224-188-122.compute-1.amazonaws.com:5432/devetqre66pt27")

def initDatabase():
    sm = sessionmaker(engine)
    session = sm()
    return session

def increaseID():
    pass