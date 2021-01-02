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
