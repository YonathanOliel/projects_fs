from django.db import models


class Miluimnick(models.Model):

    first_name = models.CharField(max_length = 255, null = False)
    last_name = models.CharField(max_length = 255, null = False)
    name_business = models.CharField(max_length = 255, null = False)
    business_city = models.CharField(max_length = 255, null = False)
    business_street = models.CharField(max_length = 255, null = False)
    business_address = models.IntegerField(null = False)
    business_type = models.CharField(max_length = 255, null = False)
    link_google_maps = models.CharField(max_length = 255, default = r"https://www.google.com/maps/place/%D7%99%D7%A9%D7%A8%D7%90%D7%9C%E2%80%AD/@31.383865,37.7233517,7z/data=!3m1!4b1!4m6!3m5!1s0x1500492432a7c98b:0x6a6b422013352cba!8m2!3d31.046051!4d34.851612!16zL20vMDNzcHo?authuser=0&entry=ttu")


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    



    


