SELECT_RANDOM_YEAR = {
    'query' : """
              SELECT `year` 
              FROM (
                  SELECT DISTINCT(YEAR(release_date)) AS `year` 
                  FROM song
                  ORDER BY RAND()
              ) AS rand_year
              LIMIT 1
              """,
    'mode'  : 'select'
}