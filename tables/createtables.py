import os
from urllib import parse


def run():
    password = parse.quote_plus("IMbSTsEi5J")
    args = "sqlacodegen --outfile g_server_models.py mysql+pymysql://root:{0}@121.4.139.117:32726/test-g-server".format(password)
    os.system(args)


if __name__ == '__main__':
    run()
