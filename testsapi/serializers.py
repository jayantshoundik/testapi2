from rest_framework import serializers

from testsapi.models import Member, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = [ 'member','start_time', 'end_time']
        
class ActivityPeriod2Serializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = [ 'start_time', 'end_time']     
    

class MemberSerializer(serializers.ModelSerializer):
    activityperiod = ActivityPeriod2Serializer(many=True)
    class Meta:
        model = Member
        fields = ['idno','real_name', 'timezone','activityperiod']
        depth =2
    