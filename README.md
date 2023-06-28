# Topic modeling of Stack Overflow Posts
In this projects, the keywords like `GPT and ChatGPT` were searched on StackOverflow and the returned results have been considered for further analysis. 
## Data Source
The following SQL Queries were Executed on `Stack Exchhange Data Explorer`:
### Query 1
~~~~sql
SELECT posts.Id AS [Post Link], posts.PostTypeId, posts.OwnerUserId, posts.AcceptedAnswerId AS [Answer Link], posts.Title, posts.Body, posts.CreationDate, posts.ClosedDate, posts.LastEditDate, posts.LastActivityDate, posts.Tags, posts.AnswerCount, posts.CommentCount, posts.Score, posts.ViewCount, posts.FavoriteCount, acc.PostTypeId, acc.OwnerUserId, acc.Body, acc.CreationDate, acc.CommentCount, acc.Score
FROM Posts
AS posts left outer join Posts acc on posts.AcceptedAnswerId = acc.Id
WHERE posts.Tags LIKE '%chatgpt%' OR posts.Tags LIKE '%chatgpt-api%'
~~~~
This query returned `259` StackOVerflow Posts.
### Query 2
~~~~sql
SELECT posts.Id AS [Post Link], posts.PostTypeId, posts.OwnerUserId, posts.AcceptedAnswerId AS [Answer Link], posts.Title, posts.Body, posts.CreationDate, posts.ClosedDate, posts.LastEditDate, posts.LastActivityDate, posts.Tags, posts.AnswerCount, posts.CommentCount, posts.Score, posts.ViewCount, posts.FavoriteCount, acc.PostTypeId, acc.OwnerUserId, acc.Body, acc.CreationDate, acc.CommentCount, acc.Score
FROM Posts
AS posts left outer join Posts acc on posts.AcceptedAnswerId = acc.Id
WHERE posts.Tags LIKE '%gpt-2%' OR posts.Tags LIKE '%gpt-3%' OR posts.Tags LIKE '%gpt-4%'
~~~~
This query returned `460` StackOverflow Posts.
### Dataset Description
| Column | Description |
| ----------- | --------------|
| Post Link | Unique StackOverlow Question Identifier |
| PostTypeId | 1 - represents questions and 2 - represents answer |