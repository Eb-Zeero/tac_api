from dateutil.relativedelta import relativedelta
from app.alchemy.config import con
import pandas as pd
import datetime


def partner_list():
    """
    This method select the partner names from the database,
    the data is read from the database using pandas python library
    and connected via mysql connection

    :returns:
    the list of partner names inside the dictionary
    """

    sql = "SELECT Partner_Name FROM Partner;"
    data = pd.read_sql(sql, con)
    dct = {
        'Partner_Names': list(data['Partner_Name'])
    }
    return dct


def semester():
    """
    This method
    *select from the database and concatenate two results
    *select from the database only the data that is in the range of three months

    then read the queries from the database using pandas

    :returns

    the list of all semesters and years separated by underscore in between
    and the only list of semester and year  that is currently on the 3 months range each day

    """
    date = datetime.datetime.now().date()
    date_3 = date + relativedelta(months=3)

    firstQuery='SELECT  CONCAT(Year,"_",Semester)as results FROM Semester '

    secondQuery = 'SELECT CONCAT(Year,"_", Semester)as current FROM  Semester ' \
                  '     where StartSemester < "{date_}" and "{date_}" < EndSemester;'.format(date_=date_3)
    data1 = pd.read_sql(firstQuery, con)
    data = pd.read_sql(secondQuery, con)

    return {'Year and Semester ': list(data1['results']),
            'Active semester': list(data['current'])[0]}

