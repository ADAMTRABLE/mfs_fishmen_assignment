from django.db import models

# Create your models here.
class Arrival(models.Model):
    id = models.AutoField(primary_key=True)
    fish = models.CharField(max_length=20)
    weight = models.FloatField()
    cost_per_unit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total_amount(self):
        total_amount = float(self.weight * self.cost_per_unit)
        return total_amount
    
    
    def __str__(self):
        return f" {self.fish}"
    
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE)

    def calculate_payment(self):
        return 0.3 * self.arrival.calculate_total_amount()

    def __str__(self):
        return f"Payment for Arrival {self.arrival.id}"