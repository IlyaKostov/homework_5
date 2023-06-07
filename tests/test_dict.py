import pytest

from utils.dicts import get_val


@pytest.fixture
def dict_fixture():
    return {"vcs": "mercurial", "bbc": "news"}


def test_get_val(dict_fixture):
    assert get_val(dict_fixture, 'vcs') == 'mercurial'
    assert get_val(dict_fixture, 'bbc', 'git') == 'news'
    assert get_val(dict_fixture, 'abc') == 'git'
    assert get_val({}, 'vcs') == 'git'
    assert get_val({}, 'vcs', 'sorry') == 'sorry'
