import base64
from sanic import Blueprint
from sanic.response import json
from models.pet import Pet
from services.pet import PetService

pets = Blueprint("pets", url_prefix="/pets")


@pets.route("/", methods=["GET"])
async def index(request):
    service = PetService()
    pets = service.all()
    return json(pets)


@pets.route("/create", methods=["POST"])
async def create(request):
    service = PetService()
    photo = request.files.get("photo")
    pet = Pet(
        name=request.form.get("name"),
        breed=request.form.get("breed"),
        age=int(request.form.get("age")),
        weight=float(request.form.get("weight")),
        photo=base64.encodebytes(photo.body).decode("utf-8").replace("\n", "")
    )
    service.create(pet)
    return json(pet)
