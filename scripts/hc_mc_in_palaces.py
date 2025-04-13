import z2edit
from z2edit import Address
from z2edit.util import Tile, chr_clear, chr_copy, chr_swap

# Graphics arrangement (numbers in expressed in hex):
#
# Western Hyrule = bank 2/3
# Eastern Hyrule = bank 4/5
# P1 = bank 8/9
# P2 = bank a/b
# P3 = bank 12/13
# P4 = bank 14/15
# P5 = bank 16/17
# P6 = bank 18/19
# P7 = bank c/d
#

# The medicine is bank3, sprite $31 (chrs 30 and 31).
# In bank 5 (eastern hyrule), the Kid is in chrs 30 and 31.
# The magic container is in banks 3 and 5, sprite $83 (chrs 82 and 83).
# In the palace banks:
#    chrs $9c,$9d are a comma and an empty space.
#    chrs $b0,$b1 are a spike (never used).
#    chrs $82,$83 are part of link-holding-up-an-item.
# In the overworkd banks:
#    chrs $9c,$9d are a comma and a fragment of cave wall.
#
# Since the sprite IDs for the meds and MC are global, it wouild be best to
# make them the same in every bank.  As such, we will move sprites thusly:
#
# Link holding up an item will replace the unused spike, and the magic container
# will replace that part of link.
#
# The medicine will overwrite the comma placement, and for overworlds, the
# cave wall will be moved into the medicine place.
def hack(project, config):
    for t in range(0x88, 0xc4):
        chr_clear(project.rom, Tile(0x11, t), True)

    # Swap the med/kid with comma/cave wall in overworld CHR banks.
    for bank in (3, 5):
        chr_swap(project.rom, Tile(bank, 0x9c), Tile(bank, 0x30))
        chr_swap(project.rom, Tile(bank, 0x9d), Tile(bank, 0x31))

    # Fix the overworld PRG banks after the cave wall move.
    project.rom.write(Address.Prg(1, 0x8463), 0x31)
    project.rom.write(Address.Prg(1, 0x846b), 0x31)
    project.rom.write(Address.Prg(2, 0x8463), 0x31)
    project.rom.write(Address.Prg(2, 0x846b), 0x31)

    # Copy the meds to the comma/blank in the palace banks.
    # Move tile $88 to $8d and clear tile $8b ($89,$8b,$8d appear unused).
    # This opens up tiles $88/$89 as location for an 8x16 sprite.
    # Copy link into $88 and over the spike ($b0), and the hc and mc over link.
    for bank in (0x09, 0x0b, 0x0d, 0x13, 0x15, 0x17, 0x19):
        chr_clear(project.rom, Tile(bank, 0x8b))
        chr_copy(project.rom, Tile(bank, 0x9c), Tile(3, 0x9c))
        chr_copy(project.rom, Tile(bank, 0x9d), Tile(3, 0x9d))

        chr_copy(project.rom, Tile(bank, 0x8d), Tile(bank, 0x88))
        chr_copy(project.rom, Tile(bank, 0x88), Tile(bank, 0x80))
        chr_copy(project.rom, Tile(bank, 0x89), Tile(bank, 0x81))
        chr_copy(project.rom, Tile(bank, 0xb0), Tile(bank, 0x82))
        chr_copy(project.rom, Tile(bank, 0xb1), Tile(bank, 0x83))

        chr_copy(project.rom, Tile(bank, 0x80), Tile(3, 0x80))
        chr_copy(project.rom, Tile(bank, 0x81), Tile(3, 0x81))
        chr_copy(project.rom, Tile(bank, 0x82), Tile(3, 0x82))
        chr_copy(project.rom, Tile(bank, 0x83), Tile(3, 0x83))

    # Fix the palace crystal statue after tile moves
    project.rom.write(Address.Prg(4, 0x8391), 0x8d)
    project.rom.write(Address.Prg(4, 0x83a5), 0x8d)

    # Rewrite the sprite table for the meds/kid:
    project.rom.write_bytes(Address.Prg(-1, 0xeea9), bytes([0x9d, 0x9d]))
    project.rom.write_bytes(Address.Prg(-1, 0xeea5), bytes([0x9d, 0x9d]))
    # Rewrite the sprite table for link-holding-up-item:
    project.rom.write_bytes(Address.Prg(-1, 0xeb92), bytes([0x89, 0xb1]))
