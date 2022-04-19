from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    result = run_sql(sql)
    for row in result:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


def delete_all():
    sql = "DELETE  FROM tasks" 
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s" 
    values = [id]
    run_sql(sql, values)