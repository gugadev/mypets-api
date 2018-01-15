from helpers.db import local_connect
from models.pet import Pet

class PetService:
  def __init__(self):
    self.db = local_connect()
  
  def all(self):
    rows = self.db.query_file("sql/getall.sql")
    pets = []
    for row in rows:
      pets.append(
        Pet(
          name=row.name,
          breed=row.breed,
          age=row.age,
          weight=row.weight,
          photo=row.photo
        )
      )
    return pets

  def create(self, pet):
    tx = self.db.transaction()
    self.db.query_file(
      "sql/insert.sql",
      name=pet.name, breed=pet.breed, age=pet.age, weight=pet.weight, photo=pet.photo
    )
    tx.commit()
    return True
  