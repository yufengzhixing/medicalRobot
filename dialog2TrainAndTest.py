#!/usr/bin/python
#encoding=utf-8
'''
聊天语聊的预处理,处理成问答对儿
'''
import jieba

def convert_seq2seq_files():
    f_r = open("/home/di/pycharmProjects/medicalRobot_3/data/processedData.txt")
    train_enc=open("/home/di/pycharmProjects/medicalRobot_3/data/train.enc","w")
    train_dec=open("/home/di/pycharmProjects/medicalRobot_3/data/train.dec","w")
    test_enc=open("/home/di/pycharmProjects/medicalRobot_3/data/test.enc","w")
    test_dec=open("/home/di/pycharmProjects/medicalRobot_3/data/test.dec","w")
    count = 0
    while 1:
        temp_line=f_r.readline()
        if not temp_line:
            break
        if len(temp_line.strip())>0:
#             print(temp_line.strip())
            sentences=temp_line.strip().split("\t")
        else:continue
        
        if len(sentences)>1:
            if (sentences[0][0]=="p") or ((sentences[0][0]=="d") and ("？" in sentences[0] or "吗" in sentences[0])):
                count += 1
                if count <33472:
                    train_enc.write("/".join(jieba.cut(sentences[0][4:])).encode("utf-8")+"\n")
                    train_dec.write("/".join(jieba.cut(sentences[1][4:])).encode("utf-8")+"\n")
                else:
                    test_enc.write("/".join(jieba.cut(sentences[0][4:])).encode("utf-8") + "\n")
                    test_dec.write("/".join(jieba.cut(sentences[1][4:])).encode("utf-8") + "\n")

        else:continue
    
    f_r.close()
    train_enc.close()
    train_dec.close()
    print "处理的总对数儿为：",count

if __name__=="__main__":
    convert_seq2seq_files()

       
    print "*"*20+"end"+"*"*20
