from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DronesCategory
from drones.models import Pilot
from drones.models import Competition
from drones.models import Drone
from drones.serializers import DronesCategorySerializer
from drones.serializers import DroneSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer
from drones.serializers import PilotMinimalSerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


class DronesCategoryList(generics.ListCreateAPIView):
    queryset = DronesCategory.objects.all()
    serializer_class = DronesCategorySerializer
    name = 'dronescategory-list'

    filter_fields = ('name',) #under the hood, django will automatically create a FilterSet class and associate it to this.
    search_fields = ('^name',)
    ordering_fields = ('name',)


class DronesCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DronesCategory.objects.all()
    serializer_class = DronesCategorySerializer
    name = 'dronescategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'

    filter_fields = ('name','drones_category','manufacturing_date','has_it_completed',)
    search_fields = ('=name',)
    ordering_fields = ('name','manufacturing_date',)

    def perform_create (self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all() 
    serializer_class = PilotMinimalSerializer
    name = 'pilot-list'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

class CompetitionFilter(filters.FilterSet):
    from_achievement_date = DateTimeFilter(name = 'distance_achievement_date', lookup_expr = 'gte')
    to_achievement_date = DateTimeFilter(name='distance_achievement_date', lookup_expr = 'lte')
    min_distance_in_feet = NumberFilter(name='distance_in_feet', lookup_expr = 'gte')
    max_distance_in_feet = NumberFilter(name='distance_in_feet', lookup_expr = 'lte')
    drone_name = AllValuesFilter(name='drone__name')
    pilot_name = AllValuesFilter(name='pilot__name')

    class Meta:
        model = Competition 
        fields = ('distance_in_feet','from_achievement_date','to_achievement_date',
                    'min_distance_in_feet','max_distance_in_feet','drone_name','pilot_name')

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'

    filter_class = CompetitionFilter  ##This is the filterset subclass to customize our filters
    ordering_fields = ('distance_in_feet','distance_achievement_date')


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DronesCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
