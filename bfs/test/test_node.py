from bfs.graph import PersonNode


def test_can_get_hash_code():
    bob = PersonNode("bob")
    jen = PersonNode("jen")

    people = {
        bob: bob,
        jen: jen
    }

    assert people[bob].key == "bob"
    assert people[jen].key == "jen"
