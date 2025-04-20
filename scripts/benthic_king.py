from z2edit import Config
from z2edit.util import ObjectDict, Tile, chr_copy

from . import barba_projectiles
from . import boss_key
from . import credits
from . import game_over
from . import hc_mc_in_palaces
from . import palace_doors
from . import songs
from . import swim
from . import tile_expansion
from . import title_text
from . import victory

def hack(project):
    config = ObjectDict.from_json(project.config)

    barba_projectiles.hack(project, config)
    boss_key.hack(project, config)
    credits.hack(project, config)
    game_over.hack(project, config)
    hc_mc_in_palaces.hack(project, config)
    palace_doors.hack(project, config)
    swim.hack(project, config)
    tile_expansion.hack(project, config)
    title_text.hack(project, config)
    title_text.hack_graphics(project, config)
    victory.hack(project, config)
    songs.hack(project, config)

    project.config = config.to_json()

    # I can't be bothered to make a CHR import for this:
    # I want P1's dynamic bank to look like P5 bricks, but be P2's bank so that
    # I still have Horse- and Helmet- Head.
    # Copy the bricks tiles from P5 to P2:
    for tile in (0x64, 0x65, 0x68, 0x69):
        chr_copy(project.rom, Tile(0x0b, tile), Tile(0x17, tile))
    # Copy HelmetHead's helmet to the boots in every bank.
    for bank in range(0, 0x1a, 2):
        chr_copy(project.rom, Tile(bank, 0x92), Tile(0x0b, 0x0a))
        chr_copy(project.rom, Tile(bank, 0x93), Tile(0x0b, 0x0b))
