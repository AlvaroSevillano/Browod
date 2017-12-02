def get_profiles(name):
    int_time_k7 = "07:00 a 08:00"
    int_time_k8 = "08:00 a 09:00"

    haltero = 'Weig'
    crossfit = 'Crossfit'
    gymnastics = 'Gymnas'
    endurance = 'Endurance'

    profiles = {'k7': [int_time_k7, [crossfit, gymnastics, endurance, haltero]],
                'k8': [int_time_k8, [crossfit, gymnastics, endurance, haltero]],
                'k7_haltero': [int_time_k7, [haltero, crossfit, gymnastics, endurance]],
                'k8_haltero': [int_time_k8, [haltero, crossfit, gymnastics, endurance]]}

    assign_profiles = {'alberto': ['k8_haltero','albertogarciamoreno0@gmail.com|bradybooth12',5],
                       'alvaro': ['k7_haltero','yuhp14@hotmail.com|25Jan2013%',2],
                       'amaya': ['k7','amayafrias@gmail.com|melocoton77',4],
                       'ana': ['k7_haltero','anaglezgciagc@yahoo.es|Browod456',6],
                       'andoni': ['k7_haltero','andoniruiz@hotmail.com|molotov0',5],
                       'blas': ['k7_haltero','vladisimon@gmail.com|abc123456+',4],
                       'chema': ['k7_haltero','jmruedahernandez@gmail.com|alvaromola',7],
                       'javi': ['k7_haltero','javialonsoramirez@gmail.com|Golessonamores',6],
                       'jonas': ['k8_haltero','juanfrcarro@gmail.com|jonas47352436j',8],
                       'koldo': ['k7','kolabarri@gmail.com|koldoklan',5],
                       'laura': ['k7','lauradoxsey@gmail.com|sev1lla!!BD',4],
                       'leixuri': ['k7_haltero','leixuridefrutos@gmail.com|87654321',7],
                       'marta': ['k7','martamedinam@yahoo.es|12345678',4],
                       'risto': ['k8_haltero','ristotapani@gmail.com|poikanen',6],
                       'ruben': ['k7_haltero','rubensendin87@gmail.com|19L0ndr3s87',4],
                       'tere': ['k7_haltero','teresa.medina.moreno@hotmail.com|teresa72',7]}

    return profiles[assign_profiles[name][0]][0], profiles[assign_profiles[name][0]][1], \
           assign_profiles[name][1], assign_profiles[name][2]
