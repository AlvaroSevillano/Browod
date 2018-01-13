def get_profiles(name):
    int_time_k7 = "07:00 - 08:00"
    int_time_k8 = "08:00 - 09:00"

    haltero = 'Weig'
    crossfit = 'CrossFit'
    gymnastics = 'Gymnas'
    endurance = 'Endurance'

    profiles = {'k7': [int_time_k7, [crossfit, gymnastics, endurance, haltero]],
                'k8': [int_time_k8, [crossfit, gymnastics, endurance, haltero]],
                'k7_haltero': [int_time_k7, [haltero, crossfit, gymnastics, endurance]],
                'k8_haltero': [int_time_k8, [haltero, crossfit, gymnastics, endurance]]}

    assign_profiles = {'alberto': ['k8_haltero','albertogarciamoreno0@gmail.com|Bradybooth12',5],
                       'alvaro': ['k7_haltero','yuhp14@hotmail.com|alvaro88',2],
                       'ana': ['k7_haltero','anaglezgciagc@yahoo.es|Aimharder456',6],
                       'andoni': ['k7_haltero','andoniruiz@hotmail.com|molotov0',5],
                       'blas': ['k7_haltero','vladisimon@gmail.com|abc123456+',4],
                       'chema': ['k7_haltero','jmruedahernandez@gmail.com|alvaromola1000',7],
                       'horacio': ['k8_haltero','halcala@gmail.com|Klan8Madrid',8],
                       'javi': ['k7_haltero','javialonsoramirez@gmail.com|Capricho1303',6],
                       'jonas': ['k8_haltero','juanfrcarro@gmail.com|jonas47352436J',8],
                       'koldo': ['k7','kolabarri@gmail.com|koldoklan',5],
                       'laura': ['k7','lauradoxsey@gmail.com|sev1lla!!AR',4],
                       'leixuri': ['k7_haltero','leixuridefrutos@gmail.com|vivirViajando1',7],
                       'risto': ['k8_haltero','ristotapani@gmail.com|poikanen74',6],
                       'ruben': ['k7_haltero','rubensendin87@gmail.com|19L0ndr3s87',4]}

    return profiles[assign_profiles[name][0]][0], profiles[assign_profiles[name][0]][1], \
           assign_profiles[name][1], assign_profiles[name][2]
