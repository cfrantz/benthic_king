# Technical Details for Benthic King

## **WARNING SPOILERS AHEAD!**

This document describes the technical details for the hacks in *Benthic King*.

## Title Text Roll

The replacement of the title text roll with a new storyline is perhaps the
most straightfoward hack and should only really be considered a hack because
CF207 never wrote an editor module for the title text in Z2Edit.

The text roll is just a list of text strings which the game will write to
the screen during the game introduction.  The hack simply rewrites these
strings with the *Benthic King* storyline.  Each line of text must be
exactly 28 characters and there are 15 lines of text.

The text is tranlated from ASCII to the Z2 characterset and written into the
know ROM locations for the title text roll.

## Credits

The end-of-game credits hack is similar to the title screen hack, but
slightly more complicated.  The original string lengths of the credits are
quite limiting and make it very difficult to display proper credits.

Fortunately, the credits are represented as *PPU Macros* referenced by a table,
so we can simply rewrite the entire table and set of macros.  Each credit
consists of a *title* and one or two lines of credits, and the table of pointers
just alternates: title, credit, title, credit, ... etc.

The hack deletes the original credits and writes a new series of PPU macros
with the new credits.  The structure of a PPU macro is:

```
ppu_addr_high_byte, ppu_addr_low_byte, lenght, bytes, ..., $FF
```

The hack creates a series of these structures in the ROM and then adjusts
the credits pointer taible to point at the newly created structures.

## Overworld Tileset Expansion

The overworld tileset expansion hack increases the number of tiles available on
the overworld from 16 to 64, but at the cost of poorer encoding density within
the ROM.

Each overworld tile (really overworld *meta*tile) is made up of 4 PPU tiles
which are encoded as a table of 16 four-byte entries in the vanilla game.
Furthermore, there is a simple table of 16 one-byte entries which describe
which of the 4 PPU background palettes to use for each tile.

