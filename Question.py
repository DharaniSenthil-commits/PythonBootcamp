from QuestionPromt import Question

QuestionList=[
    "what is colour of sky ? \n a)Red \n b)Blue \n c)pink \n",
    "what is colour of banana ? \n a)yellow \n b)Blue \n c)pink \n",
    "what is colour of orange ? \n a)Red \n b)Blue \n c)orange \n"
]

QuestionObject=[
    Question(QuestionList[0],'b'),
    Question(QuestionList[1],'a'),
    Question(QuestionList[2],'c')

]

def run_quiz(QuestionObject) :
    Score=0
    for question in QuestionObject :
        Answer=input(question.Question)
        if(Answer == question.Answer):
            Score +=1
    print("You got "+str(Score)+"/"+ str(len(QuestionObject)) + " correct")

run_quiz(QuestionObject)