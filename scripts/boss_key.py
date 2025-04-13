from z2edit import Address, Alloc
from z2edit.assembler import Asm

def hack(project, config):
    length = 31
    freespace = project.rom.alloc(Address.Prg(-1, 0x8000), length, Alloc.Near)
    asm = Asm(project.rom)
    asm(f"""
        ;; Burn some precious bank7 freespace for boss-to-item transforms.
        .bank 7
        .org {freespace}
        boss_transform_length = 3   ; number of table entries minus 1
        boss_rooms:
        .db 24, 34, 14, 58          ; horse, helmet, rebo, barba
        boss_items:
        .db  1,  3,  8,$13          ; glove, boots, key, kid (trident)

        boss_transform:
            ldy #boss_transform_length      ; length of table
        loop:
            lda boss_rooms,y                ; who's room are we in?
            cmp $0561
            beq transform                   ; if that room, get the transformed item
            dey
            bpl loop                        ; keep searching
            lda #8                          ; otherwise keyj
        done:
            sta $af,x                       ; next item
            rts
        transform:
            lda boss_items,y                ; get the transformed item.
            bne done
        .assert_org {freespace+length}

        .org $de18
            jmp boss_transform

        ; Hack item get routine

        .org $e784
            ; at $e784
            ; if (item_code > 8) goto $e79a, but we moved it up to $e797
            bcs got_it

        .org $e797
            ; we destroy the jump here so we just fall through
            ; into the key get routine
        got_it:
            cpy     #8          ; is it a key
            bne     not_a_key
            inc     $0793       ; incr keys
            sty     $ef         ; key sound
        not_a_key:
            lda      $0728      ; scroll locked?
            beq      item_done  ; nope, all done
            lda      #$00       ; unlock
            sta      $0728
            lda      $07FB      ; ???
            bne      item_done
            lda      #$02       ; restart theme
            sta      $EB
        item_done:
            cpy     #9          ; more code to handle this item?
            bcs     high_items  ; yep, go do it
            jmp     $dd47       ; bank7_remove_enemy_or_item
            nop
        high_items:

        """)
