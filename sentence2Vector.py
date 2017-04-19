#!/usr/bin/python
#encoding=utf-8

# 生成词汇表文件
def gen_vocabulary_file(input_file, output_file):
    vocabulary = {}
    with open(input_file) as f:
        counter = 0
        for line in f:
            counter += 1

            tokens = [word for word in line.strip().decode("utf-8").split("/")]
            for word in tokens:
                if word in vocabulary:
                    vocabulary[word] += 1
                else:
                    vocabulary[word] = 1
        vocabulary_list = START_VOCABULART + sorted(vocabulary, key=vocabulary.get, reverse=True)
        # 取前5000个常用汉字, 应该差不多够用了(额, 好多无用字符, 最好整理一下. 我就不整理了)
        if len(vocabulary_list) > 15662:
            vocabulary_list = vocabulary_list[:15662]
        print input_file + " 词汇表大小:", len(vocabulary_list)
        with open(output_file, "w") as ff:
            for word in vocabulary_list:
                try:
                    ff.write(word.encode("utf-8") + "\n")
                except:continue




# 把对话字符串转为向量形式
def convert_to_vector(input_file, vocabulary_file, output_file):
    tmp_vocab = []
    n = 0
    with open(vocabulary_file, "r") as f:
        tmp_vocab.extend(f.readlines())

    tmp_vocab = [line.strip() for line in tmp_vocab]
    vocab = dict([(x, y) for (y, x) in enumerate(tmp_vocab)])
    # {'硕': 3142, 'v': 577, 'Ｉ': 4789, '\ue796': 4515, '拖': 1333, '疤': 2201 ...}
    output_f = open(output_file, 'w')
    with open(input_file, 'r') as f:
        for line in f:
            line_vec = []
            # for words in line.strip().decode("utf-8"):
            for words in line.strip().split("/"):
                # print words,vocab.get(words, UNK_ID)
                line_vec.append(vocab.get(words, UNK_ID))
            output_f.write(" ".join([str(num) for num in line_vec]) + "\n")
    output_f.close()

if __name__=="__main__":
    train_encode_file = '/home/di/pycharmProjects/medicalRobot_3/data/train.enc'
    train_decode_file = '/home/di/pycharmProjects/medicalRobot_3/data/train.dec'
    test_encode_file = '/home/di/pycharmProjects/medicalRobot_3/data/test.enc'
    test_decode_file = '/home/di/pycharmProjects/medicalRobot_3/data/test.dec'

    print '开始创建词汇表...'
    # 特殊标记，用来填充标记对话
    PAD = "__PAD__"
    GO = "__GO__"
    EOS = "__EOS__"  # 对话结束
    UNK = "__UNK__"  # 标记未出现在词汇表中的字符
    START_VOCABULART = [PAD, GO, EOS, UNK]
    PAD_ID = 0
    GO_ID = 1
    EOS_ID = 2
    UNK_ID = 3
    # 参看tensorflow.models.rnn.translate.data_utils

    vocabulary_size = 15267

    gen_vocabulary_file(train_encode_file, "data/train_encode_vocabulary")
    gen_vocabulary_file(train_decode_file, "data/train_decode_vocabulary")

    train_encode_vocabulary_file = '/home/di/pycharmProjects/medicalRobot_3/data/train_encode_vocabulary'
    train_decode_vocabulary_file = '/home/di/pycharmProjects/medicalRobot_3/data/train_decode_vocabulary'

    print "对话转向量..."

    convert_to_vector(train_encode_file, train_encode_vocabulary_file, 'data/train_encode.vec')
    convert_to_vector(train_decode_file, train_decode_vocabulary_file, 'data/train_decode.vec')

    convert_to_vector(test_encode_file, train_encode_vocabulary_file, 'data/test_encode.vec')
    convert_to_vector(test_decode_file, train_decode_vocabulary_file, 'data/test_decode.vec')

    print "*"*20,"over.","*"*20
