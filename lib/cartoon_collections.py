def roll_call_dwarves(dwarfs):
    for i,dwarf in enumerate(dwarfs):
        print(f"{i+1}. {dwarf}")
    pass

def summon_captain_planet(strings):
    return [string.capitalize() + "!" for string in strings]
    pass

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4 :
            return True
    return False
    pass

def find_the_cheese(arr):
    cheeses = {
        "cheddar": True,
        "gouda": True,
        "camembert": True,
    }
    for item in arr:
        if item in cheeses:
            return item
    return None
    pass
