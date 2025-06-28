from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://SERVING_NINJAS_owner:npg_OUAZuS0LW2tT@ep-restless-frog-a8opsmw5-pooler.eastus2.azure.neon.tech/SERVING_NINJAS?sslmode=require"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
