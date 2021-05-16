from z2edit import Text, Address

CREDITS = [
    ("BENTHIC KING   ",   "BY CF207 AND",  "BENTGLASSTUBE"),
    ("PROGRAMER   ",      "CF207        ", "             "),
    ("GRAPHICS ",         "BENTGLASSTUBE", ""),
    ("STORY   ",          "CF207        ", "BENTGLASSTUBE"),
    ("MUSIC",             "BENTGLASSTUBE", "             "),
    ("TOWER PALACE",      "CF207        ", ""),
    ("SEA PALACE  ",      "BENTGLASSTUBE", ""),
    ("SPECIAL THANKS",    "ZELDA II     ", "COMMUNITY"),
    ("THANKS A BILLION.", "PUSH START TO", "PLAY AGAIN"),
]

CREDITS_POINTERS = Address.prg(5, 0x9259)
CREDITS_DATA = Address.prg(5, 0x927D)
CREDITS_LEN = 305

PPU_ADDR = [0x2247, 0x228B, 0x22CB]

def hack(config, edit, asm):
    if len(CREDITS) != 9:
        raise Exception("Expecting exactly 9 credits items")

    # Assume we're operating on a vanilla ROM and just free the credits
    # data back to freespace.  We'll re-allocate at/near the same place,
    # but this will allow us to use more or less than the original.
    edit.free(CREDITS_DATA, CREDITS_LEN)

    for (i, item) in enumerate(CREDITS):
        val = bytearray()
        val.append(PPU_ADDR[0] >> 8)
        val.append(PPU_ADDR[0] & 255)
        text = Text.to_zelda2(item[0])
        val.append(len(text))
        val.extend(text)
        val.append(0xFF)
        dest = edit.alloc_near(CREDITS_DATA, len(val))
        edit.write_bytes(dest, bytes(val))
        edit.write_pointer(CREDITS_POINTERS + i*4, dest)

        val = bytearray()
        val.append(PPU_ADDR[1] >> 8)
        val.append(PPU_ADDR[1] & 255)
        text = Text.to_zelda2(item[1])
        val.append(len(text))
        val.extend(text)
        if item[2]:
            val.append(PPU_ADDR[2] >> 8)
            val.append(PPU_ADDR[2] & 255)
            text = Text.to_zelda2(item[2])
            val.append(len(text))
            val.extend(text)
        val.append(0xFF)
        dest = edit.alloc_near(CREDITS_DATA, len(val))
        edit.write_bytes(dest, bytes(val))
        edit.write_pointer(CREDITS_POINTERS + i*4 + 2, dest)

    return config
