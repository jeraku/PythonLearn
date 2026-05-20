Chunking 

Data -> chunk data -> Vector (LLM)-> store in Vector DB 

chunking is splitting the larger data into smaller pieces of data. 

If you have PDF then that will have mulitple content, with different context in it.

so after reading the content and sending to Embedding model (LLM), then pointers will be generated and to store the information in a vector DB. 

Whatever the data your sending for an LLM that will store as a single pointer in Vector DB. 

When we split the data, different sentences will get stored with different context. 
if a single sentence contains both the context, then its not necessary to return the values eventhough context is same, the value differs.
so chunking need to be done properly.
To overcome the problem, we have two different ways.
Discrete ways - like Formula method. 
Semantic way - search based on the similar word.

Doc= 
"python is a programming language."
"Python uses DB to connect and retrieve from data"

If search about python aobve displaying line should be fine. but when I search about DB- then I dont need to respond with above line. 
which is not necessary when the DB comes into picture.


LLM WILL NEVER SAY I DONT KNOW.

It will give random answer. We can control that while chunking the data.

Chunking methodlogies
1) Fixed chunking / Discrete chunking - setting chars limit -> 100. so in PDF while reading splits into 100 chars each. 
problem with Fixed chunking - while splitting, a word will also be splitted. Ex: America while splitting. AME RICA -> which is not right 
bitmaps -> [BIT,MAPS] -> this chunking value is differs. 
2) Overlap -> To overcome the above issue, we need to go with Overlap concept. while splitting the sentence it wil happen like 
0-50 chars and next step 40-90 and then 80-130.
in the above 10 characters will be overlapped.

To control chunking - you need to reuse the methods defined in the package and control the chunking.

overlap increases then more tokens will be used. so think how you want to perform.

in python you can use the slicing concept and chunk the data.

chunking the data will have different ways so we can use anything whichever is best for you.

Every word is token in AI world. so while querying the details, Please make sure to use the tokens efficiently.


