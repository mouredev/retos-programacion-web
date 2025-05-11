source .venv/bin/activate
rm -rf public
pip install --upgrade pip
pip install -r requirements.txt
export LOGLEVEL=default
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
cp vercel.json public/
deactivate