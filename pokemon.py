class Pokemon:
    def __init__(self,name,level,type,maximum_health,current_health,is_knocked_out):
        self.name=name
        self.level=level
        self.type=type
        self.maximum_health=maximum_health
        self.current_health=current_health
        self.is_knocked_out=is_knocked_out

    def lose_health(self,lose):
        self.lose=lose
        return self.name+" lost "+str(self.lose)+" health."
    def gain_health(self,gain):
        self.gain=gain
        print(self.name+" gained "+str(self.gain)+" health.")
    def knock_out(self):
        self.is_knocked_out="yes"
        return self.name+" was knocked out."
    def revive_knock_out(self):
        print(self.name+" was revived.")
    def attack(self,target):
        if self.is_knocked_out=="no":
            if target.current_health - self.level > 0:
                if self.type==target.type:
                    target.current_health=target.current_health - self.level
                    return "damage dealt is: "+str(self.level)+"\n"+target.lose_health(self.level)
                elif (self.type=="grass" and target.type=="fire") or (self.type=="fire" and target.type=="water") or (self.type=="water" and target.type=="grass"):
                    target.current_health = target.current_health - self.level/2
                    return "damage dealt is: "+str(self.level/2)+"\n"+target.lose_health(self.level/2)
                elif (self.type=="fire" and target.type=="grass") or (self.type=="grass" and target.type=="water") or (self.type=="water" and target.type=="fire"):
                    target.current_health = target.current_health - self.level*2
                    return "damage dealt is: "+str(self.level*2)+"\n"+target.lose_health(self.level*2)
            else:
                target.current_health=0
                return target.knock_out()
        else:
            return "Knocked out pokemons can't attack"

class Trainer:

    hp_potion=25

    def __init__(self,name,potions,pokemon_list,cur_act_pokemon):

        self.name=name
        self.potions=potions
        self.pokemon_list=pokemon_list
        self.active_pokemon=pokemon_list[cur_act_pokemon]

    def use_potion(self):

        if self.potions>0:
            self.potions-=1
            if self.active_pokemon.current_health > self.active_pokemon.maximum_health - self.hp_potion:
                self.active_pokemon.current_health=self.active_pokemon.maximum_health
            else:
                self.active_pokemon.current_health+=self.hp_potion
            print(str(self.active_pokemon.name) + " restored his health to: " + str(self.active_pokemon.current_health))
        else:
            print("No potions left,cant heal the pokemon")

    def attack_trainer(self,target_trainer):
        print(str(self.active_pokemon.name)+" attacked "+str(target_trainer.active_pokemon.name))
        print(self.active_pokemon.attack(target_trainer.active_pokemon))

    def switch_active_pokemon(self,new_pokemon):
        if self.pokemon_list[new_pokemon].is_knocked_out=="no":
            self.active_pokemon=self.pokemon_list[new_pokemon]
            print("Active pokemon switched to: "+str(self.active_pokemon.name))
        else:
            print("Can't switch to knocked out pokemon")

class Charmeleon(Pokemon):
    def __init__(self,level,maximum_health,current_health,is_knocked_out):
        super().__init__("Charmeleon",level,"fire",maximum_health,current_health,is_knocked_out)

class Seadra(Pokemon):
    def __init__(self,maximum_health,current_health,is_knocked_out):
        super().__init__("Seadra",32,"water",maximum_health,current_health,is_knocked_out)


#Pokemons
bulbasaur=Pokemon("Bulbasaur",8,"grass",64,64,"no")
venusaur=Pokemon("Venusaur",32,"grass",236,236,"no")
charmeleon=Charmeleon(16,142,142,"no")
squirtle=Pokemon("Squirtle",8,"water",63,63,"no")
vulpix=Pokemon("Vulpix",8,"fire",60,60,"no")
seadra=Seadra(154,154,"no")

#Trainers
ash=Trainer("Ash",3,[bulbasaur,charmeleon,squirtle],1)
misty=Trainer("Misty",3,[venusaur,vulpix,seadra],2)

misty.attack_trainer(ash)
print(ash.active_pokemon.current_health)
misty.attack_trainer(ash)
print(ash.active_pokemon.current_health)
misty.attack_trainer(ash)
print(ash.active_pokemon.current_health)
ash.attack_trainer(misty)
ash.switch_active_pokemon(0)
print(ash.active_pokemon.name)
ash.switch_active_pokemon(1)
print(ash.active_pokemon.name)





