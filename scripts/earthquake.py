from z2edit import Address
from z2edit.assembler import Asm

def hack(project, config):
    length = 35
    freespace = project.rom.alloc(Address.Prg(0, 0x8000), length)

    b7_length = 15
    b7_freespace = project.rom.alloc(Address.Prg(-1, 0x8000), b7_length)

    asm = Asm(project.rom)
    asm(f"""
    .bank 0
    .org {freespace}
    ; This memory location will be non-zero if we're on an earthquake screen.
    shake_effect = $06e1
    ; Player will be forced to take the item on bank/3/sideview/61/0 which
    ; will indicate we're in the post-earthquake world.
    earthquake = $067e

    shake:
        ldx $fd                     ; current fine-x scroll
        lda shake_effect            ; Earthquake?
        beq countdown               ; No: goto the sprite0 delay.
        lda $051b                   ; Random value
        and #7                      ; RNG value range 0..7.
        cpx #$80                    ; More than halfway on the fine-x scroll?
        bcc shake_position          ; No, we want an add for the shake effect.
        eor #$ff                    ; Yes, we want a subtract for the shaking.
    shake_position:
        adc $fd                     ; Add to current fine-x scroll.
        tax                         ; Into X register.
        and #3                      ; Random value range 0..3.
        bne countdown               ; 25% chance to make the earthquake sound.
        lda #$40                    ; Yes, make the sound.
        sta $ed

    countdown:
        ldy #$10                    ; Delay - 16 times through do-nothing loop.
    sprite0hit_delay:
        dey
        bne sprite0hit_delay
        rts
    .assert_org {freespace+length}

   .org $d4be
        ; Patch over the code which sets the scroll position
        jsr shake
        lda $ff                     ; Coarse-X value
        nop
        nop
        sta $2000                   ; Send scroll values to the PPU.
        stx $2005
        sty $2005

    .org {b7_freespace}
    check_earthquake:
        ldx $706
        bne done
        lda earthquake
        and #8
        beq done
        ldx #1
    done:
        rts
    .assert_org {b7_freespace + b7_length}

    .org $cdbe
        ; Patch over the code which checks which overworld to load.
        jsr check_earthquake
        
    """)
