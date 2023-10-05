from gilded_rose.main import Item, update_quality


def test_item_name_does_not_change_when_updating_quality():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert "foo" == item.name


def test_item_sell_in_decreases_by_one_when_updating_quality():
    item = Item("foo", 5, 5)
    update_quality([item])
    assert 4 == item.sell_in


def test_item_quality_decreases_by_one_when_updating_quality():
    item = Item("foo", 5, 5)
    update_quality([item])
    assert 4 == item.quality


def test_item_quality_does_not_decrease_to_a_negative_value():
    item = Item("foo", 0, 0)
    update_quality([item])
    assert 0 == item.quality


def test_item_quality_degrades_by_2_when_sell_in_is_0():
    item = Item("foo", 0, 10)
    update_quality([item])
    assert 8 == item.quality
