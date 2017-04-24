import pandas as pd
from .models import *



def loadAffordability(file):
    df = pd.read_csv(file)

    # Convert NaN values to None for db insert
    dframe = df.where((pd.notnull(df)), None)

    # Convert NaN to none for db insertion

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['Year'])
        n, _ = Neighborhood.objects.get_or_create(NP_ID=row['NP_ID'])
        d, _ = Demographic.objects.get_or_create(name=row['Demographic'])
        h, _ = HousingSize.objects.get_or_create(household_type=row['Unit_Size'])
        ry.save()
        d.save()
        h.save()
        n.save()
        if row['Affordable_ind'] == 'Y':
            aff = True
        elif row['Affordable_ind'] == 'N':
            aff = False

        a = Affordable(
            affordable=aff,
            demographic=d,
            housing_size=h,
            neighborhood=n,
            year=ry
        )
        a.save()

def loadDemoByYear(file):
    df = pd.read_csv(file)

    dframe = df.where((pd.notnull(df)), None)


    for index, row in dframe.iterrows():
            ry, _ = ReportYear.objects.get_or_create(year=row['DP_REPORTYEAR'])
            demo, _ = Demographic.objects.get_or_create(name=row['DP_TITLE'])
            ry.save()
            demo.save()
            demo_by_year = DemographicByYear(
                demographic=demo,
                income_median=row['DP_INCOME_MEDIAN'],
                housing_budget=row['DP_HOUSINGBUDGET'],
                per_with_children=row['DP_PERCENT_WITH_CHILDREN'],
                household_comp=row['DP_HOUSEHOLD_COMP'],
                year=ry,
            )
            demo_by_year.save()

def loadNeighborhoodRent(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['NHM_ReportYear'])
        n, _ = Neighborhood.objects.get_or_create(NP_ID=row['NP_ID'])
        h, _ = HousingSize.objects.get_or_create(household_type=row['NHM_UnitSize'])
        ry.save()
        n.save()
        h.save()
        rent, _ = NeighborhoodRent.objects.get_or_create(
                nh_id=n,
                housing_size=h,
                rent_amt=row['NHM_Rent_Amt'],
                year=ry,
        )
        rent.save()

def loadNeighborhoodProfiles(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        this_neighborhood, _ = Neighborhood.objects.get_or_create(
                NP_ID=row['NP_ID'],
                name=row['NP_Title']
        )
        this_neighborhood.save()

def loadHousingSupplyandPermits(file):
    """Load housing supply and permit data into respective models"""

    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['ReportYear'])
        n, _ = Neighborhood.objects.get_or_create(NP_ID=row['NP_ID'])
        hs = HousingSupply(
                            neighborhood=n,
                            report_year=ry,
                            single_units=row['SingleFamilyUnits'],
                            multi_units=row['MultiFamilyUnits']
        )
        hs.save()

        hp = HousingPermits(
                            neighborhood=n,
                            report_year=ry,
                            single_permits=row['SingleFamilyPermits'],
                            multi_permits=row['MultiFamilyPermits']
        )
        hp.save()


def loadHHToolTip(file):
    """ Load hh tooltip data from csv """
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['Year'])
        n, _ = Neighborhood.objects.get_or_create(NP_ID=row['NP_ID'])

        this_tooltip = HHToolTip(
                                neighborhood=n,
                                year=ry,
                                demographic=row['Demographic'],
                                households=row['Households']
                                )

        this_tooltip.save()


def loadPopToolTip(file):
    """ Load hh tooltip data from csv """
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['Year'])
        n, _ = Neighborhood.objects.get_or_create(NP_ID=row['NP_ID'])

        this_tooltip = PopToolTip(
                                neighborhood=n,
                                year=ry,
                                ethnicity=row['Ethnicity'],
                                population=row['Population']
                                )

        this_tooltip.save()


fileDemo = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/DemographicProfiles_w2015_Profiles_2-15-17.csv"
fileNeighborhoods = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/NeighborhoodProfiles.csv"
fileAfford = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv"
fileRent = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/NeighborhoodHousingMarket.csv"
fileSupply = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/HousingSupplyAndPermits.csv"
fileHHToolTips = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/hhToolTips.csv"
filePopToolTips = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/popToolTips.csv"

# Load year and neighborhood first because loadAffordability depends on it
loadDemoByYear(fileDemo)
loadNeighborhoodProfiles(fileNeighborhoods)


loadAffordability(fileAfford)
loadNeighborhoodRent(fileRent)
loadHousingSupplyandPermits(fileSupply)
loadHHToolTip(fileHHToolTips)
loadPopToolTip(filePopToolTips)
