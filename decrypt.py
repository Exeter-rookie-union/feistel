#!/usr/bin/python3
# coding: utf8
"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""
import sys
import re


def bitwise_and(left_text, right_text):
    text_length = len(left_text)
    r = 0
    list_result = []
    print("进行bit and 运算")
    while r < text_length:
        if left_text[int(r)] == "1" and right_text[int(r)] == "1":
            list_result.append("1")
        else:
            list_result.append("0")
        r += 1
    return list_result


def xor(left_text_list, right_text_list):
    text_length = len(left_text_list)
    m = 0
    list_result = []
    print("进行异或运算")
    while m < text_length:
        if left_text_list[int(m)] == right_text_list[int(m)]:
            list_result.append("0")
        else:
            list_result.append("1")
        m += 1
    return list_result


a = sys.argv
# print(a)

rm = ['feistel.py', '10100000', '5', '0101', '1111', '1010', '0101', '0101']

# rm = ['feistel.py', '10100000', '2', '0101', '1111']

ciphertext = rm[1]
rtime = rm[2]


i = 0

# print(plaintext)
ciphertext = re.findall(r'.{4}', rm[1])
# print(11111111)
# print(plaintext)
ciphertext1 = ''.join(ciphertext)
# print(plaintext1)

while i < int(rtime):

    print("进行第"+ str(i) +"次解密")
    #将加密文本分成2份，left-w and right-w

    # print(111111)
    # print(ctext)
    ciphertext_swap_str = re.findall(r'.{4}', ''.join(ciphertext))
    # print(2222222)
    print(ciphertext)
    print(ciphertext_swap_str)
    bot_text = ciphertext_swap_str[0]
    top_text = re.findall(r'.{1}', ciphertext_swap_str[1])

    print("bot_w：" + bot_text)
    print("top_w: " + str(top_text))

    # i += 1

    #轮key
    print(int(rm[2])+2 - int(i))
    rkey = rm[int(rm[2])+2 - int(i)]
    rkeyi = re.findall(r'.{1}', rkey)
    # print(222222)
    print("第"+ str(i)+ "轮key: " + str(rkeyi))

    i += 1

    list1 = bitwise_and(top_text, rkeyi)
    # r = 0
    # list1 = []
    # print("进行bit and 运算")
    # while r < 4:
    #     # print(r)
    #     # print("")
    #     # print(rtext)
    #     # print(rkeyi)
    #
    #     if top_text[int(r)] == "1" and rkeyi[int(r)] == "1":
    #         # print(111)
    #         list1.append("1")
    #     else:
    #         # print(222)
    #         list1.append("0")
    #     r += 1
    # # print(4444444)
    # print("bit and的运算结果是：" + str(list1))

    bot_text_str = re.findall(r'.{1}', bot_text)
    # print(leftw)
    # print("-----")
    # left-w 与 right-w 异或
    list2 = xor(bot_text_str, list1)
    # m = 0
    # list2 = []
    # print("进行异或运算")
    # while m < 4:
    #     # print(222222)
    #     # print(m)
    #     # print(leftw)
    #     # print(list1)
    #     if bot_text_str[int(m)] == list1[int(m)]:
    #         # print(111)
    #         list2.append("0")
    #     else:
    #         # print(222)
    #         list2.append("1")
    #     m += 1
    #
    # print("异或运算结果是："+ str(list2))


    # print("----====-")
    ciphertext_swap = top_text + list2

    # print(99999)
    print("交换后的明文："+ str(ciphertext_swap))
    ciphertext = ''.join(ciphertext_swap)
    print("交换后的明文str："+ciphertext)
    # plaintext =
    plaintext = list2 + top_text
    print(''.join(plaintext))





