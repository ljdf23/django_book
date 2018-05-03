from rest_framework import serializers
from drones.models import DronesCategory
from drones.models import Pilot
from drones.models import Competition
from drones.models import Drone
from drones import views

class DroneSerializer(serializers.ModelSerializer):
    # display the category name
    drones_category = serializers.SlugRelatedField(
        queryset=DronesCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = ('name', 'drones_category', 'manufacturing_date',
                  'has_it_completed', 'inserted_timestamp')

    def __unicode__(self):
        return '%d: %s' % (self.name, self.has_it_completed)

class DroneMinimalSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Drone
        fields = ('name', 'has_it_completed')
 
class DronesCategorySerializer(serializers.ModelSerializer):
    drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')
 
    #drones = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    #drones = serializers.StringRelatedField(many=True)
    #drones = DroneSerializer(many=True, read_only=True)

    class Meta:
        model = DronesCategory
        fields = ('pk', 'name', 'drones')

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # display all the details for the related drone
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'distance_in_feet',
                  'distance_achievement_date', 'drone')
  
class CompetitionMinimalSerializer(serializers.HyperlinkedModelSerializer):
    # display all the details for the related drone
    drone = DroneMinimalSerializer()

    class Meta:
        model = Competition
        fields = ('distance_in_feet', 'drone')
  
class PilotMinimalSerializer(serializers.ModelSerializer):
    competitions = CompetitionMinimalSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)
    key = 'asd'

    class Meta:
        model = Pilot
        fields = ( 'name', 'id', 'gender', 'gender_description',
                  'races_count', 'inserted_timestamp' ,'competitions')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)
  
    class Meta:
        model = Pilot
        fields = ( 'name', 'id', 'gender', 'gender_description',
                  'races_count', 'inserted_timestamp' ,'competitions')
 
class PilotCompetitionSerializer(serializers.ModelSerializer):
    # display the pilot's name
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(), slug_field='name')
    # display the drone's name
    drone = serializers.SlugRelatedField(
        queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'distance_in_feet',
                  'distance_achievement_date', 'pilot', 'drone')
