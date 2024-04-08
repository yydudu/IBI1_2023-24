#define a function to calculate it
def favorite_bond_actor(birth):
    bond_actors = {'Roger Moore': range(1973, 1987),'Timothy Dalton': range(1987, 1995),'Pierce Brosnan': range(1995, 2006),'Daniel Craig': range(2006, 2022)}
    year_turned_18 = birth + 18
    
    for actor, years in bond_actors.items():
        if year_turned_18 in years:
            return actor
    
    return "No Bond actor found for that year."

#example
print(favorite_bond_actor(1970))  

