
class Traverse(object):

    def traverseDic(self, dic, key):
        for i in dic:
            if key == i:
                return dic[i]

    def traverseArr(self, arr, key):
        for i in arr:
            if key == i:
                return i


if __name__ == '__main__':
    s = {
        "a": "aa",
        "b": "b"
        }
    a =  Traverse()
    print(a.traverseDic(s, "b"))