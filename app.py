from flask import Flask, render_template, request ,url_for,flash
import requests

app = Flask(__name__)
app.secret_key='tu_clave_secreta'
API="https://pokeapi.co/api/v2/pokemon/"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/pokemon")
def pokemon():
    pokemon_name=request.form.get('pokemon_name')
    
    if not pokemon_name: 
        flash('por favor, ingresa un nombre')
    return redirect(url_for('inicio'))
try:
    resp=request.get(f"{API}{pokemon_name}")
if resp.status


if __name__ == "__main__":
    app.run(debug=True)