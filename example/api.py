from WaniKaniTools.api import __init__

if __name__ == '__main__':
    import os
    os.chdir('..')

    # api_v1
    resource = (
        'user-information',
        'study-queue',
        'level-progression',
        'srs-distribution',
        'recent-unlocks',  # Argument is output limit in range 1-100. Default=10
        'critical-items',  # Argument is percentage in range 0-100. Default=75
        'radicals',  # Argument is level, comma-delimited. Default=all levels
        'kanji',
        'vocabulary'
    )
    api_v1 = __init__.v1()
    result = api_v1.GET(resource[2])['requested_information']
    print(result)

    # api_v2
    resource_v2 = (
        'user',
        'subjects',  # Argument is id. Params are ids, types, slugs, levels, updated_after
        'assignments',  # Argument is id. Params are ...
        'review_statistics',
        'study_materials',
        'summary',
        'reviews',
        'level_progressions',
        'resets'
    )
    api_v2 = __init__.v2()
    result = api_v2.GET(resource_v2[1])

    print(result)
