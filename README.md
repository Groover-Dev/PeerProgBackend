# PeerProgBackend

## Getting Started
First, start by cloning this project  
Then, in the PeerProgBackend directory run the following commands:

- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- ./manage.py migrate
- ./manage.py runserver 0.0.0.0:8000

Then navigate to http://0.0.0.0:8000/api/schema/swagger-ui/

## First Part

Create 2 new models: `Release` and `Track`

#### Release
Relase model should have the following attributes:
 - name
 - release_date
 - created_at

With the following constraints:
 - A release must always be linked to a user
 - A release can be distributed on several DSP
 - A release have several tracks

#### Track
Track model should have the following attributes:
 - name
 - created_at

With the following constraints:
 - A track can appear on different releases


### API
Create a CRUD API for the freshly created Release and Track models.
Release output should display all its dsp name and all its tracks
Track output should display all the releases on which it appears.


## Second Part
Add filtering and ordering features on the Release API (by name dsp and by date)

## Third Part
- Setup pagination
- Setup permissoins
