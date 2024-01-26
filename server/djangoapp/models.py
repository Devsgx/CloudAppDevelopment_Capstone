from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model)`:
    name=models.CharField(null=False,max_length=20)
    description=models.CharField(null=False,max_length=500)
  
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    SEDAN='Sedan'
    SUV='SUV'
    WAGON='Wagon'
    type=[(SEDAN='Sedan'),
    (SUV='SUV'),
    (WAGON='Wagon')]
    name = models.CharField(null=False, max_length=20)
    description = models.CharField(max_length=500)
    make=models.ForeignKey(CarMake, null=False)
    cartype=models.CharField(max_length=10, choices=type, default=SEDAN)
    dealer=models.IntegerField()
    year=models.DateField()
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description + "," + \
         "Type: " + self.cartype + "," + \
            "Year :" + self.year + "," + \

        
# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer(models.Model):
    city = models.CharField(null=False, max_length=50)
    state = models.CharField(max_length=20)
    st = models.CharField(max_length=2)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(null=False, max_length=50)
    full_name = models.CharField(null=False, max_length=50)
        
    # Create a toString method for object string representation
    def __str__(self):
        return "City: " + self.city + "," + \
            "State: " + self.state + "," + \
         "St: " + self.st + "," + \
            "Address: " + self.address + "," + \
         "Zip: " + self.zip + "," + \
         "Lat: " + self.lat + "," + \
            "Long: " + self.long + "," + \
         "Short Name: " + self.short_name + "," + \
         "Full Name: " + self.full_name + "," + \        
        
# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    name = models.CharField(null=False, max_length=50)
    dealership = models.IntegerField()
    review = models.CharField(max_length=500)
    purchase = models.BooleanField()
    purchase_date = models.DateField()
    car_make = models.CharField()
    car_model = models.CharField()
    car_year = models.IntegerField()
            
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Dealership: " + self.dealership + "," + \
         "Review: " + self.review + "," + \
            "Purchase Date: " + self.purchase_date + "," + \
         "Car Make: " + self.car_make + "," + \
         "Car Model: " + self.car_model + "," + \
            "Car Year: " + self.car_year + "," + \
