from sanic import Sanic
from handlers.pet import pets

app = Sanic()

# Registro de blueprints
app.blueprint(pets)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
