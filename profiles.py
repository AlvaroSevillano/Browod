def get_profiles():
    profiles = {'k7': [1, 0, 0, 0, 0, 0, 0],
                'k8': [3, 3, 1, 1, 2, 0, 0],
                'k7_haltero': [0, 0, 0, 0, 1, 0, 0],
                'k8_haltero': [3, 4, 1, 1, 3, 0, 0],
                'alvaro': [11, 0, 0, 0, 1, 0, 0]}

    assign_profiles = {'alberto': 'k8_haltero',
                       'alvaro': 'k7_haltero',
                       'amaya': 'k7',
                       'ana': 'k7_haltero',
                       'andoni': 'k7_haltero',
                       'blas': 'k7_haltero',
                       'chema': 'k7_haltero',
                       'javi': 'k7_haltero',
                       'jonas': 'k8_haltero',
                       'koldo': 'k7',
                       'laura': 'k7',
                       'leixuri': 'k7_haltero',
                       'marta': 'k7',
                       'risto': 'k8_haltero',
                       'ruben': 'k7_haltero',
                       'tere': 'k7_haltero'}

    return profiles, assign_profiles
