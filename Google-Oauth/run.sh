export FN_AUTH_REDIRECT_URI=http://localhost:8040/google/auth
export FN_BASE_URI=http://localhost:8040/user
export FLASK_APP=app.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET

python -m flask run -p 8040