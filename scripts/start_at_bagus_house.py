
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
    setup_done:
        RTS


    """)
    return config
