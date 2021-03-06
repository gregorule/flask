from application import app, db
from application.models import Games

@app.route('/add/<new_game_name>')
def add(new_game_name):
    new_game = Games(name=new_game_name)
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<old_name>/<new_name>')
def update(old_name, new_name):
    current_entry = Games.query.filter_by(name = old_name).first()
    current_entry.name = new_name
    db.session.commit()
    return current_entry.name

@app.route('/delete/<gname>')
def delete(gname):
    to_be_delete = .query.filter_by(name = gname).first()
    db.session.delete(to_be_delete)
    db.session.commit()
    return f"{to_be_delete} has been deleted"

@app.route('/total')
def total():
    total_games = Games.query.count()
    return str(total_games)
    