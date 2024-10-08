from rest_framework import serializers

from .models import SolutionPage


class SolutionPageSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        clap_data = validated_data.pop("claps_no")
        claps_old = instance.claps_no
        instance.claps_no = claps_old + clap_data
        instance.save()
        return instance

    class Meta:
        model = SolutionPage
        fields = ["claps_no"]
