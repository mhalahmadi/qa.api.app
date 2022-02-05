
import os
from flask import (
    Flask,
    request,
    abort,
    jsonify
)
from sqlalchemy.orm import  Session

from flask_sqlalchemy import SQLAlchemy
from models import Tag, db, Comment, Answer,Question, setup_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    setup_db(app)
    


    QUESTIONS_PER_PAGE = 10

    def pagination(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        formated_page = [api.format() for api in selection]
        current = formated_page[start:end]

        return current

    #application index
    @app.route('/')
    def index():
        return jsonify({
        'success': True,
        'application': 'Question'
        })
  
   
    #Get all question
    @app.route('/question', methods=['GET'])
    def get_question():
        questions= Question.query.all()
        formated_questions = pagination(request, questions)

        if len(formated_questions) == 0:
            abort(404)

        return jsonify({
        'success': True,
        'questions': formated_questions,
        'total_question': len(Question.query.all())
    })

    #create new question
    @app.route('/question/create', methods=['POST'])
    def create_question():
        body = request.get_json(force=True)
        create_question = body.get('question')

        questions = Question(
                            quistion_title=create_question
                            )

        if create_question =='':
            abort(404)

        questions.insert()
        
        question =[Question.query.get(questions.id).format()]

        return jsonify({
        'success': True,
        'question': question,
    })

     #create answer based on question ID
    @app.route('/answer/<int:quistion_id>', methods=['POST'])
    def create_answer(quistion_id):
        body = request.get_json(force=True)
        create_answer = body.get('answer')
        quistion_id = quistion_id

        answers = Answer(
                            answer=create_answer,
                            quistion_id=quistion_id
                            )

        if create_answer =='':
            abort(404)

        answers.insert()
        

        answer =[Answer.query.get(answers.id).format()]

        return jsonify({
            'success': True,
            'answer': answer
            })


    #create tag based on question ID
    @app.route('/tag/<int:quistion_id>', methods=['POST'])
    def create_tag(quistion_id):
        body = request.get_json(force=True)
        create_tag = body.get('tag')
        questions = Question.query.filter_by(id=quistion_id).first_or_404()

     
        tags = Tag(
                    tag_title=create_tag
                )

        if create_tag =='':
            abort(404)

        questions.following.append(tags)

        tags.insert()
        

        tag =[Tag.query.get(tags.id).format()]

        return jsonify({
            'success': True,
            'tag': tag
            })



    #create new comment based on answer ID
    @app.route('/comment/<int:answer_id>', methods=['POST'])
    def create_comment(answer_id):
        body = request.get_json(force=True)
        comment_title= body.get('comment')
        answer_id = answer_id

        comments = Comment(
                            comment_title=comment_title,
                            answer_id=answer_id
                            )

        if comment_title =='':
            abort(404)

        comments.insert()
        
        comment =[Comment.query.get(comments.id).format()]

        return jsonify({
            'success': True,
            'comment': comment
            })

    #get all answers of question
    @app.route('/question/<int:quistion_id>', methods=['GET'])
    def get_question_answer(quistion_id):

        get_answers = db.session.query(Answer).join(Question).filter(Answer.quistion_id == Question.id).all()
        questions = Question.query.filter_by(id=quistion_id).first_or_404()
        formated_answers = pagination(request, get_answers)
        return jsonify({
            'success': True,
            'id': questions.id,
            'quistion_title': questions.quistion_title,
            'answers': formated_answers
         })


    #get all comment of answer
    @app.route('/comment/<int:answer_id>', methods=['GET'])
    def get_answer_comment(answer_id):

        get_comments = db.session.query(Comment).join(Answer).filter(Comment.answer_id == Answer.id).all()
        answers = Answer.query.filter_by(id=answer_id).first_or_404()
        formated_comments= pagination(request, get_comments)
        return jsonify({
            'success': True,
            'id': answers.id,
            'answer': answers.answer,
            'comments': formated_comments
         })


    #get all tags based in question
    @app.route('/tag/<int:question_id>', methods=['GET'])
    def get_tag_question(question_id):

        questions= Question.query.filter_by(id=question_id).first_or_404()
        tags= Tag.query.all()
        all_question= Question.query.filter_by(id=question_id).first().following
        formated_ags= pagination(request, all_question)
        return jsonify({
            'success': True,
            'id': questions.id,
            'question': questions.quistion_title,
            'taq': formated_ags
         })

    return app


app = create_app()

if __name__ == '__main__':
    app.run()