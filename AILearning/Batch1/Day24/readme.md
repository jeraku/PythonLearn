Parent retrival

Userquery -> related  chunks (Size =500 chars) (Smaller data) > 

Example:We have Mulitple chunks in a PDF copy. 

Paragrah p1 (chunk1) (250 char)
Paragrah p2 (chunk2) (250 char)

user query : how to create a dictionary. 

Dictionary is present in chunk4 P4 alone. then it will not give proper answer for you.

so context will be found at first then reponse will be provided. 

User query related information will be referred from metadata and pull the releated answers. give the response.

In langchain : we have the concept and mathematical formula for this already. so we can reuse the same while developing it.

Parent and child concept> document will pull into a different paragraphs. 
and split the parent into different chunks again. and embed the child chunks.



