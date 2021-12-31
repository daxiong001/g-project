from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib import parse


class Server(object):
    session = None
    isClosed = True
    pwd = parse.quote_plus("IMbSTsEi5J")

    def __init__(self):
        url = "mysql+pymysql://root:{0}@121.4.139.117:32726/test-g-server".format(self.pwd)
        engine = create_engine(url, convert_unicode=True, echo=False, encoding="utf8")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.isClosed = False

    def query(self, type):
        query = self.session.query(type)
        return query

    def add(self, item):
        self.session.add(item)

    def add_all(self, items):
        self.session.add_all(items)

    def delete(self, item):
        self.session.delete(item)

    def commit(self):
        self.session.commit()

    def close(self):
        if self.isClosed:
            pass
        self.session.close()
        self.isClosed = True
