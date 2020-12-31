######################################################################
# Expanded tileset experiment for Zedla2.
# Give overworld up to 64 unique tiles.
######################################################################
import z2edit
from z2edit import PyAddress
from z2edit.util import ObjectDict, Tile, chr_clear

chr_clear(edit, Tile(0x11, 0x88), True)
chr_clear(edit, Tile(0x11, 0x89), True)
chr_clear(edit, Tile(0x11, 0x8a), True)
chr_clear(edit, Tile(0x11, 0x8b), True)
chr_clear(edit, Tile(0x11, 0x8c), True)
chr_clear(edit, Tile(0x11, 0x8d), True)
chr_clear(edit, Tile(0x11, 0x8e), True)
chr_clear(edit, Tile(0x11, 0x8f), True)
chr_clear(edit, Tile(0x11, 0x90), True)
chr_clear(edit, Tile(0x11, 0x91), True)
chr_clear(edit, Tile(0x11, 0x92), True)
chr_clear(edit, Tile(0x11, 0x93), True)
chr_clear(edit, Tile(0x11, 0x94), True)
chr_clear(edit, Tile(0x11, 0x95), True)
chr_clear(edit, Tile(0x11, 0x96), True)
chr_clear(edit, Tile(0x11, 0x97), True)
chr_clear(edit, Tile(0x11, 0x98), True)
chr_clear(edit, Tile(0x11, 0x99), True)
chr_clear(edit, Tile(0x11, 0x9a), True)
chr_clear(edit, Tile(0x11, 0x9b), True)
chr_clear(edit, Tile(0x11, 0x9c), True)
chr_clear(edit, Tile(0x11, 0x9d), True)
chr_clear(edit, Tile(0x11, 0x9e), True)
chr_clear(edit, Tile(0x11, 0x9f), True)
chr_clear(edit, Tile(0x11, 0xa0), True)
chr_clear(edit, Tile(0x11, 0xa1), True)
chr_clear(edit, Tile(0x11, 0xa2), True)
chr_clear(edit, Tile(0x11, 0xa3), True)
chr_clear(edit, Tile(0x11, 0xa4), True)
chr_clear(edit, Tile(0x11, 0xa5), True)
chr_clear(edit, Tile(0x11, 0xa6), True)
chr_clear(edit, Tile(0x11, 0xa7), True)
chr_clear(edit, Tile(0x11, 0xa8), True)
chr_clear(edit, Tile(0x11, 0xa9), True)
chr_clear(edit, Tile(0x11, 0xaa), True)
chr_clear(edit, Tile(0x11, 0xab), True)
chr_clear(edit, Tile(0x11, 0xac), True)
chr_clear(edit, Tile(0x11, 0xad), True)
chr_clear(edit, Tile(0x11, 0xae), True)
chr_clear(edit, Tile(0x11, 0xaf), True)
chr_clear(edit, Tile(0x11, 0xb0), True)
chr_clear(edit, Tile(0x11, 0xb1), True)
chr_clear(edit, Tile(0x11, 0xb2), True)
chr_clear(edit, Tile(0x11, 0xb3), True)
chr_clear(edit, Tile(0x11, 0xb4), True)
chr_clear(edit, Tile(0x11, 0xb5), True)
chr_clear(edit, Tile(0x11, 0xb6), True)
chr_clear(edit, Tile(0x11, 0xb7), True)
chr_clear(edit, Tile(0x11, 0xb8), True)
chr_clear(edit, Tile(0x11, 0xb9), True)
chr_clear(edit, Tile(0x11, 0xba), True)
chr_clear(edit, Tile(0x11, 0xbb), True)
chr_clear(edit, Tile(0x11, 0xbc), True)
chr_clear(edit, Tile(0x11, 0xbd), True)
chr_clear(edit, Tile(0x11, 0xbe), True)
chr_clear(edit, Tile(0x11, 0xbf), True)
chr_clear(edit, Tile(0x11, 0xc0), True)
chr_clear(edit, Tile(0x11, 0xc1), True)
chr_clear(edit, Tile(0x11, 0xc2), True)
chr_clear(edit, Tile(0x11, 0xc3), True)

######################################################################
# Create a new tile mapping table, followed by a palette mapping table.
######################################################################
length = 0x16c
freespace = edit.alloc_near(PyAddress.prg(0, 0xb000), length)
overworld_tile_mappings = freespace
overworld_palette_codes = freespace + 0x100
freespace = freespace.addr()

