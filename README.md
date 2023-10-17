# Topic modeling of Stack Overflow Posts
In this project, the StackOverflow posts related to `NLP` topics have been considered for topic modeling. 
## Data Source
The following SQL Queries were Executed on `Stack Exchhange Data Explorer`:
### Query
~~~~sql
SELECT posts.Id AS [Post Link], posts.PostTypeId, posts.OwnerUserId, posts.AcceptedAnswerId AS [Answer Link], posts.Title, posts.Body, posts.CreationDate, posts.ClosedDate, posts.LastEditDate, posts.LastActivityDate, posts.Tags, posts.AnswerCount, posts.CommentCount, posts.Score, posts.ViewCount, posts.FavoriteCount, acc.PostTypeId, acc.OwnerUserId, acc.Body, acc.CreationDate, acc.CommentCount, acc.Score
FROM Posts
AS posts left outer join Posts acc on posts.AcceptedAnswerId = acc.Id
WHERE posts.Tags LIKE '%nlp%' OR posts.Tags LIKE '%nltk%' OR posts.Tags LIKE '%spacy%' OR posts.Tags LIKE '%stanford-nlp%' OR posts.Tags LIKE '%huggingface-transformers%' OR posts.Tags LIKE '%gensim%' OR posts.Tags LIKE '%word2vec%' OR posts.Tags LIKE '%sentiment-analysis%' OR posts.Tags LIKE '%bert-language-model%' OR posts.Tags LIKE '%named-entity-recognition%' OR posts.Tags LIKE '%tf-idf%' OR posts.Tags LIKE '%word-embedding%' OR posts.Tags LIKE '%topic-modeling%' OR posts.Tags LIKE '%opennlp%' OR posts.Tags LIKE '%spacy-3%' OR posts.Tags LIKE '%nlp-question-answering%'
~~~~
This query returned `47550` StackOVerflow Posts.

### Dataset Description
| Column | Description |
| ----------- | --------------|
| Post Link | Unique StackOverlow Question Identifier |
| PostTypeId | 1 - represents questions and 2 - represents answer |