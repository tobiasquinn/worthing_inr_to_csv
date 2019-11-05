# worthing_inr_to_csv
Takes a set of emails in eml format from Worthing Hospital Anticoagulant Clinic Warafarin INR Result Service and outputs as csv file

## Usage

Stick eml emails in ./eml directory (tested with emails from mozilla thunderbird)

python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python eml_to_inr.py > inr.csv
