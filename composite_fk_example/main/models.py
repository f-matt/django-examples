from django.db import models
from viewflow.fields import CompositeKey

class Model1(models.Model):
    id =  CompositeKey(columns=['id1', 'id2'])
    col1 = models.CharField()

    class Meta:
        managed = False
        db_table = 'model1'


class Model2(models.Model):
    id = models.IntegerField(primary_key=True)
    model1_id1 = models.IntegerField()
    model1_id2 = models.IntegerField()
    model1_id = CompositeKey(columns=['model1_id1', 'model1_id2'])
    col1 = models.CharField()

    model1 = models.ForeignKey(Model1, on_delete=models.PROTECT)

    class Meta:
        db_table = 'model2'