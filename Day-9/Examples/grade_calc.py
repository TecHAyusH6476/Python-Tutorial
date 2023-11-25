# module - we need to create a method or function
# where we will be calc. grades , average , feedback

# Falsy values in python
# undefined -> False
# null -> False
# "" -> False


def calc_average(scores):  # scores is a list  [45,34,45,12,34]
    # we have to see edge or corner case
    if not scores:
        return 0
    else:
        return sum(scores) / len(scores)


def calc_grade(avg_score):  # avg_score is a number
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 65:
        return "C"
    else:
        return "D"


def provide_feedback(avg_score):
    if avg_score >= 90:
        return "Good Work!"
    elif avg_score >= 75:
        return "You are doing well!"
    else:
        return "you passed but there is room for imp.."
