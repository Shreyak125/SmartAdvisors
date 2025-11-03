from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug True for  development
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# Running the python script on a virtual enviormnet backend
# python3 -m venv venv (not required if you already have a venv)
# source venv/bin/activate
# (not necessary if already installed) pip install flask flask-cors flask_sqlalchemy python-dotenv pdfplumber psycopg2-binary
# python run.py
# deactivate
