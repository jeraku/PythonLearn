Hallucination

knowledge groundness - ground truth
amswer from doc, then fine. if not then problem.

Embedding
Lettuce Dedduction -> Model - to find difference on the hallucination or not.
call another LLM and provide feedback. - LLM as Judge

EvalFramework -> Ragas -> to find the response whether that is a hallucination or not.

Faithfullness > Results are blocked by the context.
Answer relevancy > context and answer are same - whether hthe answer is relavant to the question.
Context precision > how many docs are useful - Retrieved documents > how many are useful.
Context Recall > Does all necessary doc been retrieved
answer correctness.  > ground truth > Unit testing
Answer similarity> Expected anser semantic similarity > Unit Testing.

CI/CD pippeline > UNIT TEST -> to validate how its works
Deepeval and Ragas are used to measure the response LLM

