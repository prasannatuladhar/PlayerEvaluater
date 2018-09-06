from django.shortcuts import render,redirect, get_object_or_404
from .models import Player
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'player/home.html')


def result(request):
    return render(request,'player/result.html')


def result_view(request):
    res = request.GET.get('result', False)
    return redirect('/game/' + str(res))

@login_required(login_url='/admin/login')
def create(request):
    if request.method == "POST":
        if request.POST['home_team'] and request.POST['away_team'] and request.POST['player1'] and request.POST['player2'] and request.POST['player3'] and request.POST['player4'] and \
                request.POST['player5'] and request.POST['player1_jersey'] and request.POST['player2_jersey'] and request.POST['player3_jersey'] and request.POST['player4_jersey'] and \
                request.POST['player5_jersey'] :
            player = Player()
            player.home_team = request.POST['home_team']
            player.away_team = request.POST['away_team']
            player.player1 = request.POST['player1']
            player.player2 = request.POST['player2']
            player.player3 = request.POST['player3']
            player.player4 = request.POST['player4']
            player.player5 = request.POST['player5']
            player.player1_jersey = request.POST['player1_jersey']
            player.player2_jersey = request.POST['player2_jersey']
            player.player3_jersey = request.POST['player3_jersey']
            player.player4_jersey = request.POST['player4_jersey']
            player.player5_jersey = request.POST['player5_jersey']
            player.save()
            return redirect('/game/' + str(player.id))
        else:
            return render(request, 'player/create_info.html')
    else:
         return render(request,'player/create_info.html')


def detail(request,player_id):
    player = get_object_or_404(Player,pk=player_id)
    return render(request,'player/detail.html',{"players": player})


@login_required(login_url='/admin/login')
def upvote_2p_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_2p_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_2p_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_2p_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_2p_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_3p_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_3p_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_3p_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_3p_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_3p_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_reb_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_reb_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_reb_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_reb_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_reb_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_turn_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_turn_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_turn_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_turn_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_turn_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_assist_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_assist_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_assist_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_assist_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_assist_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_steal_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_steal_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_steal_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_steal_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_steal_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_block_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player1 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_block_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player2 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_block_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player3 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_block_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player4 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def upvote_block_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player5 += 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_2p_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_2p_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_2p_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_2p_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_2p_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_2pt_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_3p_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_3p_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_3p_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_3p_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_3p_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_3pt_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_reb_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_reb_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_reb_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_reb_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_reb_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_rebounds_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_turn_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_turn_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_turn_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_turn_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_turn_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_turnovers_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_assist_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_assist_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_assist_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_assist_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_assist_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_assists_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_steal_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_steal_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_steal_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_steal_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_steal_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_steals_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_block_1(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player1 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_block_2(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player2 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_block_3(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player3 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_block_4(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player4 -= 1
    player.save()
    return redirect('/game/' + str(player_id))

@login_required(login_url='/admin/login')
def downvote_block_5(request,player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.counter_blocks_player5 -= 1
    player.save()
    return redirect('/game/' + str(player_id))


