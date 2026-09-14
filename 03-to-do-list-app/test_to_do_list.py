from to_do_list import is_valid_index


def test_is_valid_index():
    tasks = ["a", "b", "c"]
    assert is_valid_index(1, tasks) == True
    assert is_valid_index(3, tasks) == True
    assert is_valid_index(0, tasks) == False
    assert is_valid_index(4, tasks) == False