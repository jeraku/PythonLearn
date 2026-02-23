LLM -> predicts next words

Query + Prompt + tools -> LLM 
function.js -> Call Groq- > LLM - function (weather, Calculate) ->  getweather function -> returns the repsonse of open api 
tools.js -> tools -> Open AI format -> type function -> name (method name) -> parameter (type and properties) -> response is required(city) > Refer open AI documentation

app.js -> available function -> 
Query()
answer= chat with tools(query)
print(answer)


groqinput -> message (role: system and user)

groq_client.js -> 