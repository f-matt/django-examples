from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from main.models import Model2
from main.serializers import Model2Serializer

class Model2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Model2.objects.all()
    serializer_class = Model2Serializer

    def get_queryset(self):
        col1 = self.request.query_params.get('col1')
        if col1 is None:
            raise ValidationError(detail='Query parameter is mandatory')

        return Model2.objects.filter(col1__iexact=col1).values()