# -*- coding:utf-8 -*-

"""
@author yuyong.zhao
"""
from collections import Counter

def read_file(file_name):
    with open(file_name) as file:
        text = file.read().split()
    return text

def has_punctuation(string):

    """
    判断是否包含标点符号

    大部分标点范围
    u'\u0020-\u007f\u2000-\u206f\u3000-\u303f\uff00-uffef'

    :param string:输入文本
    :return:True or False
    """
    return all(
                0x0020<=ord(ch)<=0x007f or
                0x2000<=ord(ch)<=0x206f or
                0x3000<=ord(ch)<=0x303f or
                0xff00<=ord(ch)<=0xffef
                for ch in string
              )
def is_bi_word(bi_word):
    """
    仅限于汉字二元词组的判断

    :param bi_word:
    :return:
    """
    return (not has_punctuation(bi_word)) and len(bi_word) == 6 # 判断长度为6表示判断两个汉字的词组

def twoTupleWordCnt(text_list, max_count):
    """
    统计二元词组的个数
    :param text: 输入内容
    :param max_count: 最大的前几个词组
    :return: 排名前max_count个二元词组的内容
    """

    two_tuple_list = []
    for i in range(0, len(text_list)):
        cur_ele = text_list[i]
        next_ele = text_list[i+1]
        if is_bi_word(cur_ele) and is_bi_word(next_ele):
            two_tuple_list.append("_".join([cur_ele, next_ele]))
    c = Counter(two_tuple_list)
    return c.most_common(max_count)

def two_tuple_count():
    file_name = "word"
    text_list = read_file(file_name)
    res_list = twoTupleWordCnt(text_list, 10)
    for x in res_list:
        print "[%s] = [%d]" % (x[0], x[1])

two_tuple_count()
