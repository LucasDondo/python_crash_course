import pytest
from c_repos import (
    get_request,
    get_r_dic,
    get_status_code,
    get_result_incompletion,
    get_total_count,
    get_q_repos,
)


@pytest.fixture
def r():
    return get_request()


@pytest.fixture
def d(r):
    return get_r_dic(r)


def test_status_code(r):
    """Tests the status code."""
    assert get_status_code(r) == 200


def test_q_repos(d):
    """Tests the amount of repos."""
    assert get_q_repos(d) == 30


def test_result_incompletion(d):
    """Tests the amount of repos."""

    if get_result_incompletion(d):
        assert get_q_repos(d) < get_total_count(d)
    else:
        assert get_q_repos(d) == get_total_count(d)
