from gilded_rose.main import Item, update_quality

SULFURAS = "Sulfuras, Hand of Ragnaros"


def test_sulfuras_sell_in_does_not_decrease_when_updated():
    item = Item(SULFURAS, 1, 0)
    update_quality([item])
    assert 1 == item.sell_in


def test_sulfuras_quality_does_not_decrease_when_updated():
    item = Item(SULFURAS, 1, 80)
    update_quality([item])
    assert 80 == item.quality
