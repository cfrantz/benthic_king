from z2edit import Address
from z2edit.assembler import Asm
from z2edit.util import Tile

def hack(project, config):
    # Change the mid-line dot character into an apostrophe.
    # Use the comma from position 0x9c to create the apostrophe.
    comma = project.rom.read_bytes(Tile(7, 0x9c), 16)
    apostrophe = comma[5:8] + comma[0:5] + comma[13:16] + comma[8:13]
    project.rom.write_bytes(Tile(7, 0x32), apostrophe)

    # Currently, it looks like the text output routine for town dialog
    # is setup to write vertically with some optional accent thing going
    # on above the letters (something for japanese text?).
    #
    # Change it to write horizontally, blanking out the rest of the line
    # so longer (multi-pane) dialogs are easier to read.
    asm = Asm(project.rom)
    asm(f"""
    .bank 3
    .org $b6dd
        sta      $0305      ; Letter Written to Screen

        ;; This bit of original ROM code calculates the position to write
        ;; the next char and places it into the address field of the macro.
        lda      $0489      ; Letter X Position offset
        asl
        asl
        asl
        sta      $02
        lda      $072C      ; Scrolling Offset Low Byte
        clc
        adc      #$88       ; Base X position of text lines
        and      #$F0       ; keep bits xxxx .... (round to align to tile)
        php
        clc
        adc      $02
        sta      $02
        lda      $072A      ; Scrolling Offset High Byte
        adc      #$00
        plp
        adc      #$00
        and      #$01       ; keep bits .... ...x
        asl
        asl
        adc      #$21       ; $2000 or $2400 
        sta      $03
        lda      $02
        lsr
        lsr
        lsr
        adc      #$00       ; Was #$E0; changed to zero because of #$21 above
        adc      $048A      ; Letter Y Position offset
        sta      $0303      ; Letter position when writing to screen
        lda      $03
        adc      #$00
        sta      $0302

        ;; Hack the PPU macro to clear the whole line so multiple panes of
        ;; dialog are easier to read.
        ldy     #4              ; Total macro length
        ldx     #$ff            ; End of macro symbol
        sec
        lda     #9              ; 10 chars, but 1 less cuz we already have the letter
        sbc     $489            ; minus current X position
        bmi     noblank         ; negative, no blanking needed.
        tax                     ; loop counter
        lda     #$f4            ; Blank character
    blankloop:
        sta     $306,x          ; Fill in the macro past the letter.
        iny
        dex
        bpl     blankloop       ; Till we're done.
        
    noblank:
        txa                     ; end-of-macro symbol into A
        sta     $0302,y         ; save it.
        sty     $0301           ; Total length
        dey
        dey
        dey
        sty     $0304           ; Data length of this particular macro.

        nop                     ; With 9 bytes to spare!
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

    .assert_org $b746           ; Make sure we end where we expected to.


    ;; This version just put a single blank in front of the cursor position,
    ;; but would chew up the right-hand side of the dialog box.
    ;; Simpler dialog hack
    ;;    .org $b6f6
    ;;        sta $0305
    ;;    .org $b734
    ;;        lda #2
    ;;        sta $0304
    ;;        stx $0306

    """)

    return config
