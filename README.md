qa.api.app
---

API for question 

### use URL for API
http://qaapi.us-east-1.elasticbeanstalk.com/

---
#### Get all question


http://qaapi.us-east-1.elasticbeanstalk.com/question

Outcome:
```
"success": true, 
    "questions": [
        {
            "id": 1,
            "quistion_title": "How to be good in programming?"
        },
        {
            "id": 2,
            "quistion_title": "How to be good in programming?"
        },
        {
            "id": 3,
            "quistion_title": "What is python?"
        }
    ],
    "total_question": 3
}
```

---
#### Post new question


http://qaapi.us-east-1.elasticbeanstalk.com/question/create

JSON body
```
{
   "question": "What is python?"
}
```

Outcome:
```
{
    "success": true,
    "question": [
        {
            "id": 4,
            "quistion_title": "What is python?"
        }
    ]
}
```

---
#### Post new answer


http://qaapi.us-east-1.elasticbeanstalk.com/answer/2

JSON body
```
{
   "answer": "it is language of brogramming"
}
```

Outcome:
```
{
    "success": true,
    "answer": [
        {
            "id": 2,
            "quistion_id": 2,
            "answer": "it is language of brogramming"
        }
    ]
}

---
#### Post tag


http://qaapi.us-east-1.elasticbeanstalk.com/tag/1

JSON body
```
{
   "tag": "python"
}
```

Outcome:
```
{
    "success": true,
    "tag": [
        {
            "id": 6,
            "tag_title": "python"
        }
    ]
}
```

---
#### Post comment


http://qaapi.us-east-1.elasticbeanstalk.com/comment/1

JSON body
```
{
   "comment": "programming language"
}
```

Outcome:
```
{
    "success": true,
    "comment": [
        {
            "id": 3,
            "comment_title": "programming language",
            "answer_id": 1
        }
    ]
}
```
---
#### Get all answers of question


http://qaapi.us-east-1.elasticbeanstalk.com/question/1

Outcome:
```
{
    "success": true,
    "id": 1,
    "quistion_title": "How to be good in programming?",
    "answers": [
        {
            "id": 1,
            "quistion_id": 1,
            "answer": "write more code"
        }
     ]
}
```
---
#### Get all comment of answer


http://qaapi.us-east-1.elasticbeanstalk.com/comment/1

Outcome:
```
success": true,
    "id": 1,
    "answer": "write more code",
    "comments": [
        {
            "id": 1,
            "comment_title": "with small projects",
            "answer_id": 1
        },
        {
            "id": 2,
            "comment_title": "with small projects",
            "answer_id": 1
        },
        {
            "id": 3,
            "comment_title": "programming language",
            "answer_id": 1
        }
    ]
}
```

---
#### Get all tags based in question


http://qaapi.us-east-1.elasticbeanstalk.com/tag/3

Outcome:
```
{
    "success": true,
    "id": 3,
    "question": "What is python?",
    "taq": [
        {
            "id": 6,
            "tag_title": "python"
        }
    ]
}
```
