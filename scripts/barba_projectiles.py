from z2edit import PyAddress
# Make Barba shoot projectiles up or down.
def hack(config, edit, asm):
    length = 21
    freespace = edit.alloc_near(PyAddress.prg(4, 0x8000), length)
    freespace = freespace.addr()
    asm(f"""
        .bank 4
        .org {freespace}
        barba_projectile_direction:
            lda $29                 ; Link's y position
            cmp $2f                 ; Barba's y position
            bcs direction_done      ; If >= barba's Ypos, nothing to do
            lda $584,x              ; Flip bits
            eor #$ff
            sta $584,x
        direction_done:
            dec $30,x
            dec $30,x
            dec $30,x
            rts
        .assert_org {freespace+length}

        .org $b1ab
            jsr barba_projectile_direction
            nop
            nop
            nop
    """)
    return config
