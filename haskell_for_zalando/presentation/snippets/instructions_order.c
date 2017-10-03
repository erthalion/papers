gtod = scd->tick_gtod + __gtod_offset;
clock = gtod + delta;
min_clock = wrap_max(gtod, old_clock);
max_clock = wrap_max(old_clock, gtod + TICK_NSEC);
