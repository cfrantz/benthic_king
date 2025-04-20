from z2edit import Address

GAME_OVER = bytes.fromhex("""
    21 6b 0a f4 ec e5 de de e9 e2 e7 e0 f4 21 c8 0f
    f0 e2 ed e1 f4 ed e1 de f4 df e2 ec e1 de ec 22
    4c 08 00 01 02 03 04 05 06 07 22 6c 08 10 11 12
    13 14 15 16 17 22 8c 08 20 21 22 23 24 25 26 27
    22 a9 0e 19 08 09 30 31 32 33 34 35 36 37 0a 0b
    1a 22 c8 83 18 28 0e 22 c9 0e 29 ff ff 38 ff ff
    1e 1f ff ff 39 ff ff 2a 22 d7 83 1b 2b 0f 22 e9
    4e ff 23 07 83 18 28 0e 23 09 4e ff 23 18 83 1b
    2b 0f 23 28 50 ff 23 46 83 18 28 0e 23 48 50 ff
    23 59 83 1b 2b 0f 23 67 52 ff 23 85 82 18 28 23
    87 52 ff 23 9a 82 1b 2b 23 a6 54 ff 23 69 83 0c
    1c 2c 23 76 83 0d 1d 2d 23 e3 42 50 23 ea 44 55
    23 f1 46 55 23 f9 46 05 ff 3f 00 08 16 30 0f 0f
    16 30 27 0f ff
""")

def hack(project, config):
    project.rom.write_bytes(Address.Prg(0, 0x8000), GAME_OVER)
