from django.db import migrations
import random
from datetime import datetime , timedelta
from django.utils import timezone



def data(apps, schema_editor):
    import time
    t1 = time.time()
    order_data = apps.get_model("migration_five_million" , "order_data")
    db_alisas = schema_editor.connection.alias

    cities = [("Karachi" , "KHI") , ("Lahore" , "LHR") , ("Islamabad" , "ISL") , ("Sialkot" , "SKT") , ("Peshawar" , "PEW") , 
    ("Quetta" , "UET") , ("Skardu" , "KDU")]


    travel_types = ["ONEWAY" , "RETURN"]
    
    
    for i in range (0, 5000000,10000):
        data_stored = []
        # threads = []
        for j in range(10000):
            # def add_data():
                
            destinations = random.choices(cities)
            origin = random.choices(cities)
            type = random.choices(travel_types)
            departure_time = timezone.now() + timedelta(days=random.randint(0, 10))

            data_stored.append(
                order_data(
                    created_at = (timezone.now() - timedelta(days=2)),
                    destination = destinations[0][0],
                    destination_iata = destinations[0][1],
                    origin = origin[0][0],
                    origin_iata = origin[0][1],
                    type = type,
                    departure = departure_time,
                    arrival = departure_time + timedelta(days=random.randint(1,2)),
                )
            )

                
            

        #     import threading
        #     th1 = threading.Thread(target = add_data)
        #     th1.start()
        #     threads.append(th1)

        # for thread in threads:
        #     thread.join()
        order_data.objects.using(db_alisas).bulk_create(data_stored)

    time = time.time() - t1
    print("total time is " , time/60)



class Migration(migrations.Migration):

    dependencies = [
        ("migration_five_million" , "0001_initial"),
    ]

    operations = [
        migrations.RunPython(data)
    ]
    


        