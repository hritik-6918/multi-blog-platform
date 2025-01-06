from flask import request, jsonify
from src.app import app, db
from src.models import Blog

@app.route('/blogs/', methods=['POST'])
def create_blog():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author_id = data.get('author_id')

    if not title or not content or not author_id:
        return jsonify({"message": "Title, content, and author_id are required"}), 400

    new_blog = Blog(title=title, content=content, author_id=author_id)
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({"message": "Blog post created successfully"}), 201

@app.route('/blogs/', methods=['GET'])
def list_blogs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    blogs = Blog.query.paginate(page=page, per_page=per_page)
    result = []
    for blog in blogs.items:
        result.append({
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author_id': blog.author_id,
            'created_at': blog.created_at,
            'updated_at': blog.updated_at
        })
    return jsonify({
        "items": result,
        "page": blogs.page,
        "total_pages": blogs.pages,
        "total_items": blogs.total
        }), 200

@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog:
        return jsonify({
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author_id': blog.author_id,
            'created_at': blog.created_at,
            'updated_at': blog.updated_at
        }), 200
    else:
        return jsonify({"message": "Blog post not found"}), 404


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify({"message": "Blog post not found"}), 404
    
    data = request.get_json()
    blog.title = data.get('title', blog.title)
    blog.content = data.get('content', blog.content)
    blog.author_id = data.get('author_id', blog.author_id)

    db.session.commit()
    return jsonify({"message": "Blog post updated successfully"}), 200

@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog:
        db.session.delete(blog)
        db.session.commit()
        return jsonify({"message": "Blog post deleted successfully"}), 200
    else:
        return jsonify({"message": "Blog post not found"}), 404