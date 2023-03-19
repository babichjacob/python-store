from store import get, writable


def test_get():
    a_store = writable(32)
    assert get(a_store) == 32
