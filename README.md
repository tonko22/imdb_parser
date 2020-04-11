# imdb_parser
Series ID parsing microservice


# Deploy locally:

1. Activate python env: 
    source imbd_env_3.7/bin/activate # 
2. Intsall requirements: 
    pip install -r requirements.txt
3. Run fastapi server: 
    uvicorn server:app --port [bind_port]
4. Run local test:
    python test_request.py
5. Stop server (while connected to process):
    CTRL+C
