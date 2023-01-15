import sqlite3


def get_result(name="films_db.sqlite"):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute(
        """UPDATE films
        set duration = 100 
        from films f
        join genres g
        on f.genre = g.id
        where duration > 100 and g.title = 'мюзикл'""")
    con.commit()
    con.close()
