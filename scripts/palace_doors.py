######################################################################
# Add the town-door mechanic to palaces.
######################################################################
import logging
from z2edit import Address, Alloc
from z2edit.util import ObjectDict, Tile, chr_copy
from z2edit.assembler import Asm

logger = logging.getLogger(__name__)

def hack(project, config):
    # Copy the town top doorframe to all Palace CHR banks.
    for bank in (0x09, 0x0b, 0x0d, 0x13, 0x15, 0x17, 0x19):
        chr_copy(project.rom, Tile(bank, 0xa4), Tile(0x07, 0x49))
        chr_copy(project.rom, Tile(bank, 0xa7), Tile(0x07, 0x4a))

    metatile = config.get("/bank/4/metatile/background")
    ptr = Address(metatile.address)
    group = project.rom.read_pointer(ptr)
    length = metatile.length[0] * 4
    data = bytearray(project.rom.read_bytes(group, length))
    project.rom.free(group, length)

    # Metatiles 0x41 and 0x4f will be the door frame and door base.
    data[4:8] = [0xa4, 0xf5, 0xa7, 0xf5]
    data.extend([0x64, 0x65, 0x65, 0x64])
    # Write the metatile table back to the ROM and update the pointers.
    group = project.rom.alloc(group, len(data), Alloc.Near)
    project.rom.write_pointer(ptr, group)
    project.rom.write_pointer(ptr+2, group)
    project.rom.write_bytes(group, bytes(data))
    # Inform the config about the new length.
    metatile.length[0] = len(data) / 4
    metatile.length[1] = len(data) / 4

    # Hack the game to support doorways in palaces
    bank4_length = 23
    bank4_freespace = project.rom.alloc(Address.Prg(4, 0x9ee0), bank4_length, Alloc.Near)
    logger.info("bank4_freespace %r", bank4_freespace)

    bank7_length = 15
    bank7_freespace = project.rom.alloc(Address.Prg(-1, 0xfeaa), bank7_length, Alloc.Near)
    logger.info("bank7_freespace %r", bank7_freespace)

    asm = Asm(project.rom)
    asm(f"""
        .bank 4
        bank7_set_ram_address_for_object = $c944
        bank7_place_object_vertical = $df56
        bank7_Mute_music_when_loading_between_areas = $d03d

        ;; Set the magic door tile in the magic tiles table.
        .org $851a
        .db $4f

        .org {bank4_freespace}
        ;; Door tiles in bottom to top order.
        door_construction_table:
        .db $4f,$40,$40,$41

        ;; Routine to construct the door object.
        palace_door_construction_routine:
            ldx #3                                  ; Door is 4 tiles tall.
            stx $0
            jsr bank7_set_ram_address_for_object    ; Location where we'll put it.
        loop:
            lda door_construction_table,x           ; Get the object id
            jsr bank7_place_object_vertical         ; Place it
            dex
            dec $0
            bpl loop                                ; Repeat
            rts
        .assert_org {bank4_freespace+bank4_length}

        ;; Take over "small object 6" which is currently a duplicate of the
        ;; conventional palace locked door.  Patch in our door routine.
        .org $813f
        .dw palace_door_construction_routine

        .org $d031
        ;; The vanilla door exit routine would always change the music unless you were
        ;; in old kasuto.  Change it to always change the music in towns, but not
        ;; in palaces.
        door_exit_done = $d041
        door_exit_music:
            lda $0707                               ; Current world
            cmp #3                                  ; worlds >= 3 are palaces
            bcs door_exit_done                      ; branch greater-or-equal

        ;; In freespace, after the softlock fix:
        .org {bank7_freespace}
        maybe_mute_music_between_areas:
            lda $0707                               ; current world
            cmp #3                                  ; worlds >= 3 are palaces
            bcs dont_mute_music
            jmp bank7_Mute_music_when_loading_between_areas ; mute music and return
        dont_mute_music:
            pla                                     ; pop the return address
            pla                                     ; cuz we aren't going back there
            jmp $cfec                               ; goto eval room entry conditions
        .assert_org {bank7_freespace+bank7_length}

        ;; Patch it into the room exit routine
        .org $cfe5
            jsr maybe_mute_music_between_areas
    """)

    for group in config.get('/bank/4/sideview/group').values():
        logger.info("Updating", group)
        group.max_door_index = 28

    render = config.get('/bank/4/sideview/group/0/render_info')
    door = config.get(f'{render}/small/6')
    door.name = 'Door'
    door.render = 'Grid'
    door.width = 1
    door.height = 4
    door.metatile = [0x41, 0x40, 0x40, 0x4f]

