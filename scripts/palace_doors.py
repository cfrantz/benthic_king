######################################################################
# Add the town-door mechanic to palaces.
######################################################################
import z2edit
from z2edit import PyAddress
from z2edit.util import ObjectDict, Tile, chr_copy

def hack(config, edit, asm):
    # Copy the town top doorframe to all Palace CHR banks.
    for bank in (0x09, 0x0b, 0x0d, 0x13, 0x15, 0x17, 0x19):
        chr_copy(edit, Tile(bank, 0xa4), Tile(0x07, 0x49))
        chr_copy(edit, Tile(bank, 0xa7), Tile(0x07, 0x4a))

    # Hack the game to support doorways in palaces
    bank4_length = 23
    bank4_freespace = edit.alloc_near(PyAddress.prg(4, 0x9ee0), bank4_length)
    print("bank4_freespace", bank4_freespace)
    bank4_freespace = bank4_freespace.addr()

    bank7_length = 15
    bank7_freespace = edit.alloc_near(PyAddress.prg(7, 0xfeaa), bank7_length)
    print("bank7_freespace", bank7_freespace)
    bank7_freespace = bank7_freespace.addr()

    asm(f"""
        .bank 4
        bank7_set_ram_address_for_object = $c944
        bank7_place_object_vertical = $df56
        bank7_Mute_music_when_loading_between_areas = $d03d

        ;; Set CHR tile codes for door components.
        ;; This creates background objects $41 and $51.
        ;; Object $41 is the top door frame.
        ;; Object $51 looks just like palace bricks, but is a distinct object
        ;;            so the door routine can detect when Link stands on it.
        .org $8341
        .db $a4,$f5,$a7,$f5
        .org $8381
        .db $64,$65,$65,$64

        .org {bank4_freespace}
        ;; Door tiles in bottom to top order.
        door_construction_table:
        .db $51,$40,$40,$41

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

        ;; Set the magic door tile in the magic tiles table.
        .org $851a
        .db $51

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

    # Update the config so the editor understands doors in palaces.
    for group in config.sideview.group:
        if group.id in ('palace_125', 'palace_346'):
            group.max_door_index = 28
            group.door_objects = [('Small', 6)]

    # Update the config to replace palace small object 6 with our door object.
    for obj in config.objects:
        if obj.id == 6 and obj.area == 'Palace':
            obj.name = 'Door'
            obj.render = 'Grid'
            obj.width = 1
            obj.height = 4
            obj.metatile = [0x41, 0x40, 0x40, 0x51]

    return config
