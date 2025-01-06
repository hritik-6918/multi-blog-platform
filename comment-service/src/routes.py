from flask import request, jsonify
from src.app import app, db
from src.models import Comment

@app.route('/comments/', methods=['POST'])
def create_comment():
    data = request.get_json()
    post_id = data.get('post_id')
    user_id = data.get('user_id')
    text = data.get('text')

    if not post_id or not user_id or not text:
        return jsonify({"message": "post_id, user_id, and text are required"}), 400

    new_comment = Comment(post_id=post_id, user_id=user_id, text=text)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully"}), 201

@app.route('/comments', methods=['GET'])
def list_comments():
    post_id = request.args.get('post_id', type=int)
    if not post_id:
         return jsonify({"message": "post_id is required"}), 400

    comments = Comment.query.filter_by(post_id=post_id).all()
    result = []
    for comment in comments:
        result.append({
           'id': comment.id,
           'post_id': comment.post_id,
           'user_id': comment.user_id,
           'text': comment.text,
           'created_at': comment.created_at
       })
    
    return jsonify({"comments": result}), 200