asm(f"""
    .bank 0
    .org {freespace}
    overworld_tile_mappings:
    .db $5C,$5D,$5E,$5F     ; Town
    .db $F4,$F4,$F4,$F4     ; Grotto
    .db $60,$61,$62,$63     ; Palace
    .db $5A,$5A,$5B,$5B     ; Bridge
    .db $6C,$6C,$6C,$6C     ; Desert
    .db $6D,$6D,$6D,$6D     ; Grass
    .db $68,$69,$6A,$6B     ; Forest
    .db $6F,$6F,$6F,$6F     ; Swamp
    .db $70,$71,$FE,$FE     ; Graveyard
    .db $FE,$FE,$FE,$FE     ; Road
    .db $6E,$6E,$6E,$6E     ; Lava
    .db $64,$65,$66,$67     ; Mountain
    .db $6E,$6E,$6E,$6E     ; Water
    .db $6E,$6E,$6E,$6E     ; Water (walkable)
    .db $56,$57,$58,$59     ; Rock
    .db $40,$41,$42,$43     ; Spider

    .db $d1,$f5,$d0,$f5     ; Tile $10
    .db $d1,$f5,$d1,$f5     ; Tile $11
    .db $d1,$f5,$d2,$f5     ; Tile $12
    .db $d1,$f5,$d3,$f5     ; Tile $13
    .db $d1,$f5,$d4,$f5     ; Tile $14
    .db $d1,$f5,$d5,$f5     ; Tile $15
    .db $d1,$f5,$d6,$f5     ; Tile $16
    .db $d1,$f5,$d7,$f5     ; Tile $17
    .db $d1,$f5,$d8,$f5     ; Tile $18
    .db $d1,$f5,$d9,$f5     ; Tile $19
    .db $d1,$f5,$da,$f5     ; Tile $1a
    .db $d1,$f5,$db,$f5     ; Tile $1b
    .db $d1,$f5,$dc,$f5     ; Tile $1c
    .db $d1,$f5,$dd,$f5     ; Tile $1d
    .db $d1,$f5,$de,$f5     ; Tile $1e
    .db $d1,$f5,$df,$f5     ; Tile $1f

    .db $d2,$f5,$d0,$f5     ; Tile $20
    .db $d2,$f5,$d1,$f5     ; Tile $21
    .db $d2,$f5,$d2,$f5     ; Tile $22
    .db $d2,$f5,$d3,$f5     ; Tile $23
    .db $d2,$f5,$d4,$f5     ; Tile $24
    .db $d2,$f5,$d5,$f5     ; Tile $25
    .db $d2,$f5,$d6,$f5     ; Tile $26
    .db $d2,$f5,$d7,$f5     ; Tile $27
    .db $d2,$f5,$d8,$f5     ; Tile $28
    .db $d2,$f5,$d9,$f5     ; Tile $29
    .db $d2,$f5,$da,$f5     ; Tile $2a
    .db $d2,$f5,$db,$f5     ; Tile $2b
    .db $d2,$f5,$dc,$f5     ; Tile $2c
    .db $d2,$f5,$dd,$f5     ; Tile $2d
    .db $d2,$f5,$de,$f5     ; Tile $2e
    .db $d2,$f5,$df,$f5     ; Tile $2f

    .db $d3,$f5,$d0,$f5     ; Tile $30
    .db $d3,$f5,$d1,$f5     ; Tile $31
    .db $d3,$f5,$d2,$f5     ; Tile $32
    .db $d3,$f5,$d3,$f5     ; Tile $33
    .db $d3,$f5,$d4,$f5     ; Tile $34
    .db $d3,$f5,$d5,$f5     ; Tile $35
    .db $d3,$f5,$d6,$f5     ; Tile $36
    .db $d3,$f5,$d7,$f5     ; Tile $37
    .db $d3,$f5,$d8,$f5     ; Tile $38
    .db $d3,$f5,$d9,$f5     ; Tile $39
    .db $d3,$f5,$da,$f5     ; Tile $3a
    .db $d3,$f5,$db,$f5     ; Tile $3b
    .db $d3,$f5,$dc,$f5     ; Tile $3c
    .db $d3,$f5,$dd,$f5     ; Tile $3d
    .db $d3,$f5,$de,$f5     ; Tile $3e
    .db $d3,$f5,$df,$f5     ; Tile $3f

    overworld_palette_codes:
    .db 2,1,2,1,3,0,0,0,1,1,1,1,3,3,1,1 ; Tiles $00-$0F
    .db 2,1,2,1,3,0,0,0,1,1,1,1,3,3,1,1 ; Tiles $10-$1F
    .db 2,1,2,1,3,0,0,0,1,1,1,1,3,3,1,1 ; Tiles $20-$2F
    .db 2,1,2,1,3,0,0,0,1,1,1,1,3,3,1,1 ; Tiles $30-$3F

    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; Create a decompressor which understands the expanded tileset.
    ; Tile IDs $0 to $E behave normally.
    ; Tile ID $F is only useful as length==1, so reuse all other length
    ; encodings for tile $F to mean "that many of the following expansion
    ; tile ID".
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    overworld_decompress:
        lda ($0e),y             ; Get compressed tile
        and #$0f                ; Tile id
        cmp #$0f
        bcc regular_rle         ; Tile id < $0f means regular mode
        lda ($0e),y             ; Get compressed tile
        cmp #$1f
        bcc regular_rle         ; (count,tile) < $1f means regular mode
        pha                     ; Save it to extract the count later
        iny
        lda ($0e),y             ; Expansion tile
        sta $02
        pla                     ; Get the count byte
        lsr                     ; shift the count down 4 bits
        lsr
        lsr
        lsr
        clc                     ; count + 0
        bcc save_count          ; we just cleared carry, branch always to save.
    regular_rle:
        and #$0f                ; Get tile type
        sta $02                 ; store it
        lda ($0e),y             ; Get compressed tile
        lsr                     ; shift the count down 4 bits
        lsr
        lsr
        lsr
        sec                     ; count + 1
    save_count:
        adc $03
        sta $03
        rts
    .assert_org {freespace+length}

    ; Patch in decompressor
    .org $892d
        jsr overworld_decompress
    .org $8c30
        jsr overworld_decompress

    ; Patch in new tables: tile mappings
    .org $8980
        lda overworld_tile_mappings,x 
    .org $8c97
        lda overworld_tile_mappings,x 

    ; Patch in new tables: palette mappings
    .org $8aa8
        lda overworld_palette_codes,x
    .org $8ab1
        lda overworld_palette_codes,x
    .org $8aba
        lda overworld_palette_codes,x
    .org $8ac3
        lda overworld_palette_codes,x

    .org $8bb3
        lda overworld_palette_codes,x
    .org $8bbc
        lda overworld_palette_codes,x
    .org $8bc6
        lda overworld_palette_codes,x
    .org $8bcf
        lda overworld_palette_codes,x
""")

