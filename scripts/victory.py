# Trigger the victory condition for Benthic King
# When Link collects the Kid (aka Trident), the game is over.
def hack(config, edit, asm):
    asm(f"""
        .bank 0
        .org $e821
        go_on_get_the_kid:
            lda #3
            sta $76c
            nop
            nop
            nop
    """)
    return config
