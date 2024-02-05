-- select all articles with their author’s email
SELECT A.title, A.content, U.email
FROM article A 
JOIN user U ON U.id = A.author_id

-- select articles from 7th to 12th sorted by id.
SELECT * FROM article
WHERE id BETWEEN 7 and 12
ORDER BY id
-- alternative
SELECT * FROM article
ORDER BY id
LIMIT 6 OFFSET 6
