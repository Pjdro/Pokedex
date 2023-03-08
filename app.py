from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

# Main Pokemon lookup
@app.route("/pokemon", methods=['GET', 'POST'])
def pokemon():
    if request.method == "POST":
        pokemon_name = request.form["pokemon_name"]
        if not pokemon_name:
            error_message = 'Plese enter a name or number'
            return render_template("index.html", error_message=error_message)
        # Stores the response using the API
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/')
        if response.ok:
            # If response is not null, codifies it into a dictionary using json
            pokemon_data = response.json()
            return render_template('pokemon.html', pokemon=pokemon_data)
        else:
            # Else, prints an error message
            error_message = f'Pokemon {pokemon_name} not found!'
            return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html")
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("/register.html")
    else:
        if not request.form.get("username"):
            error_message = 'Plese enter a username'
            return render_template("/register.html", error_message=error_message)
        elif not request.form.get("password") or not request.form.get("confirmation"):
            error_message = 'Plese enter a password'
            return render_template("/register.html", error_message=error_message)



if __name__ == "main":
    app.run(debug=True)