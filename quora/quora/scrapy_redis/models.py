from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    VARCHAR)

from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()


class Question(BaseModel):
    __tablename__ = 'question'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(1155), nullable=False)
    question = Column(VARCHAR(1255))
    question_details = Column(Text)
    answer_count = Column(Integer, nullable=False, default=0)


class Answer(BaseModel):
    __tablename__ = 'answer'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer, nullable=False, primary_key=True)
    question_id = Column(Integer)
    answer_rank = Column(Integer)
    time = Column(VARCHAR(125))
    views = Column(Integer)
    temp1 = Column(Integer)
    content = Column(Text)
    author = Column(VARCHAR(155))
    author_url = Column(VARCHAR(555))
    update_on = Column(DateTime())


class Topic(BaseModel):
    __tablename__ = 'topic'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    topic_id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(VARCHAR(255))


class Topics(BaseModel):
    __tablename__ = 'topics'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    question_id = Column(Integer, nullable=False, primary_key=True)
    topic_id = Column(Integer, nullable=False, primary_key=True)


class Merged(BaseModel):
    __tablename__ = 'merged_new'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    merged_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, nullable=False)
    merged_url = Column(VARCHAR(1155), nullable=False)
    merged_question = Column(VARCHAR(1155), nullable=False)


# class Html(BaseModel):
#     __tablename__ = 'html'
#     __table_args__ = {
#         'mysql_engine': 'InnoDB',
#         'mysql_charset': 'utf8'
#     }
#     html_id = Column(Integer, primary_key=True)
#     html = Column(Text)
