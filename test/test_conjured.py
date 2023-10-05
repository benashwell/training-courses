from gilded_rose.main import Item, update_quality

CONJURED = "Conjured Mana Cake"


def test_conjured_degrades_by_2_when_sell_in_not_passed():
    item = Item(CONJURED, 5, 10)
    update_quality([item])
    assert 8 == item.quality


def test_conjured_degrades_by_4_when_sell_in_passed():
    item = Item(CONJURED, 0, 10)
    update_quality([item])
    assert 6 == item.quality
