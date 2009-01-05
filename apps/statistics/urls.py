from django.conf.urls.defaults import *

urlpatterns = patterns('statistics.views',
    url(r'^$', 'index', name='statistics_index'),
    (r'^(?P<user_type>(user|team))/(?P<user_id>\d+)/year/(?P<year>\d{4,4})/week/(?P<week>[1-9]|[1-4][0-9]|5[0-3])/$', 'display_user_type_week'),
    (r'^(?P<user_type>(user|team))/(?P<user_id>\d+)/year/(?P<year>\d{4,4})/month/(?P<month>[1-9]|1[0-2])/$', 'display_user_type_month'),
    (r'^(?P<user_type>(user|team))/(?P<user_id>\d+)/date/selection/$', 'user_type_date_selection_form'),
    (r'^(?P<user_type>(user|team))/(?P<user_id>\d+)/date/(?P<start_date>[0-9-]+)/(?P<end_date>[0-9-]+)/$', 'display_user_type_date_selection'),

    (r'^team_stat/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/week/(?P<week>[1-9]|[1-4][0-9]|5[0-3])/$', 'display_team_stat_week'),
    (r'^team_stat/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/month/(?P<month>[1-9]|1[0-2])/$', 'display_team_stat_month'),
    (r'^team_stat/(?P<team_id>\d+)/date/selection/$', 'team_stat_date_selection_form'),
    (r'^team_stat/(?P<team_id>\d+)/date/(?P<start_date>[0-9-]+)/(?P<end_date>[0-9-]+)/$', 'display_team_stat_date_selection'),

    (r'^data/user/(?P<user_id>\d+)/year/(?P<year>\d{4,4})/week/(?P<week>[1-9]|[1-4][0-9]|5[0-3])/$', 'data_user_week'),
    (r'^data/user/(?P<user_id>\d+)/year/(?P<year>\d{4,4})/month/(?P<month>[1-9]|1[0-2])/$', 'data_user_month'),
    (r'^data/user/(?P<user_id>\d+)/date/(?P<start_date>[0-9-]+)/(?P<end_date>[0-9-]+)/$', 'data_user_date'),

    (r'^data/team/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/week/(?P<week>[1-9]|[1-4][0-9]|5[0-3])/$', 'data_team_week'),
    (r'^data/team/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/month/(?P<month>[1-9]|1[0-2])/$', 'data_team_month'),
    (r'^data/team/(?P<team_id>\d+)/date/(?P<start_date>[0-9-]+)/(?P<end_date>[0-9-]+)/$', 'data_team_date'),

    (r'^data/team_stat/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/week/(?P<week>[1-9]|[1-4][0-9]|5[0-3])/$', 'data_team_stat_week'),
    (r'^data/team_stat/(?P<team_id>\d+)/year/(?P<year>\d{4,4})/month/(?P<month>[1-9]|1[0-2])/$', 'data_team_stat_month'),
    (r'^data/team_stat/(?P<team_id>\d+)/date/(?P<start_date>[0-9-]+)/(?P<end_date>[0-9-]+)/$', 'data_team_stat_date'),
)
