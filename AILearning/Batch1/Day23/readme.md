Query compression

user send a Query -> VectorDB
VectordB -> Top5 context -> prompt (Augment) -> LLM

If there is not relation between the query and then how it behaves
Example 
python +  fast API +  deployment and networking flow
In above multiple context has been formed. 

LLM give a query with different queries.

chunking -> compress the query in chunks.
user query -> Embed and moved to llm -> retrieve the query again 
which will return more token - so compress the response of the user query.

Options to do compress
LLM based compression (LLM gives query)
Embedding based compression (Cosine similarity)
Keyword based compression. (Unwanted keywords TF/IDF, BM25 algorithm to remove the keywords )

LLM based compression
User Query > chunk it -> embed it and store in vector db >  retirval from vector Db > and pass it to the LLM (In house LLM/ Local LLM) and generate another query. 
context length will be reduced and creates another query.
Instead of asking the direct question to LLM. compress the query (reduce the size of the query) and pass it to LLM.




