from django.urls import path
from . import views

urlpatterns = [
    path('<int:player_id>',views.detail,name='detail'),
    path('<int:player_id>/upvote_2p_1',views.upvote_2p_1,name='upvote_2p_1'),
    path('<int:player_id>/upvote_2p_2',views.upvote_2p_2,name='upvote_2p_2'),
    path('<int:player_id>/upvote_2p_3',views.upvote_2p_3,name='upvote_2p_3'),
    path('<int:player_id>/upvote_2p_4',views.upvote_2p_4,name='upvote_2p_4'),
    path('<int:player_id>/upvote_2p_5',views.upvote_2p_5,name='upvote_2p_5'),
    path('<int:player_id>/upvote_3p_1',views.upvote_3p_1,name='upvote_3p_1'),
    path('<int:player_id>/upvote_3p_2',views.upvote_3p_2,name='upvote_3p_2'),
    path('<int:player_id>/upvote_3p_3',views.upvote_3p_3,name='upvote_3p_3'),
    path('<int:player_id>/upvote_3p_4',views.upvote_3p_4,name='upvote_3p_4'),
    path('<int:player_id>/upvote_3p_5',views.upvote_3p_5,name='upvote_3p_5'),
    path('<int:player_id>/upvote_reb_1',views.upvote_reb_1,name='upvote_reb_1'),
    path('<int:player_id>/upvote_reb_2',views.upvote_reb_2,name='upvote_reb_2'),
    path('<int:player_id>/upvote_reb_3',views.upvote_reb_3,name='upvote_reb_3'),
    path('<int:player_id>/upvote_reb_4',views.upvote_reb_4,name='upvote_reb_4'),
    path('<int:player_id>/upvote_reb_5',views.upvote_reb_5,name='upvote_reb_5'),
    path('<int:player_id>/upvote_turn_1',views.upvote_turn_1,name='upvote_turn_1'),
    path('<int:player_id>/upvote_turn_2',views.upvote_turn_2,name='upvote_turn_2'),
    path('<int:player_id>/upvote_turn_3',views.upvote_turn_3,name='upvote_turn_3'),
    path('<int:player_id>/upvote_turn_4',views.upvote_turn_4,name='upvote_turn_4'),
    path('<int:player_id>/upvote_turn_5',views.upvote_turn_5,name='upvote_turn_5'),
    path('<int:player_id>/upvote_assist_1',views.upvote_assist_1,name='upvote_assist_1'),
    path('<int:player_id>/upvote_assist_2',views.upvote_assist_2,name='upvote_assist_2'),
    path('<int:player_id>/upvote_assist_3',views.upvote_assist_3,name='upvote_assist_3'),
    path('<int:player_id>/upvote_assist_4',views.upvote_assist_4,name='upvote_assist_4'),
    path('<int:player_id>/upvote_assist_5',views.upvote_assist_5,name='upvote_assist_5'),
    path('<int:player_id>/upvote_steal_1',views.upvote_steal_1,name='upvote_steal_1'),
    path('<int:player_id>/upvote_steal_2',views.upvote_steal_2,name='upvote_steal_2'),
    path('<int:player_id>/upvote_steal_3',views.upvote_steal_3,name='upvote_steal_3'),
    path('<int:player_id>/upvote_steal_4',views.upvote_steal_4,name='upvote_steal_4'),
    path('<int:player_id>/upvote_steal_5',views.upvote_steal_5,name='upvote_steal_5'),
    path('<int:player_id>/upvote_block_1', views.upvote_block_1, name='upvote_block_1'),
    path('<int:player_id>/upvote_block_2', views.upvote_block_2, name='upvote_block_2'),
    path('<int:player_id>/upvote_block_3', views.upvote_block_3, name='upvote_block_3'),
    path('<int:player_id>/upvote_block_4', views.upvote_block_4, name='upvote_block_4'),
    path('<int:player_id>/upvote_block_5', views.upvote_block_5, name='upvote_block_5'),

    path('<int:player_id>/downvote_2p_1',views.downvote_2p_1,name='downvote_2p_1'),
    path('<int:player_id>/downvote_2p_2',views.downvote_2p_2,name='downvote_2p_2'),
    path('<int:player_id>/downvote_2p_3',views.downvote_2p_3,name='downvote_2p_3'),
    path('<int:player_id>/downvote_2p_4',views.downvote_2p_4,name='downvote_2p_4'),
    path('<int:player_id>/downvote_2p_5',views.downvote_2p_5,name='downvote_2p_5'),
    path('<int:player_id>/downvote_3p_1',views.downvote_3p_1,name='downvote_3p_1'),
    path('<int:player_id>/downvote_3p_2',views.downvote_3p_2,name='downvote_3p_2'),
    path('<int:player_id>/downvote_3p_3',views.downvote_3p_3,name='downvote_3p_3'),
    path('<int:player_id>/downvote_3p_4',views.downvote_3p_4,name='downvote_3p_4'),
    path('<int:player_id>/downvote_3p_5',views.downvote_3p_5,name='downvote_3p_5'),
    path('<int:player_id>/downvote_reb_1',views.downvote_reb_1,name='downvote_reb_1'),
    path('<int:player_id>/downvote_reb_2',views.downvote_reb_2,name='downvote_reb_2'),
    path('<int:player_id>/downvote_reb_3',views.downvote_reb_3,name='downvote_reb_3'),
    path('<int:player_id>/downvote_reb_4',views.downvote_reb_4,name='downvote_reb_4'),
    path('<int:player_id>/downvote_reb_5',views.downvote_reb_5,name='downvote_reb_5'),
    path('<int:player_id>/downvote_turn_1',views.downvote_turn_1,name='downvote_turn_1'),
    path('<int:player_id>/downvote_turn_2',views.downvote_turn_2,name='downvote_turn_2'),
    path('<int:player_id>/downvote_turn_3',views.downvote_turn_3,name='downvote_turn_3'),
    path('<int:player_id>/downvote_turn_4',views.downvote_turn_4,name='downvote_turn_4'),
    path('<int:player_id>/downvote_turn_5',views.downvote_turn_5,name='downvote_turn_5'),
    path('<int:player_id>/downvote_assist_1',views.downvote_assist_1,name='downvote_assist_1'),
    path('<int:player_id>/downvote_assist_2',views.downvote_assist_2,name='downvote_assist_2'),
    path('<int:player_id>/downvote_assist_3',views.downvote_assist_3,name='downvote_assist_3'),
    path('<int:player_id>/downvote_assist_4',views.downvote_assist_4,name='downvote_assist_4'),
    path('<int:player_id>/downvote_assist_5',views.downvote_assist_5,name='downvote_assist_5'),
    path('<int:player_id>/downvote_steal_1',views.downvote_steal_1,name='downvote_steal_1'),
    path('<int:player_id>/downvote_steal_2',views.downvote_steal_2,name='downvote_steal_2'),
    path('<int:player_id>/downvote_steal_3',views.downvote_steal_3,name='downvote_steal_3'),
    path('<int:player_id>/downvote_steal_4',views.downvote_steal_4,name='downvote_steal_4'),
    path('<int:player_id>/downvote_steal_5',views.downvote_steal_5,name='downvote_steal_5'),
    path('<int:player_id>/downvote_block_1', views.downvote_block_1, name='downvote_block_1'),
    path('<int:player_id>/downvote_block_2', views.downvote_block_2, name='downvote_block_2'),
    path('<int:player_id>/downvote_block_3', views.downvote_block_3, name='downvote_block_3'),
    path('<int:player_id>/downvote_block_4', views.downvote_block_4, name='downvote_block_4'),
    path('<int:player_id>/downvote_block_5', views.downvote_block_5, name='downvote_block_5'),

    path('create',views.create,name='create'),
]