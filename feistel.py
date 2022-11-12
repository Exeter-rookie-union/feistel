"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""
import sys
import re


def encrypt(input, rounds, roundkeys):
    # TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"

    input = re.findall(r'.{4}', input)
    wl = re.findall(r'.{1}', input[0])
    wr = re.findall(r'.{1}', input[1])
    i = 0
    l = 0

    while rounds != 0:
        roundkeys[i] = re.findall(r'.{1}', roundkeys[i])

        while l < 4:
            wr[l] = (int(wl[l]) & int(roundkeys[i][l])) ^ int(wr[l])
            l += 1

        if rounds != 1:
            wr, wl = wl, wr

        i += 1
        l = 0
        rounds -= 1

    wl = "".join('%s' % id for id in wl)
    wr = "".join('%s' % id for id in wr)
    result = wl + wr

    return result


def decrypt(input, rounds, roundkeys):
    # TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
    input = re.findall(r'.{4}', input)
    wl = re.findall(r'.{1}', input[0])
    wr = re.findall(r'.{1}', input[1])
    i = -1
    l = 0

    while rounds != 0:
        roundkeys[i] = re.findall(r'.{1}', roundkeys[i])

        while l < 4:
            wr[l] = (int(wl[l]) & int(roundkeys[i][l])) ^ int(wr[l])
            l += 1

        if rounds != 1:
            wr, wl = wl, wr

        i -= 1
        l = 0
        rounds -= 1

    wl = "".join('%s' % id for id in wl)
    wr = "".join('%s' % id for id in wr)
    result = wl + wr

    return result


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
