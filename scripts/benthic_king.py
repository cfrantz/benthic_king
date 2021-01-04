import z2edit
from z2edit.util import ObjectDict

import barba_projectiles
import boss_key
import credits
import hc_mc_in_palaces
import palace_doors
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
    config = swim.hack(config, edit, asm)
    config = tile_expansion.hack(config, edit, asm)
    config = title_text.hack(config, edit, asm)
    config = victory.hack(config, edit, asm)

    # Now tell the editor about the new configuration.
    name = meta['config'] + '-hacks'
    z2edit.config[name] = config.to_json()
    # Now tell the project about the new configuration.
    meta['extra'] = {'next_config': name}
    edit.meta = meta
