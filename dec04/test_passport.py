from dec04.passport2 import check_field


def test_field():
    assert check_field('byr', '2002')
    assert not check_field('byr', '2003')

    assert check_field('hgt', '60in')
    assert check_field('hgt', '190cm')
    assert not check_field('hgt', '190in')
    assert not check_field('hgt', '190')

    assert check_field('hcl', '#123abc')
    assert not check_field('hcl', '#123abz')
    assert not check_field('hcl', '123abc')

    assert check_field('ecl', 'brn')
    assert not check_field('ecl', 'wat')

    assert check_field('pid', '000000001')
    assert not check_field('pid', '0123456789')
