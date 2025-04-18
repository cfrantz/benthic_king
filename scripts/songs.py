from z2edit import Address
from z2edit.experimental.musiclib import (
        Song,
        Pattern,
        OVERWORLD_SONG_TABLE,
        TOWN_SONG_TABLE,
        PALACE_SONG_TABLE,
        GP_SONG_TABLE,
)

PALACE_INTRO = Song(
    pattern=[
        Pattern(0x08,
            [0xb0, 0xa8, 0xa2, 0x98, 0xa8, 0xa2, 0x98, 0x90, 0xa2, 0x98, 0x90, 0x8a, 0x98, 0x90, 0x8a, 0x84],
            [0x43, 0x43, 0x43, 0x43],
            [0x43, 0x43, 0x43, 0x43],
            [])
    ],
    sequence=[0]
)

PALACE_THEME = Song(
    pattern=[
        Pattern(0x28,
            [ 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xe8, 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xa8, 0xb0 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
        Pattern(0x28,
            [ 0x86, 0x94, 0x9e, 0x67, 0x82, 0x86, 0x94, 0x9e, 0xe6, 0xac, 0xe6, 0x86, 0x94, 0x9e, 0x67, 0x82, 0x86, 0x94, 0x9e, 0xe6, 0xac, 0xa6, 0xac ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
        Pattern(0x28,
            [ 0x71, 0xc2, 0xec, 0x37, 0x33, 0xec, 0x71, 0xc2, 0xec, 0x37, 0x33, 0xe8 ],
            [ 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xe8, 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xa8, 0xb0 ],
            [ 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
        Pattern(0x28,
            [ 0x67, 0xc2, 0xe2, 0x27, 0x29, 0xec, 0x67, 0xc2, 0xe2, 0x67, 0x5f ],
            [ 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xe8, 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xa8, 0xb0 ],
            [ 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
        Pattern(0x28,
            [ 0x82, 0xb2, 0xb2, 0xb2, 0x71, 0x82, 0xb2, 0xb2, 0xb2, 0xf0, 0xe8, 0x82, 0xb2, 0xb2, 0xb2, 0xf0, 0xe8, 0x27, 0x29, 0xec ],
            [ 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xe8, 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xa8, 0xb0 ],
            [ 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94, 0x94 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
        Pattern(0x28,
            [ 0x63, 0xc2, 0xde, 0x23, 0x27, 0xe8, 0x63, 0xc2, 0xde, 0x63, 0x61 ],
            [ 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xe8, 0x8a, 0x98, 0xa2, 0x69, 0x82, 0x8a, 0x98, 0xa2, 0xe8, 0xb0, 0xa8, 0xb0 ],
            [ 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x86, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8a, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x8e, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90 ],
            [ 0xc8, 0x88, 0x09, 0xc8 ]),
    ],
    sequence=[0, 1, 2, 3, 2, 3, 4, 5, 2, 3, 2, 3, 4, 5]
)

BOSS_THEME = Song(
    pattern=[
        Pattern(0x18,
            [ 0x82, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0x37, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0x37, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0xb6, 0xb8, 0xbc, 0xb8, 0xb6, 0xb4, 0xb6, 0xb4, 0xb0, 0xae ],
            [ 0x19, 0x19, 0xd8, 0x17, 0x17, 0xd6, 0x15, 0x15, 0xd4, 0x13, 0x13, 0xd2 ],
            [ 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2 ],
            [ 0xc8, 0x49, 0x49, 0x49, 0x88, 0x88 ]),


        Pattern(0x18,
            [ 0x82, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0x37, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0x37, 0xb0, 0xb0, 0xae, 0xb0, 0xb4, 0xb6, 0xb8, 0xbc, 0xb8, 0xb6, 0xb8, 0xfc, 0xf8 ],
            [ 0x19, 0x19, 0xd8, 0x17, 0x17, 0xd6, 0x15, 0x15, 0xd4, 0x13, 0x13, 0xd2 ],
            [ 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2 ],
            [ 0xc8, 0x49, 0x49, 0x49, 0x88, 0x88 ]),

        Pattern(0x18,
            [ 0xc2, 0xf0, 0xb4, 0xf6, 0x39, 0xf6, 0xf8, 0x7d, 0xf0, 0xb4, 0xf6, 0x39, 0xf6, 0x75 ],
            [ 0x19, 0x19, 0xd8, 0x17, 0x17, 0xd6, 0x15, 0x15, 0xd4, 0x13, 0x13, 0xd2 ],
            [ 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2 ],
            [ 0xc8, 0x49, 0x49, 0x49, 0x88, 0x88 ]),

        Pattern(0x18,
            [ 0xc2, 0xf0, 0xb4, 0xf6, 0x79, 0x37, 0xf8, 0x3d, 0x39, 0xf6, 0xf8, 0xf6, 0xf4, 0xee ],
            [ 0x19, 0x19, 0xd8, 0x17, 0x17, 0xd6, 0x15, 0x15, 0xd4, 0x13, 0x13, 0xd2 ],
            [ 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x98, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9c, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0x9e, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2, 0xa2 ],
            [ 0xc8, 0x49, 0x49, 0x49, 0x88, 0x88 ]),
    ],
    sequence=[0, 1, 0, 1, 2, 3]
)

CREDITS_THEME = Song(
    pattern=[
        Pattern(0x28,
            [ 0x82, 0xb0, 0xb0, 0xae, 0xb0, 0x34, 0x37, 0x02, 0xf0, 0xae, 0xb0, 0x34, 0x37, 0x02, 0xb0, 0xb0, 0xae, 0xb0, 0x34, 0x76, 0xb8, 0x75, 0x43 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x98, 0x82, 0x98, 0x82, 0x8e, 0x82, 0x94, 0x82, 0x98, 0x82, 0x98, 0x82, 0x8e, 0x82, 0x94, 0x82, 0x98, 0x82, 0x98, 0x82, 0x8e, 0x82, 0x94, 0x82, 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa6, 0x82 ],
            []),
        Pattern(0x28,
            [ 0x82, 0xf8, 0xb8, 0xb8, 0x36, 0x35, 0x02, 0xb8, 0xb8, 0xb8, 0xb8, 0x36, 0x35, 0x02, 0xf8, 0xb8, 0xb8, 0x36, 0x74, 0xb6, 0x71, 0x43 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa6, 0x82, 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa6, 0x82, 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa6, 0x82, 0x98, 0x82, 0x98, 0x82, 0x8e, 0x82, 0x94, 0x82 ],
            []),
        Pattern(0x28,
            [ 0xf6, 0xb4, 0xf0, 0xb6, 0xb4, 0xb0, 0xf6, 0xb4, 0xb4, 0xb0, 0xe8, 0x67, 0x43, 0x82 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0x98, 0x82, 0x8e, 0x82, 0x94, 0x82 ],
            []),
        Pattern(0x28,
            [ 0xf6, 0xb4, 0xf0, 0xb6, 0xb4, 0xb0, 0xf8, 0xb6, 0xb6, 0xb4, 0xf6, 0x75, 0x43, 0x82, 0x77, 0x75 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x98, 0x82, 0xa8, 0x82, 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa2, 0x82, 0xa6, 0x82, 0xa2, 0x82, 0x9c, 0x82, 0x96, 0x82 ],
            []),
        Pattern(0x28,
            [ 0xf6, 0xf4, 0xf6, 0xf4, 0xb6, 0xb4, 0xb0, 0xb4, 0xb6, 0xb4, 0xb6, 0xb8, 0xf6, 0xf4, 0xf6, 0xf4, 0xb6, 0xb4, 0xb0, 0xb4, 0xb6, 0xb8, 0xb6, 0xb4 ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x98, 0x82, 0xa2, 0x82, 0x98, 0x82, 0xa2, 0x82, 0x98, 0x82, 0xa2, 0x82, 0x98, 0x82, 0xa2, 0x82, 0x96, 0x82, 0xa2, 0x82, 0x96, 0x82, 0xa2, 0x82, 0x96, 0x82, 0xa2, 0x82, 0x96, 0x82, 0xa2, 0x82 ],
            []),
        Pattern(0x28,
            [ 0xf6, 0xf4, 0xf6, 0xf4, 0xb6, 0xb4, 0xb0, 0xb4, 0xb6, 0xb8, 0xb6, 0xb8, 0x7d, 0x43, 0x43, 0x7d ],
            [ 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43, 0x43 ],
            [ 0x94, 0x82, 0xa2, 0x82, 0x94, 0x82, 0xa2, 0x82, 0x94, 0x82, 0xa2, 0x82, 0x94, 0x82, 0xa2, 0x82, 0x8e, 0x82, 0x96, 0x82, 0x9c, 0x82, 0xa2, 0x82, 0xa6, 0x82, 0xa2, 0x82, 0x9e, 0x82, 0x96, 0x82 ],
            []),
    ],
    sequence = [0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5]
)


def hack(project, config):
    songs = Song.read_all_songs(project.rom)

    Song.commit(project.rom, PALACE_SONG_TABLE, [
            PALACE_INTRO,
            PALACE_THEME,
            BOSS_THEME,
            songs["PalaceItemFanfare"],
            songs["CrystalFanfare"],
    ])

    Song.commit(project.rom, GP_SONG_TABLE, [
            songs["GreatPalaceIntro"],
            songs["GreatPalaceTheme"],
            songs["ZeldaTheme"],
            CREDITS_THEME,
            songs["GreatPalaceItemFanfare"],
            songs["TriforceFanfare"],
            songs["FinalBossTheme"],
    ])

    # Split the timbres of the pulse wave channels
    project.rom.write_bytes(Address.Prg(6, 0x9d34), bytes([0xa8, 0x9d]))

    # Pulse 1 timbre
    project.rom.write_bytes(Address.Prg(6, 0x9135), bytes([
        0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97,
        0x98, 0x99, 0x9a, 0x9b, 0x9c, 0x9d, 0x9e, 0x9e,
        0x9f, 0x9e, 0x9c, 0x9a, 0x98, 0x96, 0x94, 0x92,
    ]))

    # Pulse 2 timbre
    project.rom.write_bytes(Address.Prg(6, 0x9da8), bytes([
        0x90, 0x92, 0x91, 0x93, 0x92, 0x94, 0x92, 0x91,
        0x93, 0x95, 0x93, 0x91, 0x93, 0x96, 0x93, 0x91,
        0x94, 0x97, 0x94, 0x91, 0x94, 0x98, 0x94, 0x91,
    ]))
