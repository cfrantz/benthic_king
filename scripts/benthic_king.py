import z2edit
from z2edit.util import ObjectDict, Tile, chr_copy

import barba_projectiles
import boss_key
import credits
import hc_mc_in_palaces
import palace_doors
import songs
import swim
import tile_expansion
import title_text
import victory

def apply_all_hacks(edit, asm):
    # Get a local copy of the config so we can update it as we go.
    meta = edit.meta
    config = ObjectDict.from_json(z2edit.config[meta['config']])

    # Apply our hacks.
    config = barba_projectiles.hack(config, edit, asm)
    config = boss_key.hack(config, edit, asm)
    config = credits.hack(config, edit, asm)
    config = hc_mc_in_palaces.hack(config, edit, asm)
    config = palace_doors.hack(config, edit, asm)
    config = songs.hack(config, edit, asm)
    config = swim.hack(config, edit, asm)
    config = tile_expansion.hack(config, edit, asm)
    config = title_text.hack(config, edit, asm)
    config = title_text.hack_graphics(config, edit, asm)
    config = victory.hack(config, edit, asm)

    # I can't be bothered to make a CHR import for this:
    # I want P1's dynamic bank to look like P5 bricks, but be P2's bank so that
    # I still have Horse- and Helmet- Head.
    # Copy the bricks tiles from P5 to P2:
    for tile in (0x64, 0x65, 0x68, 0x69):
        chr_copy(edit, Tile(0x0b, tile), Tile(0x17, tile))
    # Copy HelmetHead's helmet to the boots in every bank.
    for bank in range(0, 0x1a, 2):
        chr_copy(edit, Tile(bank, 0x92), Tile(0x0b, 0x0a))
        chr_copy(edit, Tile(bank, 0x93), Tile(0x0b, 0x0b))

    # Now tell the editor about the new configuration.
    name = meta['config'] + '-hacks'
    z2edit.config[name] = config.to_json()
    # Now tell the project about the new configuration.
    meta['extra'] = {'next_config': name}
    edit.meta = meta
