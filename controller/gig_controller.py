from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gig import Gig
from models.setlist import Setlist
from models.song import Song
from app import db

gigs_blueprint = Blueprint("gigs", __name__)

@gigs_blueprint.route('/gigs')
def all_gigs():
    returned_gigs = Gig.query.all()
    return render_template('/gigs/index.jinja', gigs=returned_gigs)

@gigs_blueprint.route("/gigs/<id>")
def show_gig(id):
    selected_gig = Gig.query.get(id)
    selected_songs = Song.query.join(Setlist).filter(Setlist.gig_id == id)
    return render_template("gigs/show_gig.jinja", gig=selected_gig, songs=selected_songs)