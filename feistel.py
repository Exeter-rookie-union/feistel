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


def bitwise_and(left_text_list, right_text_list):
    text_length = len(left_text_list)
    r = 0
    bitand_list_result = []
    while r < text_length:
        if left_text_list[int(r)] == "1" and right_text_list[int(r)] == "1":
            bitand_list_result.append("1")
        else:
            bitand_list_result.append("0")
        r += 1
    return bitand_list_result


def xor(left_text_list, right_text_list):
    text_length = len(left_text_list)
    m = 0
    xor_list_result = []
    while m < text_length:
        if left_text_list[int(m)] == right_text_list[int(m)]:
            xor_list_result.append("0")
        else:
            xor_list_result.append("1")
        m += 1
    return xor_list_result


def encrypt(input, rounds, roundkeys):
    # TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
    global ciphertext_result
    plaintext = re.findall(r'.{4}', input)

    i = 0
    while i < int(rounds):
        plaintext_swap_str = re.findall(r'.{4}', ''.join(plaintext))
        bot_text = plaintext_swap_str[0]
        top_text = re.findall(r'.{1}', plaintext_swap_str[1])
        # 轮key
        rkey = roundkeys[int(i)]
        rkeyi = re.findall(r'.{1}', rkey)
        i += 1
        # bit wise and 运算
        bitand_result_list = bitwise_and(top_text, rkeyi)
        bot_text_str = re.findall(r'.{1}', bot_text)
        # left-w 与 right-w 异或
        xor_reult_list = xor(bot_text_str, bitand_result_list)
        plaintext_swap = top_text + xor_reult_list
        plaintext = ''.join(plaintext_swap)
        ciphertext = xor_reult_list + top_text
        ciphertext_result = ''.join(ciphertext)

    return ciphertext_result


def decrypt(input, rounds, roundkeys):
    # TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
    global plaintext_reult
    ciphertext = re.findall(r'.{4}', input)
    i = 0
    while i < int(rounds):
        # 将加密文本分成2份，left-w and right-w
        ciphertext_swap_str = re.findall(r'.{4}', ''.join(ciphertext))
        bot_text = ciphertext_swap_str[0]
        top_text = re.findall(r'.{1}', ciphertext_swap_str[1])
        # 轮key
        rkey = roundkeys[int(rounds)-1 - int(i)]
        rkeyi = re.findall(r'.{1}', rkey)
        i += 1
        bitand_result_list = bitwise_and(top_text, rkeyi)
        bot_text_str = re.findall(r'.{1}', bot_text)
        # left-w 与 right-w 异或
        xor_reult_list = xor(bot_text_str, bitand_result_list)
        ciphertext_swap = top_text + xor_reult_list
        ciphertext = ''.join(ciphertext_swap)
        plaintext = xor_reult_list + top_text
        plaintext_reult = ''.join(plaintext)

    return plaintext_reult


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')

try:
    input = args.pop(0)
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
    raise SystemExit("input is not a valid bit string")

try:
    rounds = int(args.pop(0))
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
    raise SystemExit("rounds is not a valid number")

if (len(args) < rounds):
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys = args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
    raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
    result = decrypt(input, rounds, roundkeys)
else:
    result = encrypt(input, rounds, roundkeys)

print(result)
