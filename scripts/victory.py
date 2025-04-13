from z2edit.assembler import Asm

# Trigger the victory condition for Benthic King
# When Link collects the Kid (aka Trident), the game is over.
#
# Since we are applying a custom assembly hack to the code for handling
# the Child, we delete it from the item effects so that when the editor
# re-packs the ROM, it won't overwrite our custom code.
def hack(project, config):
    item = config.get("/global/item")
    item.effects.effect.pop("Child")

    asm = Asm(project.rom)
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
