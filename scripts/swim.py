from z2edit import PyAddress

def hack(config, edit, asm):
    length = 703
    freespace = edit.alloc(PyAddress.prg(0, 0x8000), length)
    freespace = freespace.addr()

    bank7_length = 9
    bank7_freespace = edit.alloc_near(PyAddress.prg(7, 0xff4c), bank7_length)
    bank7_freespace = bank7_freespace.addr()

    asm(f"""
        .bank 0

        ;; Some useful addressses in bank7
        get_regionx5_plus_world = $cf30
        load_bank0 = $ffc5
        load_bank_at_769 = $ffc9
        bank7_xy_movement_routine = $d1ce
        bank7_xy_computation = $d1e4
        BITMASKS = $f26c

        ;; Unused RAM at $06e0
        swim_enabled = $06e0    ; is swim enabled on this screen?
        effects = $06e0         ; other effects
        tmpy = $06e8            ; Temp storage for Y register

        ;; Freespace in bank7 to hold our thunk to swimcheck.
        .org {bank7_freespace}
        dynamic_banks_entry:
            sta $0561
            jsr load_bank0
            jmp swimcheck
        .assert_org {bank7_freespace+bank7_length}

        .org $c65d              ; In the elevator exit routine
            jsr dynamic_banks_entry
        .org $cc9d              ; In "get area code enter code and direction"
            jsr dynamic_banks_entry
        .org $cfb4              ; room-to-room transition (I think).
            jsr dynamic_banks_entry
        .org $d00e              ; doorways
            jsr dynamic_banks_entry

        ;; Table for each region.  Each segment of the table is 16 bytes long,
        ;; and contains (room numbers,chr bank) pairs.
        .org {freespace}
        room:
        bank = {freespace+1}
        ; This first entry should really be in the "west towns" world, but
        ; dynamic banks runs before the world-to-world transition, so we put it
        ; in the 'west caves' category.
        .db $3d,$81,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West caves
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West towns
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $15,$0a,$3d,$0a,$38,$0a,$36,$0a,$18,$0a,$22,$0a,$02,$08,$08,$08 ; West P125
        .db $09,$08,$07,$08,$0b,$08,$0d,$08,$10,$08,$00,$00,$00,$00,$00,$00 ; West P346
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ caves (or west GP)
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ P125
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ P346
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East caves
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East towns
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East P125
        .db $3e,$12,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East P346
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East GP


        ;; Table for each region.  Each segment of the table is 16 bytes long,
        ;; and contains room numbers in which swim is enabled, with a zero terminator.
        swimrooms:
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West caves
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West towns
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West P125
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; West P346
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ caves (or West GP)
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ P125
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; DM/MZ P346
        .db $1d,$22,$27,$2f,$13,$14,$2d,$08,$33,$39,$26,$09,$0a,$00,$00,$00 ; East Caves (or DM/MZ GP)
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; Not used
        .db $2e,$3a,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East Towns
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East P125
        .db $3a,$36,$3b,$3c,$3d,$3e,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East P346
        .db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00 ; East GP

        ;; Original jump gravity table is at $9470.
        ;; We have our own alternate "swim gravity" table.
        jump_gravity = $9470
        swim_gravity:
        .db $ff,$ff,$ff,$ff

        ;; Swimcheck is just like dynamic banks:  Scan the table for the
        ;; room we're in.  Dynamic banks loads a CHR bank, swimcheck just sets a flag.
        swimcheck:
            jsr get_regionx5_plus_world     ; Get region*5+world
            asl                             ; 16 bytes per region/world combo
            asl
            asl
            asl
            pha                             ; Save R5+W for later
            tax
        swimcheckloop:
            lda swimrooms,x                 ; scan through table
            beq swimcheckdone
            cmp $0561                       ; equal to current room
            beq swimcheckdone
            inx
            bne swimcheckloop
        swimcheckdone:
            sta swim_enabled                ; store the swim state

            lda #0
            ldx #6                          ; zero out $6e6 down to $6e1
        zero_effects_bytes:
            sta effects,x
            dex
            bne zero_effects_bytes

        ;; Second part: dynamic banks, sfx and automation
            pla                             ; Get R5+W
            tax
        loop:
            lda ROOM,x                      ; table of rooms
            beq done                        ; zero value means end
            cmp $0561                       ; equal to room number?
            beq loadchr                     ; yes, get and load chr bank
            inx                             ; nope, inc pointer
            inx
            bne loop                        ; check next value
        loadchr:
            lda BANK,x                      ; Which CHR bank or effect?
            bmi soundeffect                 ; Effect
            sta $076e                       ; Save CHR bank.
        done:
            jmp load_bank_at_769            ; load bank $769 and return
        soundeffect:
            pha
            lsr                             ; Get SFX offset into X
            lsr
            lsr
            lsr
            tax
            pla                             ; Low nybble is sound effect
            and #$0f
            cpx #$08                        ; Values $81 to $8F for misc effects
            beq automation
            sty tmpy
            tay
            lda BITMASKS,y
            sta $e0,x
            ldy tmpy
            jmp load_bank_at_769            ; load bank $769 and return
        automation:
            tax
            sta effects,x                   ; Set effect byte
            jmp load_bank_at_769            ; load bank $769 and return
            
            
        ;; Mess with jump routine so A means "go up"
        swim1:
            lda swim_enabled                ; Is swimming enabled
            beq not_swimming1
            lda swim_gravity,y              ; Yes - Load the swim gravity.
            rts
        not_swimming1:
            lda jump_gravity,y              ; No - Load the regular gravity.
            rts

        swim2:
            lda swim_enabled                ; Is swimming enabled
            beq not_swimming2
            lda $057d                       ; Link's Y velocity
            bmi swim_no_gravity             ; Heading up? do nothing.
            lda swim_gravity                ; Heading down, rewrite downward accel as -1
            sta $057d
        swim_no_gravity:
            ldy #0
            rts
        not_swimming2:
            lda $057d                       ; Link's Y velocity (original code).
            bpl moving_down
            ldy #$30
        moving_down:
            rts


        link_movement_routine:
            lda     swim_enabled
            bne     slow_link_movement_routine
            jmp     bank7_xy_movement_routine

        ;; Hack the movement routine to change the bitfield encoding of the
        ;; acceleration parameters.  Instead of <4,4> of <pix,subpix>,
        ;; change to <3,5> of <pix,subpix>.  Allows for more sluggish motion.
        slow_link_movement_routine:
            lda      $70,x
            asl
            asl
            asl
            sta      $01
            lda      $70,x
            lsr
            lsr
            lsr
            lsr
            lsr
            cmp      #$04
            bcc      save_signed_result
            ora      #$F8
        save_signed_result:
            sta      $00
            jmp      bank7_xy_computation


        max_walk_speed:
        ;; The max walk speed is interpreted in 4-bit <pix,subpix> units.
        .db $18,$e8

        max_swim_speed:
        ;; The max swim speed is interpreted in <3,5>-bit <pix,subpix> units.
        .db $20,$E0

        check_max_speed:
            ldx     swim_enabled
            beq     check_walk_speed
            cmp     max_swim_speed,y
            rts
        check_walk_speed:
            cmp     max_walk_speed,y
            rts
        .assert_org {freespace+length}

        ;; Hack swim into jump routine
        .org $951c
            jsr swim1           ; Get the initial swim gravity for the first press of A.

        .org $9535
            jsr swim2           ; Override Y-vel on subsequent presses of A.
            nop
            nop
            nop
            nop

        ;; Hack link's xy movement
        .org $9628
            jsr link_movement_routine

        ;; Patch in max speed check
        .org $93ff
            jsr check_max_speed
        .org $940e
            jsr check_max_speed

    """)
    return config
