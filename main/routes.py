from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Movie

# Crear el blueprint para las rutas principales
bp = Blueprint('main', __name__)

# Ruta de la página principal
@bp.route('/')
@bp.route('/index')
def index():
    # Por ejemplo, mostrar las películas más recientes
    movies = Movie.query.order_by(Movie.created_at.desc()).limit(10).all()
    return render_template('main/index.html', title='Inicio', movies=movies)

# Ruta para mostrar todas las películas
@bp.route('/movies')
def movies():
    page = request.args.get('page', 1, type=int)
    movies = Movie.query.paginate(page=page, per_page=12)
    return render_template('main/movies.html', title='Películas', movies=movies)

# Ruta para buscar películas
@bp.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('main.index'))
    
    movies = Movie.query.filter(Movie.title.contains(query)).all()
    return render_template('main/search_results.html', title='Resultados', query=query, movies=movies)

# Ruta para la página "Acerca de"
@bp.route('/about')
def about():
    return render_template('main/about.html', title='Acerca de PopcornHour')