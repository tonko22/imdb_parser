# imdb_parser
Series ID parsing microservice


# Deploy locally:

1. Intsall requirements (Python 3.7, may also work on other versions): 
    pip install -r requirements.txt
2. Run fastapi server: 
    uvicorn server:app --port [bind_port]
3. Run local test:
    python test_request.py
4. Stop server (while connected to process):
    CTRL+C
