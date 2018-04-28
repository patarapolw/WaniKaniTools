import os
import pytest

import tests
from WaniKaniTools.api import APIv1, APIv2

if 'TRAVIS' not in os.environ:
    api_v2 = APIv2()


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
@pytest.mark.parametrize('resource', ['user-information',
                                      'study-queue',
                                      'level-progression',
                                      'srs-distribution',
                                      'recent-unlocks',  # Argument is output limit in range 1-100. Default=10
                                      'critical-items',  # Argument is percentage in range 0-100. Default=75
                                      'radicals',  # Argument is level, comma-delimited. Default=all levels
                                      'kanji',
                                      'vocabulary'])
def test_api_v1(resource):
    api_v1 = APIv1()
    result = api_v1.GET(resource)['requested_information']
    print(result)


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
@pytest.mark.parametrize('resource', ['user',
                                      'subjects',  # Argument is id. Params are ids, types, slugs, levels, updated_after
                                      'assignments',  # Argument is id. Params are ...
                                      'review_statistics',
                                      'study_materials',
                                      'summary',
                                      'reviews',
                                      'level_progressions',
                                      'resets'
                                      ])
def test_api_v2(resource):
    result = api_v2.GET(resource)

    print(result)
    # api_v2.GETurl also available: api_v2.GETurl(next_url)


if __name__ == '__main__':
    pytest.main([__file__, '-s'])
