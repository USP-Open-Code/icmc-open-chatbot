import uvicorn
import os

from src.main import create_app


if __name__ == "__main__":
    app = create_app()
    PORT = os.getenv("API_PORT", 9876)

    uvicorn.run(app, host="0.0.0.0", port=int(PORT))
