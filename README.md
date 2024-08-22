
# Data Analysis API

This API aims to process a certain dataset and then serves insights and analyses about the data through the endpoints.


## Installation 

Clone the project

```bash
git clone https://github.com/egebeyaztas/data_analysis_api.git
```

Go to the project location

```bash
cd data_analysis_api
```

Create a virtual environment

```bash
# Windows
python -m venv env
.\env\Scripts\activate

#MacOS / Linux
python3 -m venv env
source env/bin/activate
```

Install the requirements

```bash 
pip install -r requirements.txt
```

Create env file

```bash 
cp .env.example .env
```

Run the server

```bash 
python manage.py runserver
```

### Endpoints


```bash 
GET /api/conversion-rate/
GET /api/status-distribution/
GET /api/category-type-performance/
GET /api/filtered-aggregation/
```

Keep in mind that project and endpoints were prepared for a single dataset.

  
## App Response Examples

##### Response for /api/conversion-rate/ ######

```bash
{
    "conversion_rates": {
        "Customer A": 0.3924789162,
        "Customer B": 0.4050734868,
        "Customer C": 0.3935861047
    },
    "highest_conversion_rate": {
        "customer_id": "Customer B",
        "conversion_rate": 0.40507348683763283
    },
    "lowest_conversion_rate": {
        "customer_id": "Customer A",
        "conversion_rate": 0.3924789161501688
    }
}
```

Response for /api/filtered-aggregation/

```bash
{
    "average_conversions": {
        "Customer A": 105.1458333333,
        "Customer B": 112.1964285714,
        "Customer C": 94.6041666667
    },
    "average_revenues": {
        "Customer A": 26084.4752083333,
        "Customer B": 24771.76625,
        "Customer C": 24451.5189583333
    }
}
```
##



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

  
