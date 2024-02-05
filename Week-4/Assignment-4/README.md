

## Create article table
```
CREATE TABLE article (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  author_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (author_id) REFERENCES user(id)
);
```

