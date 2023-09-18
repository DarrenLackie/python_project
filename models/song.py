from app import db

class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    album = db.Column(db.String(255))
    running_time = db.Column(db.Integer)
    setlists = db.relationship("SetListItem", backref="song")

    def __repr__(self):
        return f"<Song {self.id}: Title {self.title}: Album {self.album}: Song Length {self.running_time}>"