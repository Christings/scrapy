from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from quora import settings
from .models import Question, Answer, Topic, Merged, Topics, BaseModel


class Mysql():

    def __init__(self):
        self.question = Question()
        self.answer = Answer()
        self.engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8&use_unicode=0".format(
            settings.MYSQL_USER, settings.MYSQL_PASSWD, settings.MYSQL_HOST, settings.MYSQL_DB))
        self.DB_Session = sessionmaker(bind=self.engine, autocommit=True)
        self.session = self.DB_Session()
        BaseModel.metadata.create_all(self.engine)

    def init_db(self):
        BaseModel.metadata.create_all(self.engine)

    def drop_db(self):
        BaseModel.metadata.drop_all(self.engine)

    def insert_question(self, item):
        question = Question(url=item['url'], question=item['question'], question_details=item[
                            'question_details'], answer_count=item['answer_count'])
        self.session.add(question)
        try:
            self.session.flush()
        except:
            time.sleep(0.01)

 #   def insert_html(self,html_id,html):
 #       html = Html(html_id=html_id,html=html)
 #       self.session.add(html)
 #       try:
 #           self.session.flush()
 #       except:
 #           time.sleep(0.01)

    def insert_answer(self, question_id, update_on, item):
        answer = Answer(question_id=question_id, id=item['id'], update_on=update_on, answer_rank=item['rank'], time=item['time'], views=item[
                        'views'], temp1=item['upvote'], content=item['content'], author=item['author'], author_url=item['author_url'])
        self.session.add(answer)
 #       self.session.commit()
        self.session.flush()
 #       logging.info('insert answer success')

    def get_question_id(self, urls):
        url = "http:" + urls
        question = Question()
        question_id = self.session.query(Question).filter_by(url=url).first()
        try:
            if question_id.question_id:
                return question_id.question_id
        except:
            url = "https:" + urls
            question_id = self.session.query(
                Question).filter_by(url=url).first()
            return question_id.question_id

 #   def get_html_id(self,html_id):
 #       html = Html()
 #       html = self.session.query(Html).filter_by(html_id=html_id).first()
 #       try:
 #           if html.html_id:
 #               return True
 #       except:
 #           return False

 #   def update_html(self,html_id,html):
 #       html = Html()
 #       html = self.session.query(Html).filter_by(html_id=html_id).first()
 #       html.html=html
 #       try:
 #           self.session.flush()
 #       except:
 #           pass

    def get_id_by_question(self, question):
        question = self.session.query(
            Question).filter_by(question=question).first()
        return question.question_id

    def update_question(self, item, id):
        answer = self.session.query(Question).filter_by(question_id=id).first()
        answer.question = item['question']
        answer.question_details = item['question_details']
        answer.answer_count = item['answer_count']
        try:
            self.session.flush()
        except:
            time.sleep(0.01)

    def update_answer(self, item, answer_id, update_on):
        answer = self.session.query(Answer).filter_by(id=answer_id).first()
        answer.answer_rank = item['rank']
        answer.time = item['time']
        answer.views = item['views']
        answer.temp1 = item['upvote']
        answer.content = item['content']
        answer.author = item['author']
        answer.update_on = update_on
        answer.author_url = item['author_url']
        self.session.flush()
        # logging.info('update answer success and id is : %s'%answer_id)

    def insert_topic(self, topic):
        topic = Topic(topic=topic)
        self.session.add(topic)
        try:
            self.session.flush()
        except:
            time.sleep(0.01)

    def get_topic_id(self, topic):
        top = Topic()
        topic = self.session.query(Topic).filter_by(topic=topic).first()
        try:
            return topic.topic_id
        except:
            return 0

    def insert_topics(self, question_id, topic_id):
        topics = Topics(question_id=question_id, topic_id=topic_id)
        try:
            self.session.add(topics)
            self.session.flush()
        except:
            time.sleep(0.01)

    def insert_merged(self, question_id, merged_url, merged_question):
        merged = Merged(question_id=question_id,
                        merged_url=merged_url, merged_question=merged_question)
        try:
            self.session.add(merged)
            self.session.flush()
        except:
            time.sleep(0.01)
