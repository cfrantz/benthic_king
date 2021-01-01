import z2edit
from z2edit.util import ObjectDict

import tile_expansion
import palace_doors

def apply_all_hacks(edit, asm):
    # Get a local copy of the config so we can update it as we go.
    meta = edit.meta
    config = ObjectDict.from_json(z2edit.config[meta['config']])

    # Apply our hacks.
    config = tile_expansion.hack(config, edit, asm)
    config = palace_doors.hack(config, edit, asm)

    # Now tell the editor about the new configuration.
    name = meta['config'] + '-hacks'
    z2edit.config[name] = config.to_json()
    # Now tell the project about the new configuration.
    meta['extra'] = {'next_config': name}
    edit.meta = meta
