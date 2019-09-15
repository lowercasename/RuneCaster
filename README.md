
# RuneCaster

RuneCaster is a command line utility, written in Python, to generate truly random Elder Futhark rune casts. It uses the RANDOM.ORG API.

## Setup

1. Install the necessary Python modules using `pip`:
   `pip install requests halo jsonrpcclient`
2. Set up a free RANDOM.ORG API key by heading here: https://accounts.random.org/. Click the 'Use this Service' button in the 'API Services' section, create a new API key, and copy the API Key (not the Hashed API Key) to your clipboard.

## Installation and use

1. Clone this repository somewhere on your computer:
   `git clone https://github.com/lowercasename/RuneCaster.git`
2. Open the directory:
   `cd runecaster`
3. Open up the `runecaster.py` file in your favourite text editor and edit the 'API key here' line so it looks like this:
   ```
   APIKey = 'abcdabcd-abcd-abcd-abcd-abcdabcdabcd' # Paste your RANDOM.ORG API key here
   ```
   Save and close the file.
3. Run RuneCaster:
   `python runecaster.py`

