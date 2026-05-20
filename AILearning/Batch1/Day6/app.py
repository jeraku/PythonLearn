from groq_client import call_groq

# Step 1 - Extract Topics
def extract_topics(content):
    prompt = f"""
    You are a content analyzer. 

    From the below text, extract:
        1. main concepts
        2. important keywords
        3. possible user intents
        4. flow of content
    
    Return ONLY JSON:

    {content}
    """

    return call_groq(prompt)

# Step 2 - Generate Questions
def generate_questions(content):
    prompt = f"""
    Using the below topics generate: 
        1. 1 Beginer questions
        2. 2 Intermediate questions
        3. 3 Advanced Questions

    Return as JSON array, for each element add a difficulty/level tag.

    {content}
    """

    return call_groq(prompt)

# Step 3 - Generate answers
def generate_answers(content):
    prompt = f"""
        For each question generate: 

        - short answer
        - long answer

        maintain the words understandable to a layman.

        {content}
    """
    return call_groq(prompt)

# Step 4 - Format
def format_faqs(content, audience):
    prompt = f"""
        The FAQ's:
            {content}.

        Format the above FAQ's for audience: {audience}

        Rules:
            -   Friendly tone
            -   add examples
            - maintian layman
            - use lsss jargons
        
        output as :
        question:
        short:
        Long:
        
    """
    return call_groq(prompt)

def faq_generator(content, audience='student'):
    
    step_1 = extract_topics(content)
    step_2 = generate_questions(step_1)
    step_3 = generate_answers(step_2)
    step_4 = format_faqs(step_3, audience)

    return step_4

if __name__ == "__main__":
    content = """
    Its an Application level caching, where the application checks whether the data is present in the cache (In our case redis). If data is present it returns the data. Else checks from the database and stores it in Cache and then returns the data to client.
Steps:

    The Application (Fast API), checks whether the requested data is present in the cache (redis).
    If the data present in the cache (redis) it gets the data and returns the value.
    If the data is not present in the cache (cache miss), it will check the details from the primary database (mongodb).
    If the data is available it returns the data to the application.
    The application now sets the data to Cache for future hits (cache hit).

    Cache Hit: If the requested data is present in the cache.

    Cache Miss: If the requested data is not present in the cache.


"""
    response = faq_generator(content)
    print(response)
