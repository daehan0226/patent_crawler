
from src.utils import gen_search_query


def test_gen_search_query():

    query = gen_search_query({"GD":"[20210101~20211231]", "AD":"[20210101~20211231]"})
    assert query == "GD=[20210101~20211231]*AD=[20210101~20211231]"
    