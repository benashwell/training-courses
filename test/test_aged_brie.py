from gilded_rose.main import Item, update_quality

AGED_BRIE = "Aged Brie"


def test_quality_improves_when_updated():
    item = Item(AGED_BRIE, 3, 2)
    update_quality([item])
    assert 3 == item.quality


def test_quality_is_never_more_than_50():
    item = Item(AGED_BRIE, 0, 50)
    update_quality([item])
    assert 50 == item.quality
