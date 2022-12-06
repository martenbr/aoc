import aocutils


def test_section_parse():
    assert list(aocutils.sections_from_lines([
        "a",
        "abc",
        "",
        "c",
        "d",
    ])) == [["a", "abc"], ["c", "d"]]

    assert list(aocutils.sections_from_lines([
        "a\n",
        "abc\n",
        "\n",
        "c\n",
        "d\n",
        "\n",
    ])) == [["a", "abc"], ["c", "d"]]


def test_multisplit():
    assert aocutils.multisplit("1-3 b: cdefg", ["-", " ", ": "]) == ["1", "3", "b", "cdefg"]


def test_parseints():
    assert aocutils.parseints('move 1 from 2 to 1') == [1, 2, 1]
    assert aocutils.parseints('move 23 from 2 to 4') == [23, 2, 4]
    assert aocutils.parseints('24-93,25-93') == [24, 93, 25, 93]
    assert aocutils.parseints('target area: x=155..182, y=-117..-67') == [155, 182, 117, 67]
    assert aocutils.parseints('target area: x=155..182, y=-117..-67', negative=True) == [155, 182, -117, -67]
