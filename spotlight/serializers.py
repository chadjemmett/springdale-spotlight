from rest_framework import serializers

from . models import Winner

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = [
                "paragraph",
                "winner_name",
                "social_media_url",
                "image_1",
                "image_2",
                "image_3",
                "alt_text_1",
                "alt_text_2",
                "alt_text_3",
                "headline",

                ]
