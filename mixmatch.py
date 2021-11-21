import enum


class Colors(enum.Enum):
    red = enum.auto()
    yellow = enum.auto()
    blue = enum.auto()
    green = enum.auto()
    orange = enum.auto()
    purple = enum.auto()
    empty = enum.auto()


red_transitions = {
    Colors.red: Colors.red,
    Colors.yellow: Colors.orange,
    Colors.blue: Colors.purple,
    Colors.empty: Colors.red
}

yellow_transitions = {
    Colors.red: Colors.orange,
    Colors.yellow: Colors.yellow,
    Colors.blue: Colors.green,
    Colors.empty: Colors.yellow
}

blue_transitions = {
    Colors.red: Colors.purple,
    Colors.yellow: Colors.green,
    Colors.blue: Colors.blue,
    Colors.empty: Colors.blue
}


def mix_red(s: Colors) -> Colors:
    return red_transitions[s]


def mix_yellow(s: Colors) -> Colors:
    return yellow_transitions[s]


def mix_blue(s: Colors) -> Colors:
    return blue_transitions[s]


def mix_many(s: Colors, mixes: str) -> Colors:
    for c in mixes:
        c = c.lower()
        if c == 'r':
            s = mix_red(s)
        elif c == 'y':
            s = mix_yellow(s)
        elif c == 'b':
            s = mix_blue(s)
        else:
            raise ValueError('invalid mix')
    return s


def test_many_slaps():
    assert mix_many(Colors.empty, 'rr') is Colors.red
    assert mix_many(Colors.empty, 'yy') is Colors.yellow
    assert mix_many(Colors.empty, 'bb') is Colors.blue
    assert mix_many(Colors.empty, 'ry') is Colors.orange
    assert mix_many(Colors.empty, 'rb') is Colors.green
    assert mix_many(Colors.empty, 'br') is Colors.purple
