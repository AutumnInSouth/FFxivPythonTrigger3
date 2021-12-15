from . import the_mother_crystal, the_dark_inside

events = {'the_mother_crystal_' + n: evt for n, evt in the_mother_crystal.events.items()} | \
         {'the_dark_inside_' + n: evt for n, evt in the_dark_inside.events.items()}
