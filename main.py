import langconv
import os
# import chardet
from bs4 import UnicodeDammit


def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = langconv.Converter('zh-hans').convert(sentence)
    return sentence


if __name__ == "__main__":
    file_list = os.listdir()
    if file_list.count('chs') == 0:
        os.mkdir('./chs')
    file_list = [x for x in file_list if os.path.isfile(x) and (os.path.splitext(x)[1] == '.ass' or os.path.splitext(x)[1] == '.srt')]
    print(file_list)

    for i in file_list:
        # 以二进制读入数据
        with open(i, 'rb') as b:
            buf = b.read()
        # result = chardet.detect(buf)
        # 解析编码
        result2 = UnicodeDammit(buf)
        print('Encoding: ', result2.original_encoding)
        with open(i, 'r', encoding=result2.original_encoding, errors='ignore') as text:
            text_all = text.read()
            #print(text_all)
        with open(os.path.join('./chs', i), 'w', encoding=result2.original_encoding, errors='ignore') as text:
            text.write(Traditional2Simplified(text_all))
        print(i, ' is converted')
    print('Success!')