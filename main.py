import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    from waitress import serve
    port = int(os.environ.get('PORT', 5000))  # pega a porta do ambiente, ou usa 8080 como fallback local
    print(f"Starting server on port {port}...")
    serve(app, host="0.0.0.0", port=port)
