from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("postgresql://postgres:11223344@localhost:5432/car")
auto_commit = engine.execution_options(isolation_level="AUTOCOMMIT")
session: Session = sessionmaker(auto_commit)()
