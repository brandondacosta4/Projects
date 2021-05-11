from flask import Flask 
from flask_restful import Api, Resource

dict = {
    "Canada": "canada",
    "Alberta": "AB",
    "British Columbia": "BC",
    "Manitoba": "MB",
    "New Brunswick": "NB",
    "Newfoundland and Labrador": "NL",
    "Northwest Territories": "NT",
    "Nova Scotia": "NS",
    "Nunavut": "NU",
    "Ontario": "ON",
    "Prince Edward Island": "PE",
    "Quebec": "QC",
    "Saskatchewan": "SK",
    "Yukon": "YT",
    "Calgary": 4832,
    "Central Alberta": 4833,
    "Edmonton": 4834,
    "Northern Alberta": 4835,
    "Southern Alberta": 4831,
    "Fraser": 591,
    "Interior British Columbia": 592,
    "Northern British Columbia": 594,
    "Coast of Vancouver": 595,
    "Interlake Eastern": 4603,
    "Northern Manitoba": 4604,
    "Prairie Mountain": 4602,
    "Southern Health": 4605,
    "Winnipeg": 4601,
    "Moncton Area": 1301,
    "Saint John Area": 1302,
    "Fredericton": 1303,
    "Edmundston": 1304,
    "Campbellton": 1305,
    "Bathurst": 1306,
    "Miramichi": 1307,
    "Central Newfoundland and Labrador": 1012,
    "Eastern Newfoundland and Labrador": 1011,
    "Labrador Grenfell": 1014,
    "Western Newfoundland and Labrador": 1013,
    "Western Nova Scotia": 1201,
    "Eastern Nova Scotia": 1203,
    "Northern Nova Scotia": 1202,
    "Central Nova Scotia": 1204,
    "Algoma": 3526,
    "Brant": 3527,
    "Chatham Kent": 3540,
    "Durham": 3530,
    "Eastern Ontario": 3558,
    "Grey Bruce": 3533,
    "Haldimand Norfolk": 3534,
    "Haliburton Kawartha Pineridge": 3535,
    "Halton": 3536,
    "Hamilton": 3537,
    "Hastings Prince Edward": 3538,
    "Huron Perth": 3539,
    "Kingston Frontenac Lennox & Addington": 3541,
    "Lambton": 3542,
    "Leeds Grenville and Lanark": 3543,
    "Middlesex London": 3544,
    "Niagara": 3546,
    "North Bay Parry Sound": 3547,
    "Northwestern": 3549,
    "Ottawa": 3551,
    "Peel": 3553,
    "Peterborough": 3555,
    "Porcupine": 3556,
    "Renfrew": 3557,
    "Simcoe Muskoka": 3560,
    "Southwestern": 3575,
    "Sudbury": 3561,
    "Thunder Bay": 3562,
    "Timiskaming": 3563,
    "Toronto": 3595,
    "Waterloo": 3565,
    "Wellington Dufferin Guelph": 3566,
    "Windsor Essex": 3568,
    "York": 3570,
    "Abitibi Temiscamingue": 2408,
    "Bas Saint Laurent": 2401,
    "Capitale Nationale": 2403,
    "Chaudiere Appalaches": 2412,
    "Cote Nord": 2409,
    "Estrie": 2405,
    "Gaspesie Iles de la Madeleine": 2411,
    "Lanaudiere": 2414,
    "Laurentides": 2415,
    "Laval": 2413,
    "Mauricie": 2404,
    "Monteregie": 2416,
    "Montreal": 2406,
    "Nord du Quebec": 2410,
    "Nunavik": 2417,
    "Outaouais": 2407,
    "Saguenay": 2402,
    "Terres Cries de la Baie James": 2418,
    "Central Saskatchewan": 473,
    "Far Northern Saskatchewan": 471,
    "Northern Saskatchewan": 472,
    "Regina": 475,
    "Saskatoon": 474,
    "Southern Saskatchewan": 476
}  
app = Flask(__name__)
api = Api(app) 

covid_def_msg  = "According to the World Health Organization, the Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus."
symptoms_msg = "According the the Government of Canada, Serious symptoms of Covid-19 include difficulty breathing or shortness of breath, chest pain or pressure, and loss of speech or movement. If you are experiencing please contact your local public health authority and isolate yourself at home for 14 days"
vaccines_msg = "According to the government of Canada, the Pfizer, Moderna, AstraZeneca and Janssen vaccines have been authorized in Canada"

class master(Resource):
    def get(self):
        return({"cities": dict})
api.add_resource(master, "/master")

class covid_definition(Resource):
    def get(self):
        return({"message": covid_def_msg})
api.add_resource(covid_definition, "/covid-definition")

class symptoms(Resource):
    def get(self): 
        return({"message" : symptoms_msg})
api.add_resource(symptoms, "/symptoms")


class vaccines(Resource):
    def get(self):
        return({"message": vaccines_msg})
api.add_resource(vaccines, "/vaccines")

if __name__ == "__main__":
    app.run(debug=True)
