from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.movies import bp
from app.movies.forms import MovieForm, CommentForm, RatingForm, TopicForm, ReplyForm
from app.models import User, MovieSeries, Rating, Comment, ForumTopic, ForumReply, Favorite

@bp.route('/<int:id>')
def movie_detail(id):
    movie = MovieSeries.query.get_or_404(id)
    
    # Obtener calificaciones y comentarios
    ratings = Rating.query.filter_by(pelicula_id=id).all()
    comments = Comment.query.filter_by(pelicula_id=id).order_by(Comment.fecha.desc()).all()
    
    # Formularios
    comment_form = CommentForm()
    rating_form = RatingForm()
    
    # Verificar si el usuario ya ha calificado esta película
    user_rating = None
    if current_user.is_authenticated:
        user_rating = Rating.query.filter_by(usuario_id=current_user.id, pelicula_id=id).first()
    
    return render_template('movies/detail.html', title=movie.titulo,
                          movie=movie, ratings=ratings, comments=comments,
                          comment_form=comment_form, rating_form=rating_form,
                          user_rating=user_rating)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_movie():
    # Verificar que sea moderador
    if not current_user.is_moderator():
        flash('Solo los moderadores pueden añadir películas/series', 'danger')
        return redirect(url_for('main.index'))
    
    form = MovieForm()
    if form.validate_on_submit():
        movie = MovieSeries(
            titulo=form.titulo.data,
            anio=form.anio.data,
            genero=form.genero.data,
            duracion_min=form.duracion_min.data,
            director=form.director.data,
            reparto=form.reparto.data,
            sinopsis=form.sinopsis.data,
            imagen_url=form.imagen_url.data,
            creador_id=current_user.id
        )
        db.session.add(movie)
        db.session.commit()
        flash('Película/serie añadida correctamente', 'success')
        return redirect(url_for('movies.movie_detail', id=movie.id))
    
    return render_template('movies/create.html', title='Añadir Película/Serie', form=form)

@bp.route('/<int:id>/comment', methods=['POST'])
@login_required
def add_comment(id):
    movie = MovieSeries.query.get_or_404(id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = Comment(
            contenido=form.contenido.data,
            usuario_id=current_user.id,
            pelicula_id=id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comentario añadido correctamente', 'success')
    
    return redirect(url_for('movies.movie_detail', id=id))

@bp.route('/<int:id>/rate', methods=['POST'])
@login_required
def rate_movie(id):
    movie = MovieSeries.query.get_or_404(id)
    form = RatingForm()
    
    if form.validate_on_submit():
        # Verificar si ya existe una calificación
        existing_rating = Rating.query.filter_by(usuario_id=current_user.id, pelicula_id=id).first()
        
        if existing_rating:
            existing_rating.estrellas = form.estrellas.data
            flash('Calificación actualizada correctamente', 'success')
        else:
            rating = Rating(
                estrellas=form.estrellas.data,
                usuario_id=current_user.id,
                pelicula_id=id
            )
            db.session.add(rating)
            flash('Calificación añadida correctamente', 'success')
        
        db.session.commit()
    
    return redirect(url_for('movies.movie_detail', id=id))

@bp.route('/<int:id>/forum')
def forum(id):
    movie = MovieSeries.query.get_or_404(id)
    topics = ForumTopic.query.filter_by(pelicula_id=id).order_by(ForumTopic.fecha_creacion.desc()).all()
    
    return render_template('movies/forum.html', title=f'Foro - {movie.titulo}',
                          movie=movie, topics=topics)

@bp.route('/<int:id>/forum/create', methods=['GET', 'POST'])
@login_required
def create_topic(id):
    movie = MovieSeries.query.get_or_404(id)
    form = TopicForm()
    
    if form.validate_on_submit():
        topic = ForumTopic(
            titulo=form.titulo.data,
            contenido=form.contenido.data,
            usuario_id=current_user.id,
            pelicula_id=id
        )
        db.session.add(topic)
        db.session.commit()
        flash('Tema creado correctamente', 'success')
        return redirect(url_for('movies.forum', id=id))
    
    return render_template('movies/create_topic.html', title=f'Nuevo tema - {movie.titulo}',
                          movie=movie, form=form)

@bp.route('/<int:movie_id>/forum/<int:topic_id>')
def topic_detail(movie_id, topic_id):
    movie = MovieSeries.query.get_or_404(movie_id)
    topic = ForumTopic.query.get_or_404(topic_id)
    replies = ForumReply