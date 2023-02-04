from flask import Blueprint, render_template,request
from apps.app import db
from apps.shiori.models import Itinerarys

shiori = Blueprint(
    "shiori",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@shiori.route("/")
def index():
    itinerarys = Itinerarys.query.all()
    return render_template("index.html", itinerarys=itinerarys)

@shiori.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        return render_template("register.html")
    else:
        return render_template("register.html")

