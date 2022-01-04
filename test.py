import unittest
from src.utils import gen_search_query

class Tests(unittest.TestCase): 

    def test_gen_search_query(self):

        query = gen_search_query({"GD":"[20210101~20211231]", "AD":"[20210101~20211231]"})
        self.assertEqual(query, "GD=[20210101~20211231]*AD=[20210101~20211231]")
        

if __name__ == '__main__':  
    unittest.main()