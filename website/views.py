from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Post, User
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        username = request.form.get('username') 
        text = request.form.get('text')

        if not username or not text:
            flash('Username and Post Text cannot be empty', category='error')
        else:
            post = Post(username=username, text=text, author_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create-post.html', user=current_user)


@views.route('/view-post/<int:id>')
@login_required
def view_post(id):
    post = Post.query.get(id)

    if not post:
        flash("Post does not exist.", category='error')
        return redirect(url_for('views.home'))

    return render_template('view-post.html', user=current_user, post=post)

