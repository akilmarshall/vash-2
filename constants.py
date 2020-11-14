from datetime import datetime

PROGRAM_NAME = 'VASH Report Helper'
DAYS = list(range(1, 31))
CURRENT_DAY = datetime.now().day
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
CURRENT_MONTH = MONTHS[datetime.now().month - 1]
YEAR = datetime.now().year
YEARS = list(range(2019, YEAR + 1))
INCIDENT_TYPES = ['Physical Assault', 'Sexual Assault', 'Automobile Accident', 'Automobile Theft', 'Burglary', 'Court Case', 'Death', 'Disorderly Conduct', 'Evacuation',
                  'Lodging Scam', 'Lost', 'Lost Items', 'Medical Emergency', 'property Damage', 'Robbery', 'Terroristic Threatening', 'Theft', 'Unauthorized Entry into Motor Vehicle']
COD = ['Automobile Accident', 'Homicide', 'Suicide',
       'Natural Cause/Illness', 'Water Related', 'Other']
MMA = [
    'U.S. Pacific and Mountain (AK, CA, OR, WA, AZ, CO, ID, MT, NV, UT, WY)', 'U.S. East (other contiguous states)', 'Japan', 'Canada', 'Europe (United Kingdom, Germany, France, Italy and Switzerland)', 'New Zealand', 'China', 'Korea', 'Taiwan', 'Other Asia (Hong Kong, Singapore, Malaysia, etc.)', 'Latin America (Argentina, Brazil and Mexico)', 'All Other Countries/Territories']
REFERRED = ['Airline/Airport', 'Car Rental Agency', 'County Police', 'Cruise Line', 'Hospital', 'Hotel', 'Non-Hotel Accommodation',
            'Other Agency', 'Other VAP Provider', 'Visitor Bureau', 'Tour/Travel Agency', 'Walk In/Direct', 'Volcano National Park', 'Pier']
POLICE_STATIONS = ["Honoka'a", 'Laupahoehoe', 'Hilo',
                   'Pahoa', "Na'alehu", 'Kona', 'Waimea', "Kapa'au"]
VISITOR_TYPE = ['Land', 'Cruise']
SEARCH_CATEGORIES = ['first name', 'last name', 'incident type', 'incident location',
                     'party size', 'cause of death', 'referred by', 'police station', 'visitor type', 'mma', 'notes']
