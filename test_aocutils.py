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
