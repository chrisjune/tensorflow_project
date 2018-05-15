import tensorflow as tensorflow
import numpy as np
char_arr =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_dic = {char:index for index, char in enumerate(char_arr)}
print(num_dic)
dic_len = len(num_dic)
seq_data = ['word','wood','deep','dive','cold','cool','load','love','kiss','kind']
input = [num_dic[n] for n in 'word'[:-1]]
#print(input)
#tst=[n for n in 'word'[:-1]]
#print(tst)

def makew