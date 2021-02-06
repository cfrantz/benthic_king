from z2edit import Text, PyAddress


TITLE_LINE = [
    0xa932, 0xa94f, 0xa96c, 0xa989,
    0xa9a6, 0xa9c3, 0xa9e0, 0xa9fd,
    0xaa1a, 0xaa37, 0xaa54, 0xaa71,
    0xaa8e, 0xaaab, 0xaac8,
]

TITLE_TEXT = [
# The title text strings have strict formatting requirements.  
# They must be exactly 27 characters long (in reality, they're 28 characters
# long, but the last character must be the Nintendo "newline" character).
#   "0         1         2       "
#   "0123456789012345678901234567"
    "HYRULE HAS ENJOYED YEARS    ",
    "OF UNCHARACTERISTIC PEACE.  ",
    "                            ",
    "BAGU SPENDS ALL HIS DAYS    ",
    "ENDLESSLY FISHING, BUT NOW  ",
    "HE HAS ANGERED THE KING OF  ",
    "THE MERFOLK.  THE OCEANS    ",
    "ARE RISING QUICKLY.  LINK   ",
    "MUST JOURNEY INTO THE       ",
    "BRINY DEPTHS AND DEFEAT     ",
    "THE FISH KING IN HIS MOST   ",
    "ADVENTURESOME QUEST YET...  ",
    "       .1987 NINTENDO       ",
    "                            ",
    "                            ",
]

def hack(config, edit, asm):
    for (addr, line) in zip(TITLE_LINE, TITLE_TEXT):
        print('Title Text:', repr(line))
        line = Text.to_zelda2(line)
        edit.write_bytes(PyAddress.prg(5, addr), line)
    # Insert the copyright character
    edit.write(PyAddress.prg(5, 0xaa95), 0xe)
    return config



# Rewrite macros to create a big block of graphics to mess with
#
#          10 11 12 13 14 15 16 17
# 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d
# 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d
# 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d
# 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d
# a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad
# b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd

def hack_graphics(config, edit, asm):
    edit.write_bytes(PyAddress.prg(5, 0xaf69), bytes.fromhex("22 6b 09 f4 10 11 12 13 14 15 16 17"))
    edit.write_bytes(PyAddress.prg(5, 0xaf75), bytes.fromhex("22 7f 01 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xaf79), bytes.fromhex("23 e0 08 00 00 00 00 00 00 00 cc"))
    edit.write_bytes(PyAddress.prg(5, 0xaf84), bytes.fromhex("22 88 18 f4 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d f4 f4 f4 f4 f4 f4 f4 f4 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xaf9f), bytes.fromhex("23 e8 08 00 00 00 00 00 00 00 cc"))
    edit.write_bytes(PyAddress.prg(5, 0xafaa), bytes.fromhex("22 a8 18 f4 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d f4 f4 f4 f4 f4 f4 f4 f4 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xafc5), bytes.fromhex("22 c9 0e 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d"))
    edit.write_bytes(PyAddress.prg(5, 0xafd6), bytes.fromhex("22 df 01 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xafda), bytes.fromhex("22 e9 0e 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d"))
    edit.write_bytes(PyAddress.prg(5, 0xafeb), bytes.fromhex("22 ff 01 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xafef), bytes.fromhex("23 09 17 a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad f4 f4 f4 f4 f4 f4 f4 f4 fd"))
    edit.write_bytes(PyAddress.prg(5, 0xb009), bytes.fromhex("23 f0 08 00 00 00 00 00 00 00 cc"))
    edit.write_bytes(PyAddress.prg(5, 0xb014), bytes.fromhex("23 29 17 b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd f4 f4 f4 f4 f4 f4 f4 f4 fd"))

    # Table of start addresses per line.
    for (i, ptr) in enumerate([0xaf69, 0xaf84, 0xafaa, 0xafc5, 0xafda, 0xafef, 0xb014]):
        edit.write_word(PyAddress.prg(5, 0xab5f + i*2), ptr)

    return config
