from django.db import models

class ReportYear(models.Model):
    year = models.IntegerField(default=0)

    def __str__(self):
        return str(self.year)

    def __repr__(self):
        return str(self.year)

class Affordable(models.Model):
    affordable = models.BooleanField()
    demographic = models.ForeignKey('Demographic', on_delete=models.CASCADE)
    housing_size = models.ForeignKey('HousingSize', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)
    year = models.ForeignKey('ReportYear', on_delete=models.CASCADE, null=True)

    def __str__(self):
        template = "{dm} {sz} {nh}"
        return template.format(dm=self.demographic, sz=self.housing_size, nh=self.neighborhood)

    def __repr__(self):
        template = "{dm} {sz} {nh}"
        return template.format(dm=self.demographic, sz=self.housing_size, nh=self.neighborhood)


class NeighborhoodRent(models.Model):
    nh_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)
    housing_size = models.ForeignKey('HousingSize', on_delete=models.CASCADE)
    rent_amt = models.IntegerField(default=0)
    year = models.ForeignKey('ReportYear', on_delete=models.CASCADE, help_text='Year for this rent sample', null=True)
    
   
class Demographic(models.Model):
    name = models.CharField(max_length=50, help_text='Name of this demographic group', unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class DemographicByYear(models.Model):
    demographic = models.ForeignKey('Demographic', on_delete=models.CASCADE)
    income_median = models.IntegerField(default=0)
    housing_budget = models.IntegerField(default=0)
    per_with_children = models.IntegerField(default=0, null=True)
    household_comp = models.DecimalField(default=0.0, max_digits=3, decimal_places=2, null=True)
    year = models.ForeignKey('ReportYear', on_delete=models.CASCADE, help_text='Year for this demographic sample',
                             null=True)

    def __str__(self):
        """ Return a human readable string """
        template = "DemographicByYear object: {y} {dm}"
        return template.format(dm=self.demographic, y=self.year)

    def __repr__(self):
        """ Return a human readable representation of this object """
        template = "DemographicByYear object: {y} {dm}"
        return template.format(dm=self.demographic, y=self.year)

class HousingSize(models.Model):
    household_type = models.CharField(max_length=50)

    def __str__(self):
        return self.household_type

    def __repr__(self):
        return self.household_type

      
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

    #shape_file = models.FieldFile() possibility if shape file data needs to be stored

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name




class HousingSupply(models.Model):
    """ Models single year of one neighborhood's housing supply """
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, help_text='Neighborhood by census tract')
    report_year = models.ForeignKey('ReportYear', on_delete=models.CASCADE)
    single_units = models.IntegerField(default=0, help_text='Single Family units available this year')
    multi_units = models.IntegerField(default=0, help_text='Multi-Family units available this year')

    def __str__(self):
        template = "HousingSupply: {nh} {yr}"
        return template.format(nh=self.neighborhood, yr=self.report_year)

    def __repr__(self):
        template = "HousingSupply: {nh} {yr}"
        return template.format(nh=self.neighborhood, yr=self.report_year)


class HousingPermits(models.Model):
    """ Models single year of one neighborhood's housing permits issued """
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, help_text='Neighborhood by census tract')
    report_year = models.ForeignKey('ReportYear', on_delete=models.CASCADE)
    single_permits = models.IntegerField(default=0, help_text='Single Family permits issued this year')
    multi_permits = models.IntegerField(default=0, help_text='Multi-Family permits issued this year')

    def __str__(self):
        template = "HousingPermits: {nh} {yr}"
        return template.format(nh=self.neighborhood, yr=self.report_year)

    def __repr__(self):
        template = "HousingPermits: {nh} {yr}"
        return template.format(nh=self.neighborhood, yr=self.report_year)


class HousingProductionVsCost(models.Model):
    """ Models Production, Cost, Percent Growth for viz """

    year = models.ForeignKey('ReportYear', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, help_text='Neighborhood by census tract')
    single_unit_growth = models.FloatField(help_text="Single-family unit percent growth vs previous year")
    multi_unit_growth = models.FloatField(help_text="Multi-family unit percent growth vs previous year")
    home_price_growth = models.FloatField(help_text="Home price percent growth vs previous year")
    rent_growth = models.FloatField(help_text="Rent percent growth vs previous year")



