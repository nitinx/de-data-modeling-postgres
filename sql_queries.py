# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS dim_user;"
song_table_drop = "DROP TABLE IF EXISTS dim_song;"
artist_table_drop = "DROP TABLE IF EXISTS sim_artist;"
time_table_drop = "DROP TABLE IF EXISTS dim_time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplay (
   songplay_id SERIAL PRIMARY KEY,
   start_time  VARCHAR (50),
   user_id     VARCHAR (50),
   level       VARCHAR (50),
   song_id     VARCHAR (50),
   artist_id   VARCHAR (50),
   session_id  VARCHAR (50),
   location    VARCHAR (500),
   user_agent  VARCHAR (500)
);
""")

user_table_create = ("""
CREATE TABLE dim_user (
   user_id    VARCHAR (50) NOT NULL PRIMARY KEY,
   first_name VARCHAR (50),
   last_name  VARCHAR (50),
   gender     VARCHAR (50),
   level      VARCHAR (50)
);
""")

song_table_create = ("""
CREATE TABLE dim_song (
   song_id    VARCHAR (50) NOT NULL PRIMARY KEY,
   title      VARCHAR (1000),
   artist_id  VARCHAR (50),
   year       INT,
   duration   VARCHAR (50)
);
""")

artist_table_create = ("""
CREATE TABLE dim_artist (
   artist_id VARCHAR (50) NOT NULL PRIMARY KEY,
   name      VARCHAR (500),
   location  VARCHAR (500),
   latitude  VARCHAR (50),
   longitude VARCHAR (50)
);
""")

time_table_create = ("""
CREATE TABLE dim_time (
   start_time VARCHAR (50) NOT NULL PRIMARY KEY,
   hour       INT,
   day        INT,
   week       INT,
   month      INT,
   year       INT,
   weekday    INT
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO dim_user (user_id, first_name, last_name, gender, level) 
     VALUES (%s, %s, %s, %s, %s)
     ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO dim_song (song_id, title, artist_id, year, duration) 
     VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO dim_artist (artist_id, name, location, latitude, longitude) 
     VALUES (%s, %s, %s, %s, %s)
""")

time_table_insert = ("""
INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday) 
     VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT dim_song.song_id, dim_song.artist_id
  FROM dim_song
  JOIN dim_artist ON dim_song.artist_id = dim_artist.artist_id
 WHERE title = %s
   AND name = %s
   AND duration = cast ( %s as VARCHAR)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]