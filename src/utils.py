def gen_search_query(params):
    query = ""
    for k, v in params.items():
        query += str(k) + '=' + str(v) + "*"

    return query[:-1]