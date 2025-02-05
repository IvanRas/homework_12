from src.processing import filter_by_state, operations, sort_by_date


def test_filter_by_state(test_operations):
    assert filter_by_state(operations, state=test_operations)


def test_filter_by_state_1(test_operations_1):
    assert filter_by_state(operations) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state_sort(test_operations_1):
    assert sort_by_date(operations) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
