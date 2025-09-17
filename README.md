Recommendation System API

🚀 High-performance FastAPI backend with personalized recommendations and Redis caching (50% DB load reduction, 30% infrastructure cost savings).

🔐 JWT Authentication – secure user registration & login

📊 Activity Tracking – logs user actions

📈 Personalized Recommendations – based on user activity

⚡ Redis Caching – reduces DB queries by 50%, saves ~30% infra cost, with TTL & dirty-flag invalidation

🚀 Fully Async FastAPI – scalable backend for high concurrency

🧾 Swagger Docs – interactive API testing at /docs

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1f629c9e-ec33-431a-962b-086036d7c65c" />

Can be scaled up easily by adding most frequent and recommended products with cache refreshing every 2–3 minutes.

🧰 Tech Stack

Python 3.11 | FastAPI | PostgreSQL (async SQLAlchemy) | Redis (async caching) | JWT Auth | dotenv

🗂️ Project Structure
.
.
├── app/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── cache/
│   ├── seed.py
│   └── migrate.py
├── requirements.txt
└── README.md

⚙️ Setup & Run Locally
git clone https://github.com/Ashutosh0000000/Recommendation-System-API.git
cd Recommendation-System-API

python3.11 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python migrate.py
python seed.py
uvicorn app.main:app --reload

📊 Sample API Request

POST /api/activity/

curl -X POST http://localhost:8000/api/activity/ \
 -H "Authorization: Bearer <your_token>" \
 -H "Content-Type: application/json" \
 -d '{"item_id": 4, "action": "purchased"}'


🧊 Redis Cache Impact

Cache hits reduce DB queries by 50%+
Monitor Redis metrics: keyspace_hits, keyspace_misses, used_memory_human
Use RedisInsight or CLI (redis-cli info stats) for live cache stats

💰 Cost Efficiency with Redis Caching
Offloads frequent reads to Redis, reducing DB load by over 50%
Saves server CPU and I/O costs by reducing pressure on database
Smart cache invalidation ensures freshness without expensive full rebuilds


📸 Screenshots

Redis cache stats(hits and miss cache)
[![Redis Cache Stats](assets/redis_cache_stats.png)](https://github.com/Ashutosh0000000/Recommendation-System-API)

Recommended items 
[![Stats Recommended Items](assets/stats-recommened-items.png)](https://github.com/Ashutosh0000000/Recommendation-System-API)

Authorization bearer token(registering and login with email and password for a new user)
[![Swagger Auth Popup](assets/swagger_auth_popup.png)](http://localhost:8000/docs)

Users create activity(by entering item id and action)
[![Swagger Create Activity](assets/swagger_create-activity.png)](http://localhost:8000/docs)

Succesfull activity created 
[![Swagger Post Activity](assets/swagger_post_activity.png)](http://localhost:8000/docs)


🔗 API Documentation
Open http://localhost:8000/docs
 open in your browser to explore and test the API using Swagger UI.
API using Swagger UI.