The overworld maps are compressed in ROM using run-length encoding (RLE), which
simply means each horizontal run of the same tile is encoded as a count followed
by a tile number.  Because there are only 16 tiles in the vanilla game, the
original programmers natuarlly used the low-nybble to encode the tile type and
the high-nybble to encode the run length (actually run-length minus one becase
it doesn't make sense to have a run of 0 tiles).

There are certain objects on the overworld that are very unlikely to have more
than one tile in a row: boulder, spider, town, palace or cave.  To expand the
tileset, we took the spider (tile number 15, or $F in hex) and repurposed the
high-nybble to represent an *escape sequence* meaning the the decompressor
should do something different than what it normally does:

- Encoding $0F means place the spider on the overworld.
- Encodings $1F, $2F, $3F .. $FF mean that there is ${high-nybble} count of an
  expansion tile, with the tile number of the expansion tile in the following
  byte.

The hack creates a new metatile table for all 64 tiles (including the
16 vanilla-game tiles) and a palette mapping table for the new tiles.
The hack also supplies a new overworld decompression routine which performs
the same function as the vanilla decompressor routine _and_ recognizes the
escape sequence discussed earlier.

The hack patches this new decompression routine and tile table pointers into
the appropriate locations within the ROM.

Lastly, this hack requires support from Z2Edit, as it represents a significant
change from how the original game worked.  The hack alters Z2Edit's
configuration to inform the editor that there are now 64 overworld tiles and
that a new compression scheme is being used.

## Barba Projectiles

The final boss of *Benthic King* is "The Fish King", who is really a
repurposed Barba.  To make the final boss more challenging (and entertaining),
Barba's projectile routine was changed to shoot projectiles either up or
down depending on Link's location relative to Barba.

Note: All ROM memory addresses discussed in this section are in bank 4.

In Barba's AI routine, a new projectile is spawned at `$B195` by calling 
the routine at `$9BE5` (which is part of the energy-ball shooter, aka the
wall-mounted Ras and Rat-heads which shoot at Link).  That routine sets
up a new projectile and loads a downward vertical velocity into `$0584`.

When we return back to Barba's AI routine, the game sets the initial
vertical position of Barba's fireballs at `$B1AB`.  We patch
over this code with a jump to our own code which compares Barba's vertical
position against Link's vertical position, and if Link is higher on the
screen than Barba, we flip the sign of the verical velocity.

We then position the initial starting position of the projectiles just
as the vanilla game did, making up for the fact that we stomped on that
code to insert our patch.

## Boss Item Drops

In the vanilla game, bosses always drop a key after their defeat.  In
*Benthic King*, some bosses drop an item for Link to use later:  Horsehead
drops the glove and Helmethead drops his diving helmet (aka the boots).

Note: All ROM memory addresses discussed in this section are in bank 7.

The orignial game code transforms dead bosses into keys at `$DE18`.  In order
to cause the game to drop other items besides the key, we patch over the
original game code with a jump to our hack routine.

The hack routine defines a table of rooms where boss fights occur and the
corresponding item we want to drop after that boss is defeated.
The tranformation routine compares Link's current room number against the
table and drops the corresponding item.  If no match is made, we drop a key
to preserve original game behavior.

We also have to patch the item pickup routine because the vanilla game requires
Link to pick up the key to unlock the screen after a boss fight.  We modify
the routine to unlock the screen in response to any item pickup.

## Heart/Magic containers in Palaces

In the vanilla game, heart and magic containers never appear in palaces and
the CHR banks for palaces don't even contain the graphics for them.

In order to allow the heart and magic containers to be universally available
items, we re-arranged the sprites in the various banks to a more logical
arrangement.

In the vanilla game:

- In palace banks:
  - CHRs `$9c` and `$9d` are a comma and an empty space (e.g. not used).
  - CHRs `$b0` and `$b1` are a spike (also not used).
  - CHRs `$82` and `$83` are part of a Link-holding-up-an-item sprite.
- In overworld banks:
  - CHRs `$9c` and `$9d` are a comma and a fragment of cave wall (partly used).

Since we want the sprite IDs for the Heart container, Magic container and
Kid/Medicine to be universal, we'll rearrange the sprites as:

- Link holding up an item will overwrite the spike.
- The Kid/Medicine will be moved into the comma/cave wall location and the cave
  cave wall (in overworlds) will take the old Kid/Medicine location.
- The Heart and Magic containers will move into CHRs `$80-$83` in the palace
  banks, which is where they are located in the overworld-caves and town banks.

After performing these tile moves, we rewrite the meta-tile and sprite tablesx
in the ROM to use the newly assigned CHRs.

## Town-like Doors in Palaces

To create a more interesting and challenging palace layout, we added town-like
doors into palaces.  This gives the palace designer the ability to create
more interesting mazes in the palace with some non-linear jumps between
different areas.  In *Benthic King* we used these doors to create a
sort-of *front side* and *back side* to our palace designs.

The door transfer code lives in bank 7, which means it is available throughout
the entire game.  What is required to activate it is a meta-tile which
represents the door, a sensible door transfer table and the ability to draw
the door object on the screen.

Note: All ROM memory addresses discussed in this section are in banks 4 and 7.

By examining the metatile table for palace objects located at `$817B`,
we see that metatiles `$00`, `$01` and `$11` (and their aliases starting
at `$40`) are unused.  We also know from looking at the small objects
construction table at `$8133` that small objects 5 and 6 are identical
copeis of the typical palace locked door.  We also know that small object
6 is never used in the game.

In order to draw a town-like door, we adapt metatile `$41` to be the door
frame header, `$40` to be the open door and `$51` to be the floor underneath
the open door, which is also the action trigger for the door.

We insert a short fragment of code to draw these metatiles to the map.  This
fragment of code is basically a copy of the drawing routine for any 1-tile
wide vertical object in the game, but it references our table of metatiles
for the door.

We then update the *magic tile action table* at `$851a` which causes the game to
perform the door connection transfer when Link is standing on the door's
floor tile and the player presses up.

We also hack the music routine to not change the music when Link enters
a door while Link is in a palace.

The door transfer table is located in every side-view bank at `$8817` and is
28 four-byte entries long (one byte per screen in a sideview area).  The
length of the table means the game may only have town-like doorways on the
first 28 (of 62) sideview areas in any world.  Furthermore, in a
two-world bank (like the palace bank), the door transfter table applies to
*both* worlds.  A game designer must plan the use of doors very between
the two palace worlds.

## Swim Physics

TODO: create a more detailed explanation.

We have a table of rooms in which we want swim physics.  When link enters
one of these rooms, a flag is set in a RAM variable.  We then hack the
jump routine and walk routine to apply different gravity and acceleration
parameters to Link when this RAM variable is set to a non-zero value.


## Victory

In *Benthic King*, the game is over after your defeat The Fish King (aka
Barba) and collect the Trident (aka the Kid).  There is a global game
state variable in RAM location `$076C` and setting this location to the
appropriate value will automatically send the game to the victory sequence.

We simply change the fragment of code which executes when link picks up
the kid to write the victory value into `$076c`.
