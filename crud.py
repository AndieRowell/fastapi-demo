from sqlalchemy.orm import Session, aliased, joinedload
from models import Hero, Ability, AbilityType, Relationship, RelationshipType
from schemas import HeroModel

def get_heroes_v1(db: Session):
    # set variable to store the query info
    heroes_query = (
        db.query(Hero).all()
    )
    return heroes_query

def get_heroes(db: Session):
    # set variable to store the query info
    heroes_query = (
        db.query(Hero)
        # .where(Hero.id == 6) #use to get the hero id 6 only instead of sql
        # .filter(Hero.name == "Lieutenant Lidar") #return the data just for lidar
        # .join(Hero.abilities)
        .options(joinedload(Hero.abilities).joinedload(Ability.ability_types))
        .all()
    )
    return heroes_query
