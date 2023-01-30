import sqlite3

def get_all(query: str):

    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory =sqlite3.Row

        result = []

        for item in conn.execute(query).fetchall():
            result.append(dict(item))

        return result

def get_one(query: str):

    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row

        result = conn.execute(query).fetchone()

        if result is None:
            return None
        else:
            return dict(result)



def get_movie_by_genre(type_movie, release_year,listed_in):
    query = f"""
    select title, description from netflix
    where "type" = '{type_movie}'
    and release_year = {release_year}
    and listed_in like '%{listed_in}%'
    """

    result = []

    for item in get_all(query):
        result.append(
            {
                'title': item['title'],
                'description': item['description'],
            }
        )

    return result

def search_by_cast(name1: str ='Jack Black', name2: str = 'Dustin Hoffman'):
    query = f"""
    select * from netflix 
    where netflix.cast LIKE '%Jack Black%' AND netflix.cast like '%Dustin Hoffman%'
    """

    cast = []
    set_cast = set()
    result = get_all(query)

    for item in result:
        for actor in item['cast'].split(','):
            cast.append(actor)

    for actor in cast:
        if cast.count(actor) > 2:
            set_cast.add(actor)

    return list(set_cast)