######################################################################
# banks 1 and 2 have identical copies of the decompressor used to determine
# map boundaries and terrain types.
# Patch in a version of ours for that purpose.
######################################################################
length = 0x36
for bank in (1, 2):
    freespace = edit.alloc_near(PyAddress.prg(bank, 0xac00), length)
    freespace = freespace.addr()
    asm(f"""
        .bank {bank}
        .org {freespace}
        bank1_ov_decompress:
            lda ($0e),y             ; Get compressed tile
            and #$0f                ; Tile id
            cmp #$0f
            bcc regular_rle         ; Tile id < $0f means regular mode
            lda ($0e),y             ; Get compressed tile
            cmp #$1f
            bcc regular_rle         ; (count,tile) < $1f means regular mode
            pha                     ; Save it to extract the count later
            iny
            lda ($0e),y             ; Expansion tile
            and #$0f                ; Mask off the expansion bits to alias to terrain type
            sta $02
            pla                     ; Get the count byte
            lsr                     ; shift the count down 4 bits
            lsr
            lsr
            lsr
            clc                     ; count + 0
            bcc save_count          ; we just cleared carry, branch always to save.
        regular_rle:
            and #$0f                ; Get tile type
            sta $02                 ; store it
            lda ($0e),y             ; Get compressed tile
            lsr                     ; shift the count down 4 bits
            lsr
            lsr
            lsr
            sec                     ; count + 1
        save_count:
            adc $03
            sta $03
            cmp $00
            bcs done
            iny
            jmp bank1_ov_decompress
        done:
            rts
        .assert_org {freespace+length}

        .org $83eb
            jmp bank1_ov_decompress
    """)


######################################################################
# Update the config to say that we've expanded the tileset
######################################################################

meta = edit.meta
config = ObjectDict.from_json(z2edit.config[meta['config']])
for m in config.overworld.map:
    m.objtable = ObjectDict.from_address(overworld_tile_mappings)
    m.objtable_len = 64
    m.tile_palette = ObjectDict.from_address(overworld_palette_codes)
config.overworld.tileset = 'CF207Hackjam2020'

name = meta['config'] + '-tile_expansion'
meta['extra'] = {'next_config': name}
z2edit.config[name] = config.to_json()
edit.meta = meta

