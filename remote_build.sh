python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
export LOGLEVEL=default
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
cp vercel.json public/
deactivate