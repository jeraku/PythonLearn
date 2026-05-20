# 🧠 AI Agent — Simple Explanation

This document explains how the AI Agent works in very simple words, with easy examples.

---

## 🚀 How the AI Agent Works (Simple View)

User → App → Rules → LLM → Agent → Final Answer

You ask something →  
The app collects your info →  
Some rules run →  
LLM thinks →  
Agent gives the answer.

---

## 🧳 Example  
**User:** “Give me a travel plan for Chennai.”

The agent will:
- Look at your recent messages  
- Look at your long-term preferences (if stored)  
- Think using the LLM  
- Give a travel plan  

---

# 🧠 Memory System (Very Simple)

The AI uses **two types of memory**:

1. **Short-Term Memory** → like your brain remembering the last 5 minutes  
2. **Long-Term Memory** → like saving notes in a notebook  

---

## 1. Short-Term Memory (Redis)

This is memory for **the current chat session only**.

### How it works:
1. You send a message
2. System loads your previous messages from Redis  
3. Adds your new message  
4. Sends everything to the LLM  
5. Saves the updated conversation back to Redis  

### Example:
You ask 5 questions.

For question **5**, the AI might use:
- Summary of message 3  
- Summary of message 4  
- Your new question  

So the LLM gets:  
`[summary, message3, message4]` → and gives the answer.

Short-term memory is deleted when the session expires.

---

## 2. Long-Term Memory (Vector DB)

This is memory that stays **forever** (until deleted).  
Used for personalization.

### What gets stored?
- Your preferences  
- Important details  
- Summary's of your past chats  

### How it works (simple):
1. Your message is converted into numbers (embedding)  
2. Saved in the vector database  
3. Later, when needed, the system searches this database  
4. Finds related information  
5. Adds it to the LLM prompt  

### Example:
If earlier you said:
> “I prefer vegetarian food.”

Later you ask:
> “Plan my Chennai trip.”

The system will:
- Search long-term memory  
- Find your food preference  
- Add it to the prompt  
- LLM will plan a **vegetarian-friendly** trip  

---

# 🔄 Full Flow (Simple)

User Message
↓
Short-Term Memory (Redis)
↓
Long-Term Memory (Vector DB)
↓
LLM thinks
↓
Final Answer

Short-term = recent chat  
Long-term = saved knowledge  

---

# 🎯 Summary (In One Line)

**Short-term memory helps the AI remember your current conversation.  
Long-term memory helps the AI remember you.**

