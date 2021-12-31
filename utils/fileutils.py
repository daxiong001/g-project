import configparser
import os
import yaml
import json

from common.filepath import dataBasePath


class ReadFileUtils(object):

    @staticmethod
    def readYaml(filePath, env):
        with open(filePath, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data[env]

    @staticmethod
    def readJson(filePath):
        with open(filePath, encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def readIni(filePath, section, key):
        config = configparser.RawConfigParser()
        if filePath is not None:
            config.read(filePath, encoding='utf-8')
        elif filePath is None:
            raise Exception("文件路径不正确")
        sections = config.sections()
        for i in sections:
            if i == section and i is not None:
                value = config.get(i, key)
                return value
            elif section is None:
                raise Exception("section不能为空")
            elif i != section:
                raise Exception("不存在该section")


if __name__ == '__main__':
    a = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(a)
    b = os.path.join(a, "resources/sc.png")
    #c = ReadFileUtils().readYaml(dataBasePath, "g-server-dev")
    print(b)
