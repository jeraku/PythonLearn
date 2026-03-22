# PythonLearn - Combined README

This is a comprehensive guide combining all the README files from the PythonLearn repository. It includes information on Python learning, AI concepts, database management, and various tools and techniques covered in the course.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Markdown Help](#markdown-help)
3. [AI Learning Overview](#ai-learning-overview)
4. [AI Learning Days](#ai-learning-days)
   - [Day 1-5: Basic Concepts](#day-1-5-basic-concepts)
   - [Day 6: Chain of Prompting and Vector DBs](#day-6-chain-of-prompting-and-vector-dbs)
   - [Day 7: Ollama and ChromaDB](#day-7-ollama-and-chromadb)
   - [Day 8: (Empty)](#day-8-empty)
   - [Day 9: LLM Function Calling](#day-9-llm-function-calling)
   - [Day 10: RAG - Vector DB](#day-10-rag---vector-db)
   - [Day 11: Open Search and RAG Architecture](#day-11-open-search-and-rag-architecture)
   - [Day 12: AI Agents Introduction](#day-12-ai-agents-introduction)
   - [Day 13: AI Agent Memory System](#day-13-ai-agent-memory-system)
   - [Day 14: MCP (Model Context Protocol)](#day-14-mcp-model-context-protocol)
   - [Day 15: MCP AI Agent](#day-15-mcp-ai-agent)
5. [Gen AI Workshop](#gen-ai-workshop)
6. [Database Learning](#database-learning)
   - [Database Overview](#database-overview)
   - [Day 1: Database Basics](#day-1-database-basics)
   - [Day 3: Basic CRUD SQL](#day-3-basic-crud-sql)
   - [Day 4: Alter Table Constraints](#day-4-alter-table-constraints)
   - [Day 5: Isolation and Transactions](#day-5-isolation-and-transactions)
   - [Day 6: ACID Properties](#day-6-acid-properties)
   - [Day 7: Joins](#day-7-joins)
   - [Day 8: Window Functions](#day-8-window-functions)
   - [Day 9: Advanced Window Functions](#day-9-advanced-window-functions)
   - [Day 10: Subquery and CTE](#day-10-subquery-and-cte)

---

## Project Overview

PythonLearn is a comprehensive learning repository covering Python programming, AI concepts, and database management.

<!-- pip install sqlite3 
light weight
no DB installation
10000 of record to handle.
trail purpose 100 user can use DB can go for SQLITE
Mainly this can be used for lower trail application test
-->

<!-- sublime editor -->

GPU = General personal user

---

## Markdown Help

### Headings
# Heading 1
## Heading 2
### Heading 3
#### Heading 4

**bold text**
*italic text*
***bold and italic***

- Item 1
- Item 2
  - Sub item
1. First
2. Second
3. Third

[Link text](https://example.com)

![Alt text](image_url)

`pip install numpy`

```python
print("Hello World")
```

> This is a quote or note.

| Name | Age | City |
|------|-----|------|
| Raj  | 30  | Halifax |

---

![Python](https://img.shields.io/badge/Python-3.10-blue)

# Project Title

Short description of your project.

## 🚀 Features
- Feature 1
- Feature 2

## 📦 Installation
```bash
pip install -r requirements.txt
```

---

## AI Learning Overview

### LLM Basics
LLM (Large Language Models) like Llama are neural networks that measure and respond by predicting the next word.

### How LLMs are Trained and Created

**Stage 1: Pretraining (Base Model)**
- Most costly stage
- Trains for a year
- Obtains base model

**Stage 2: Fine-tuning**
- Every week
- Label the data
- Obtains assistant model
- Cheaper than pretraining

**Stage 3: Optional - Comparison Labels**
- Fine-tuning with RLHF (Reinforcement Learning from Human Feedback)

### Model Evaluation
- Use Chatbot Arena leaderboard to compare models
- https://arena.ai/leaderboard/text

### Safety Issues

**Jailbreak Attacks**
- Acting like a polished person to extract information from AI
- Encoded values can be identified and displayed
- Image-based attacks: injecting details into images

**Prompt Injection Attacks**
- Sending blank images and asking what they say
- Hackers can link URLs in AI responses
- Modifying URLs with data exfiltration text

**Backdoor Attacks / Data Poisoning**
- Sleeper agent attacks: silently destroying AI by giving false information

### Tokenization
- Tiktokenizer: Split input and generate tokens
- Website: https://tiktokenizer.vercel.app/
- Context window: Time period for conversation

### Generative AI Applications
- Named Entity Recognition: Automatically recognize details from text
- RunPod: Rent GPUs

### LLM Training Requirements
1. Large datasets
2. Train a model (build model) - Fine tuning
3. Benchmark/Evaluate the model

### Transfer Learning

### Inference
Running the model is called inference.

### Quantization
- Reduce size and response time
- Quantized models: Reduced size (e.g., llama.cpp, gguf, ggml)

### Hardware for LLMs
- CPU/GPU (NVIDIA/AMD)/TPU (Google)/Meta (Apple software) M1, M2, M3
- PyTorch (C++)
- Jax
- mlx (Apple solution)

### LLM Inference
- Running API and getting text output
- LLM API: OPENAI
- Proprietary models: Cost involved
- Open models: Model weights (.bin/safetensors) - Self-host

### 5 Levels of LLM Apps
1. LLM OS
2. AGENTS
3. RAG (Retrieval Augmented Generation) - Real-time data, External memory, Long chats
4. Chatbot - Conversation chat, Short-term memory
5. Q&A Engine - Prompt + LLM + Answer

RAG Architecture:
- Prompt + Query + Relevant data
- Classification NLP problems: Text classification/labeling
- LLM Function Calling: Currency converter (differently formatted inputs captured and responded)

Agent: Function + Tools
- Rules + Goal = Agents

### Safety Rules
- Do not call someone more than twice
- Do not be more friendly without necessity
- Do not give knowledge without being asked
- Talk less, be secretive
- Do not let others know your next move
- Do only what you think is right
- Thank someone who improved your life

---

## AI Learning Days

### Day 1-5: Basic Concepts

#### Day 3: Prompt Engineering
- Top K: Top results
- Top P: Within probability ranges

### Day 6: Chain of Prompting and Vector DBs

**Chain of Prompting**
- Output as input for another question

**Vector DBs**

**Top-Down Approach**
- Start with big problem, break into smaller parts
- Example: Making Pizza
  - Goal: Make pizza
  - Break down: Make dough, Add sauce, Add toppings, Bake

**Bottom-Up Approach**
- Start with small pieces, combine to build solution
- Example: Making Pizza
  - Small parts: Prepare dough, Prepare sauce, Chop toppings
  - Combine: Assemble pizza → Bake → Pizza ready

### Day 7: Ollama and ChromaDB

**Ollama**: For running models
**ChromaDB**: Vector database

**Direct Search vs Semantic Search**
- Direct: "select * from employee where name = 'jegan'"
- Semantic: "select * from employee where name = 'jega*'"
- Example: Rice vs Arisi

**Distance Calculations**
- Euclidean distance: Based on Pythagorean theorem - sqrt((x2-x1)^2 + (y2-y1)^2)
- Manhattan distance: (x2-x1) + (y2-y1)
- Cosine similarity: From x0, draw line between two points = cosθ

**Embedding**
- Assign numerical values in graphical structure
- LLM model stores information like rice and arisi (pre-confirmed similarities)

**Vector DB Tools**
- OpenSearch
- MongoDB
- ChromaDB
- Pinecone
- FAISS

### Day 8: (Empty)

No content available.

### Day 9: LLM Function Calling

LLM predicts next words.

**Query + Prompt + Tools → LLM**
- function.js: Call Groq → LLM → Function (weather, calculate) → getweather function → Returns OpenAPI response
- tools.js: Tools in OpenAI format
  - Type: function
  - Name: method name
  - Parameters: type and properties
  - Response required: city (refer OpenAI docs)

**app.js**
- Available functions
- Query()
- answer = chat with tools(query)
- print(answer)

**groqinput**
- Messages: role system and user

**groq_client.js**

### Day 10: RAG - Vector DB

RAG: Retrieve data → Chunk → Augment → Output

**LLM Cut-off Date**
- Cannot answer questions about events after training data (e.g., "gold rate today")

**RAG Architecture**
- Document → Chunks → Embedding model → Vector DB
- User → Query → Context + Query → Augment → Prompt → LLM

**Tools**
- Langchain
- Groq client
- PyPDFLoader + Chunks/Split PDF
- Vector DB: FAISS DB and Nomic embed text model

### Day 11: Open Search and RAG Architecture

**References**
- https://www.youtube.com/watch?v=Qv9001gsK_E
- https://youtube.com/live/sPrTOXQf61Q

**Open Search**

**TF (Term Frequency)**
- Number of occurrences in particular page

**IDF (Inverse Term Frequency)**
- Example: Prepositions like "that", "to", "is", "at"

**TF + IDF**
- Generates score, purely rule-based

**BM25 (Best Match 25)**
- Probabilistic manner
- Text search

**Algorithms**
- KNN
- ANN

**RAG Architecture**
- ChromaDB + Persistent DB + SQLite DB + Langchain
- PCA in machine learning

**Steps**
- Load PDF
- PyPDFLoader
- Vector Search

### Day 12: AI Agents Introduction

**DAG (Directed Acyclic Graph)**
- OpenAI
- N8n

**AI Agent Components**
1. Tools (addition, getweather)
2. Memory (persistent Chroma DB) - Context window creation
3. Model - Nomic embed text
4. Groq API - OpenAI model → Brain
5. Planning module: Task planning, end goal (chain of thought, tree of thought, hierarchical tree of flow)
6. Tools: Travel itinerary planner [mode of transport, suggestions, timing, weather]
7. Learning and reflection: HIL (Human in the Loop)
8. Foundation model: Brain (LLM) - OpenAI model

**Latency and Cost**
- Better performance with optimized components

**DAG Architecture**
- One-way: A→D, no D→A

**Agent vs Tool Calling**
- Tool calling: Get weather, return only weather info
- AI Agent: Gives extra information

**n8n Components**
- Chat model
- Memory
- Tool output
- Parser

**Tools.py**
- Addition and getweather

**Memory.py**
- Persistent Chroma DB

**Groq Client.py**
- OpenAI model, brain

**Agent.py**
- Memory, tools → Get user input

**Simple Reflex Agent**

**To Run**
- python main.py

### Day 13: AI Agent Memory System

#### Simple Explanation

**How AI Agent Works**
User → App → Rules → LLM → Agent → Final Answer

**Example**
- User: "Give me a travel plan for Chennai"
- Agent looks at recent messages, long-term preferences, thinks using LLM, gives travel plan

#### Memory System

**Two Types of Memory**

1. **Short-Term Memory (Redis)**
   - Memory for current chat session only
   - How it works:
     1. Send message
     2. System loads previous messages from Redis
     3. Adds new message
     4. Sends everything to LLM
     5. Saves updated conversation back to Redis
   - Example: For question 5, AI uses summary of message 3, 4, and new question
   - LLM gets: [summary, message3, message4]
   - Deleted when session expires

2. **Long-Term Memory (Vector DB)**
   - Stays forever (until deleted)
   - Used for personalization
   - Stores: Preferences, important details, summaries of past chats
   - How it works:
     1. Message converted to numbers (embedding)
     2. Saved in vector database
     3. Later, searches database
     4. Finds related information
     5. Adds to LLM prompt
   - Example: User prefers vegetarian food → Later asks for Chennai trip → System adds vegetarian preference to prompt → LLM plans vegetarian-friendly trip

**Full Flow**
User Message → Short-Term Memory (Redis) → Long-Term Memory (Vector DB) → LLM thinks → Final Answer

**Summary**
- Short-term: Remembers current conversation
- Long-term: Remembers you

### Day 14: MCP (Model Context Protocol)

**MCP**: Agentic AI, Building AI Agents with goal-based agents
- Video uploading
- Document from video
- Timestamp
- Create and publish blog for video
- Update in Telegram

**LLM**
- MCP: Model Context Protocol (Anthropic)
- MCP gives schema
- LLM takes input and calls tool
- { "method": "list Tools []" }

**Public MCPs**
- Set of rules/protocol to consume same methods across AI

**Travily**
- AI Agents connect to internet

**SSE (Server-Sent Events)**
- Event stream API for conversation
- Standard input/output to speak with agents

**Anthropic/FastAPI MCP Agents**
- Using these to create MCP agents
- FastMCP

**Agent Integration**
- Link LLM → Call MCP

### Day 15: MCP AI Agent

MCP
AI Agent
LLM → MCP Client → MCP Server [Tools → Defined Schema]

---

## Gen AI Workshop

**GrowthSchool - Talk to AI - Prompting**
- Mastering prompt engineering
- Magic prompt formula: Role → TASK → Instruction

**Multi Tool for AI**
- Compares across different models in single place
- https://getmulti.ai/

**AI Tools**
- Grok: Tweets list and response
- Gemini
- Perplexity Pro
- ChatGPT

**AI for Productivity**
- Excel: Numerous.ai

**Dashboard & Code**
- Claude: "You are an expert data scientist, find hidden insights and convert to beautiful dashboard and share"

**Presentation**
- Copy prompt, use Gemini, use Canvas prompt: "You are an expert with details"

**AI for Learning**
- Emily AI: Assistant, record content in blog page, share summary
- Raj Shamani
- Emily Chrome plugin: Summarize video

**Learn How to Learn Faster**

**NotebookLM**
- Copy URL of article, go with topic
- Creates image/Audio/PPT

**Phot.ai**
- Creates product ad

**Generating Website from UI**
- Rollout

**Tokenization**
- Attention
- Context
- OpenAI Playground

**Image Generation**
- Aesthetic prompting

**Tools**
1. Gemini - Google AI Studio → Nano banana image generation (try nano banana)
   - Jio SIM → Gemini Pro free
2. ChatGPT Go → Only in India

---

## Database Learning

### Database Overview

**Postgres Setup**
- https://courses.parottasalna.com/database-engineering/installing-postgresql

**How to Run and Connect**

1. Start containers:
   ```bash
   docker compose up -d
   ```

2. Open browser at http://localhost:8080 and log in with:
   - Email: admin@pgadmin.com
   - Password: password

3. In pgAdmin, add new server:
   - Name: anything (e.g., Local Postgres)
   - Host: postgres (service name, not localhost)
   - Port: 5432
   - Username: admin
   - Password: password
   - Database: my_database (or leave blank for default)

4. Login from command line:
   ```bash
   docker exec -it postgres_db psql -U admin -d my_database
   ```
   Password: password

5. Copy DVD rental data:
   ```bash
   docker cp dvdrental.tar 86243781d2cb:/home/dvdrental.tar
   ```

6. Restore data:
   ```bash
   docker exec -it 86243781d2cb bash  # (assuming container ID is postgres_db)
   pg_restore -U admin -d my_database /home/dvdrental.tar
   ```

**Commands**
- `\du` - List users
- `CREATE ROLE sb_developer;`
- `CREATE ROLE jeganlogin WITH LOGIN PASSWORD 'test123';`
- `GRANT sb_developer TO jeganlogin;`
- `GRANT SELECT ON <TableName> TO db_developer;`

**Schema**
- Folder-like structure
- `CREATE ROLE analytics_team;`
- `GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO analytics_team;`
- `ALTER ROLE sb_developer WITH SUPERUSER;`
- `GRANT analytics_team TO jegan_user;`
- `REVOKE analytics_team FROM jegan_user;`

**DB Level Privileges**
- Login details
- Logged in user
- RBAC: Role-Based Access Control

**Table Privileges**
- select, insert, update, delete, trigger, truncate

**Connection Commands**
- `\c dbname` - Connect to database
- `\l` - List databases
- `select current_database();` - Show current DB
- `\dt` - List relations
- `\d <table name>` - Display table permissions

**Checkpoint**
- `CHECKPOINT;`
- `show WAL_;`
- `show WAL_Buffers;`
- `COMMIT` - Record stores in WAL, later writes to disk by checkpointer
- `SHOW synchronous_commit;`
- `SET synchronous_commit = 'off';`

**ACID Properties**

| Property    | Meaning                                       | Example                                             |
| ----------- | --------------------------------------------- | --------------------------------------------------- |
| Atomicity   | All-or-nothing transaction                    | Money transfer succeeds completely or not at all    |
| Consistency | Maintains database rules                      | Account balance cannot be negative                  |
| Isolation   | Transactions do not interfere with each other | Two users updating same account see correct results |
| Durability  | Changes persist after commit                  | Deposit remains even after a crash                  |

### Day 1: Database Basics

**DB Characteristics**
- Rigid structure
- Schema: Blueprint

**Storage**
- Program: Variables in RAM
- Disk: I/O operations required - slower
- Persistent storage: Stores on disk, survives restart
- Non-persistent: Redis (cache) in RAM, faster, survives restart: False (not qualified for primary DB)
- Redis in persistent mode allowed

**Database Types**
- Graph (Neo4J): Maps, statistical data, Vector DB, RAG arch, forms graph between nodes
- Obsidian DB
- Time series: Influx DB (logs, stock analysis) → Grafana

**Postgres**
- DB engine, pool of processes
- Client → Postmaster → Backend process pool

**Resources**
- Postgres YouTube: https://www.youtube.com/live/lo8VWgXUB08
- DVD Rental DB: https://courses.parottasalna.com/database-engineering/sample-databases/dvd-rental-database
- Miro for DB schema: https://miro.com/app/board/uXjVLD2T5os=/

### Day 3: Basic CRUD SQL

**Primary Key**
- Unique and not null
- JSONB: Decompiled binary format
- If failure during insert, primary key still increments

**Queries**

```sql
CREATE DATABASE userdb;
\c userdb;

CREATE TABLE users(
    id bigserial primary key,
    name varchar(100) not null,
    email varchar(100) unique not null,
    age smallint check (age >=18),
    salary numeric(10,2),
    is_active boolean default true,
    role varchar(20) check (role in ('admin','user','manager')),
    created_at timestamptz default now()
);

INSERT INTO users (name, email, age, salary, role) VALUES ('jegan', 'a@a.com', 30, 'test', 100);
INSERT INTO users (name, email, age, role, salary) VALUES ('jegan3', 'a@a3.com', 30, 'manager', 100);

INSERT INTO users (name, email, age, role, salary) VALUES 
    ('jegan5', 'a@a5.com', 30, 'manager', 100),
    ('jegan6', 'a@a6.com', 30, 'manager', 100),
    ('jegan7', 'a@a7.com', 30, 'manager', 100) 
RETURNING id;

INSERT INTO users (name, email, age, role, salary) VALUES ('jegan11', 'a@a11.com', 30, 'manager', 100) RETURNING id;

UPDATE users SET salary = salary + 500 WHERE id = 3;
UPDATE users SET salary = salary + 500 WHERE id = 6 RETURNING id;
UPDATE users SET is_active = false WHERE created_at < now() - interval '10 minute';

DELETE FROM users WHERE id = 1;

-- Schema validation
\d users;

TRUNCATE TABLE users;

ALTER TABLE users ADD COLUMN phone_no int;
```

### Day 4: Alter Table Constraints

```sql
CREATE TABLE users (
    user_id serial primary key,
    username varchar(100) not null,
    email varchar(100) not null,
    password text not null,
    created_at timestamp
);

INSERT INTO users (username, email, password) VALUES ('jegan', 'j@j.com', 'password');

ALTER TABLE users ADD COLUMN phone varchar(15);
ALTER TABLE users ADD COLUMN is_active BOOLEAN NOT NULL;
ALTER TABLE users ADD COLUMN age INT CHECK(age >= 18);
ALTER TABLE users ADD CONSTRAINT uniq_email_id UNIQUE(email);
```

### Day 5: Isolation and Transactions

**Isolation**
- Transactions: BEGIN ... COMMIT/ROLLBACK

**Example**
```sql
BEGIN
SELECT * FROM film LIMIT 10;
SELECT title FROM film LIMIT 10;
UPDATE film SET title = 'Changed Title' WHERE title = 'African Egg';
SELECT * FROM film LIMIT 10;
COMMIT;

UPDATE film SET title = 'Changed Title' WHERE title LIKE 'Changed%';
ROLLBACK;
```

**Atomicity**
- Either all success or all failure
- Example: Jegan = 100, BEGIN, Jegan = 100 + 5, Issue, then Jegan = 100

**Transaction Problems**
1. **Dirty Read**: Data read from temporary fields
2. **Non-repeatable Reads**: Like update query, multiple transactions same time
3. **Phantom Reads**: Like insert query, new data inserted during transaction

**Isolation Levels**
- `BEGIN ISOLATION LEVEL REPEATABLE READ`
- `BEGIN ISOLATION LEVEL SERIALIZABLE`

### Day 6: ACID Properties

**Atomicity**
- Either all success or all fail
- Example: Jegan = 100, BEGIN, Jegan = 100 + 5, Issue → Jegan = 100
- Two transactions started same time, different entries changed → All fail or all success
- Mainly COMMIT/ROLLBACK

**WAL (Write-Ahead Logging)**
- Temporary storage for changed data
- On COMMIT, data stored in buffer, then WAL, then after crash retrieves and stores in DB

**Example**
```sql
BEGIN
SELECT * FROM accounts
UPDATE accounts SET balance = 'abcd'  -- Error as balance is numeric
COMMIT  -- Will fail
```

**Isolation**
```sql
BEGIN
SELECT * FROM accounts
UPDATE accounts SET balance = 101 WHERE id = 3;
SAVEPOINT SP1;
UPDATE accounts SET balance = 'abcd';  -- Error
ROLLBACK TO SP1;  -- Success marker
COMMIT;
```

**Durability**
- Problems: Crashes, reboot, power outage
- Solutions: WAL, checkpointing, fsync, synchronous commit

**Commands**
- `SHOW wal_;`
- `SHOW wal_buffers;`
- `COMMIT` - Record in WAL, then disk by checkpointer; or direct to disk
- `SHOW synchronous_commit;`
- `SET synchronous_commit = 'off';`

**Backups**

### Day 7: Joins

**Setup**
```sql
CREATE TABLE employee (
    emp_id serial primary key, 
    emp_name varchar(100), 
    dept_id integer, 
    salary integer
);

INSERT INTO employee (emp_name, dept_id, salary) VALUES 
    ('jegan', 1, 100), 
    ('jegan1', 1, 101),
    ('jegan2', 1, 102);

INSERT INTO employee (emp_name, dept_id, salary) VALUES 
    ('Raj', 2, 100), 
    ('Raj1', 2, 101), 
    ('Raj3', 2, 103);

INSERT INTO employee (emp_name, dept_id, salary) VALUES 
    ('Raj', 2, 103), 
    ('Rajk1', 3, 1031), 
    ('Rajk3', 3, 1033);

UPDATE employee SET dept_id = 3 WHERE emp_name='Raj' AND emp_id = 5;

CREATE TABLE department (
    dept_id serial primary key, 
    dept_name varchar(100) not null
);

INSERT INTO department (dept_name) VALUES ('hr'), ('cse');

ALTER TABLE employees ADD COLUMN dept_id INTEGER NOT NULL;
ALTER TABLE employees ALTER COLUMN dept_id TYPE INTEGER;
```

**Join Examples**
```sql
-- Cross join
SELECT e.emp_name, e.dept_id, e.salary, d.dept_name 
FROM employee AS e, department AS d 
WHERE e.dept_id = d.dept_id;

-- Inner join
SELECT e.emp_name, e.dept_id, e.salary, d.dept_name 
FROM employee AS e 
INNER JOIN department AS d ON e.dept_id = d.dept_id;

-- Right join
SELECT e.emp_name, e.dept_id, e.salary, d.dept_name 
FROM employee AS e 
RIGHT JOIN department AS d ON e.dept_id = d.dept_id;

-- Left join
SELECT e.emp_name, e.dept_id, e.salary, d.dept_name 
FROM employee e 
LEFT JOIN department d ON e.dept_id = d.dept_id;

-- Full outer join
SELECT e.emp_name, e.dept_id, e.salary, d.dept_name 
FROM employee e 
FULL OUTER JOIN department d ON e.dept_id = d.dept_id;
```

**WAL Settings**
- `SHOW wal_tab;`
- `SHOW wal_synchronous_commit;` - If ON, COMMIT writes to wal_buffer then WAL_disk
- For performance: Increase WAL size or set sync commit off (not write to disk)

**WAL Buffers**
- `SHOW wal_buffers;`

### Day 8: Window Functions

**Window Functions: Ranking and Aggregation**

**Components**
1. Partition by
2. Order by
3. Rows

**Ranking Functions**
- ROW_NUMBER() [ORDER BY, GROUP BY]
- ROW, RANK, DENSE_RANK, NTILE

**Aggregation Functions**
- SUM, AVG, MIN, MAX, COUNT

**Value Functions**
- (Covered in Day 9)

**Distribution Functions**
- (Covered in Day 9)

**Ranking Examples**
```sql
SELECT emp_id, emp_name, dept_id, salary, 
    ROW_NUMBER() OVER (ORDER BY salary DESC) 
FROM employee;

SELECT emp_id, emp_name, dept_id, salary, 
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) 
FROM employee;

-- RANK: 1,1,2,3
SELECT emp_id, emp_name, dept_id, salary, 
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) 
FROM employee;

-- DENSE_RANK: 1,1,3,4
SELECT emp_id, emp_name, dept_id, salary, 
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) 
FROM employee;

-- NTILE: Splits into groups
SELECT emp_id, emp_name, dept_id, salary, 
    NTILE(4) OVER (ORDER BY salary DESC) AS QUARTILE 
FROM employee;

SELECT emp_id, emp_name, dept_id, salary, 
    NTILE(100) OVER (ORDER BY salary DESC) AS QUARTILE 
FROM employee;
```

**Aggregation Examples**
```sql
SELECT emp_id, emp_name, dept_id, salary, 
    SUM(salary) OVER (PARTITION BY dept_id) AS total_sum 
FROM employee;

-- Running total
SELECT account_id, amount, 
    SUM(amount) OVER (PARTITION BY account_id ORDER BY txn_date) 
FROM transactions;
```

### Day 9: Advanced Window Functions

**Window Functions**
- Ranking: ROW_NUMBER, NTILE, RANK, DENSE_RANK
- Aggregation: SUM, MAX, MIN, AVG, COUNT

**Today's Topics**
- Value Functions
- Distribution Functions
- ROWS

**Value Functions**
- LAG
- LEAD
- FIRST_VALUE
- LAST_VALUE

**LAG**
- Compare previous row and current row

```sql
SELECT * FROM monthly_sales;

SELECT region, month, sales_amount, 
    LAG(sales_amount) OVER (PARTITION BY region ORDER BY month) AS last_month_sales 
FROM monthly_sales;

-- Output example:
-- region | month | sales_amount | last_month_sales
-- North  | Jan   | 1000         | NULL
-- North  | Feb   | 1200         | 1000
-- North  | Mar   | 900          | 1200
-- South  | Jan   | 800          | NULL
-- South  | Feb   | 950          | 800

-- LAG with offset 2
SELECT region, month, sales_amount, 
    LAG(sales_amount, 2) OVER (PARTITION BY region ORDER BY month) AS last_month_sales 
FROM monthly_sales;

-- Output:
-- North | Jan | 1000 | NULL
-- North | Feb | 1200 | NULL
-- North | Mar | 900  | 1000
-- South | Jan | 800  | NULL
-- South | Feb | 950  | 800

-- LAG with default value
SELECT region, month, sales_amount, 
    LAG(sales_amount, 2, 0) OVER (PARTITION BY region ORDER BY month) AS last_month_sales 
FROM monthly_sales;
```

### Day 10: Subquery and CTE

**Topic: Subquery and CTE (Common Table Expression)**

**Subquery**: Inner query

**Tables**: Dept, Employee, Project, Users

**Example**
```sql
SELECT emp_name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```</content>
<parameter name="filePath">c:\jegan\automation\github_J\PythonLearn\Combined_README.md