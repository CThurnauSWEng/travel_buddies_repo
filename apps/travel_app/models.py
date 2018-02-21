from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

from datetime import datetime

class TripManager(models.Manager):
    def validate_trip_data(self, post_data):
        response = {
            'status' : True
        }
        errors = []

        if len(post_data['destination']) < 1:
            errors.append("Destination must be at least 1 character long")

        if len(post_data['description']) < 1:
            errors.append("Description must be at least 1 character long")

        current_date = datetime.now()
        formattedDate = current_date.strftime("%Y-%m-%d")

        if post_data['dateFrom'] < formattedDate:
            errors.append("From travel date must be in the future")
        
        if post_data['dateTo'] < post_data['dateFrom']:
            errors.append("To travel date must be after the from date")

        if len(errors) > 0:
            response['status'] = False
            response['errors'] = errors
        else:
            this_user = User.objects.get(id=post_data['user_id'])
            trip = Trip.objects.create(
                destination = post_data['destination'],
                description = post_data['description'],
                plannedBy   = this_user,
                dateFrom    = post_data['dateFrom'],
                dateTo      = post_data['dateTo']
            )
            trip.travelers.add(this_user)
            response['trip'] = trip

        return response


# Models
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    plannedBy   = models.ForeignKey(User,related_name="planned_trips")
    dateFrom    = models.DateField()
    dateTo      = models.DateField()
    travelers   = models.ManyToManyField(User,related_name="trips")
    createdAt   = models.DateTimeField(auto_now_add=True)
    updatedAt   = models.DateTimeField(auto_now_add=True)
    objects     = TripManager()




