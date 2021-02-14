
def hack(config, edit, asm):
    asm(f"""
    .bank 0
    .org $aa3f
        LDA $67e            ; Item taken in the earthquake room?
        AND #8              ; 0=Yes, else no.
        BEQ setup_done      ; If yes, then start at north palace
                            ; otherwise, start at bagu's house.
        LDA #$03
        STA $0769           ; Bank
        LDA #$01
        STA $0707           ; World
        LDA #$03
        STA $056b           ; Town code
        LDA #$32
        STA $0748
        LDA #$1f            ; Room 31
        STA $0561           ; Room
        LDA #$01
        STA $075c           ; Page 1
        STA $0701           ; On RHS.
        LDA #$00
        STA $070a
        STA $0706           ; Region
        STA $056c           ; Palace code

        ; Door stack parameters:
        ; I don't understand what any of these values mean (except $075b).
        ; I just took the values from NES RAM after performing the door
        ; transition I wanted.
        ldx #5
        sta $69b3,x
        sta $69ac,x
        sta $69a5,x
        sta $05cc,x
        lda #1
        sta $075b           ; Door stack depth?
        sta $69ba,x
        sta $6990,x
        lda #3
        sta $6989,x
        sta $697b,x
        lda #6
        sta $699e,x
        lda #10
        sta $6982,x
        lda #11
        sta $6997,x
        lda #$60
        sta $05d3,x

        lda #8
        sta $079a           ; Have Bagu's note (cuz you ARE Bagu).

    setup_done:
        RTS
    """)
    return config
