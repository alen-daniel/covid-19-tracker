# covid-19-tracker
A covid-19 dashboard to visualize the state of covid-19 data in Canada's provinces and health regions.

References: 

Data source: https://opencovid.ca/api/

Visualization inspiration: https://covid19tracker.ca/province.html

### Running the app locally

Clone the git repo, then install the requirements with pip. Note some of the dash dependencies have issues with more recent versions. This app was tested using python 3.7.12.

```
git clone https://github.com/alen-daniel/covid-19-tracker
cd covid-19-tracker
pip install -r requirements.txt
```

Launch the python back-end

```
python app.py
```

Access the Dash front-end by opening a web browser and entering the url localhost:8050