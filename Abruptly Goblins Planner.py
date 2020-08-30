#Change for git 
#Change for git branch

gamers=[]

def add_gamer(gamer,gamers_list):
    if "name" in gamer.keys() and "availability" in gamer.keys():
        gamers_list.append(gamer)
    return gamers_list

kimberly={"name":"Kimberly Warner","availability":["Monday","Tuesday","Friday"]}
add_gamer(kimberly,gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)

def build_daily_frequency_table():
    return {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
count_availability=build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for name,avail_days in gamer.items():
            for avail_day in avail_days:
                if avail_day in available_frequency.keys():
                    available_frequency[avail_day] += 1
    return available_frequency

print(calculate_availability(gamers,count_availability))


def find_best_night(availability_table):
    max_day=""
    max=0
    for key,value in availability_table.items():
        if value > max:
            max = value
            max_day=key
    return max_day

game_night=find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list,day):
    a=[]
    for player in gamers_list:
        for key,value in player.items():
            if day in value:
                a.append(player["name"])

    return a

attending_game_night=available_on_night(gamers,game_night)
print(attending_game_night)

form_email="{name}, please come on {day_of_week} to play {game}"



def send_email(gamers_who_can_attend,day,game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer,day_of_week=day,game=game))

send_email(attending_game_night,game_night,"Abruptly Goblins")


unable_to_attend_best_night=gamers.copy()
for gamer in gamers:
    if gamer["name"] in attending_game_night:
        unable_to_attend_best_night.remove(gamer)
print(unable_to_attend_best_night)

second_night_availability=build_daily_frequency_table()
print(calculate_availability(unable_to_attend_best_night,second_night_availability))

second_night=find_best_night(second_night_availability)
print(second_night)

available_second_game_night=available_on_night(unable_to_attend_best_night,second_night)
print(available_second_game_night)

send_email(available_second_game_night,second_night,"Abruptly Goblins")