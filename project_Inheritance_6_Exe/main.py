from project_Inheritance_6_Exe.guild import Guild
from project_Inheritance_6_Exe.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
