from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    home_team = models.CharField(max_length=25, default="Home Team")
    away_team = models.CharField(max_length=25, default="Away Team")
    player1 = models.CharField(max_length=25, default="Player1")
    player2 = models.CharField(max_length=25, default="Player2")
    player3 = models.CharField(max_length=25, default="Player3")
    player4 = models.CharField(max_length=25, default="Player4")
    player5 = models.CharField(max_length=25, default="Player5")
    player1_jersey = models.CharField(max_length=2, default="01")
    player2_jersey = models.CharField(max_length=2, default="02")
    player3_jersey = models.CharField(max_length=2, default="03")
    player4_jersey = models.CharField(max_length=2, default="04")
    player5_jersey = models.CharField(max_length=2, default="05")
    counter_2pt_player1 = models.IntegerField(default=0)
    counter_2pt_player2 = models.IntegerField(default=0)
    counter_2pt_player3 = models.IntegerField(default=0)
    counter_2pt_player4 = models.IntegerField(default=0)
    counter_2pt_player5 = models.IntegerField(default=0)
    counter_3pt_player1 = models.IntegerField(default=0)
    counter_3pt_player2 = models.IntegerField(default=0)
    counter_3pt_player3 = models.IntegerField(default=0)
    counter_3pt_player4 = models.IntegerField(default=0)
    counter_3pt_player5 = models.IntegerField(default=0)
    counter_rebounds_player1 = models.IntegerField(default=0)
    counter_rebounds_player2 = models.IntegerField(default=0)
    counter_rebounds_player3 = models.IntegerField(default=0)
    counter_rebounds_player4 = models.IntegerField(default=0)
    counter_rebounds_player5 = models.IntegerField(default=0)
    counter_turnovers_player1 = models.IntegerField(default=0)
    counter_turnovers_player2 = models.IntegerField(default=0)
    counter_turnovers_player3 = models.IntegerField(default=0)
    counter_turnovers_player4 = models.IntegerField(default=0)
    counter_turnovers_player5 = models.IntegerField(default=0)
    counter_assists_player1 = models.IntegerField(default=0)
    counter_assists_player2 = models.IntegerField(default=0)
    counter_assists_player3 = models.IntegerField(default=0)
    counter_assists_player4 = models.IntegerField(default=0)
    counter_assists_player5 = models.IntegerField(default=0)
    counter_steals_player1 = models.IntegerField(default=0)
    counter_steals_player2 = models.IntegerField(default=0)
    counter_steals_player3 = models.IntegerField(default=0)
    counter_steals_player4 = models.IntegerField(default=0)
    counter_steals_player5 = models.IntegerField(default=0)
    counter_blocks_player1 = models.IntegerField(default=0)
    counter_blocks_player2 = models.IntegerField(default=0)
    counter_blocks_player3 = models.IntegerField(default=0)
    counter_blocks_player4 = models.IntegerField(default=0)
    counter_blocks_player5 = models.IntegerField(default=0)

    def counter_total_1(self):
        return self.counter_2pt_player1*2 + self.counter_3pt_player1*3

    def counter_total_2(self):
        return self.counter_2pt_player2*2 + self.counter_3pt_player2*3

    def counter_total_3(self):
        return self.counter_2pt_player3*2 + self.counter_3pt_player3*3

    def counter_total_4(self):
        return self.counter_2pt_player4*2 + self.counter_3pt_player4*3

    def counter_total_5(self):
        return self.counter_2pt_player5*2 + self.counter_3pt_player5*3
