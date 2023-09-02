
def count_pop_slow(mask):
    """Count bits population"""
    count = 0
    while mask:
        count += mask & 1
        mask >>= 1
    return count


def count_pop(mask):
    """Count bits population optimized"""
    count = 0
    while mask:
        count += 1
        mask &= mask - 1
    return count
