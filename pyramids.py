# The function, longest_slide_down(), takes an array representing possible distances from one level to the next of a pyramid and finds the longest possible path from the top to the bottom that one could take by sliding (you can only move one space over left or right from one level to the next).
# This is not the most efficient solution but is an accurate representation of my current programming skills (November 2017). I worked on this solution entirely on my own.

def longest_slide_down(pyramid):
    def longest_path(pyramid, index):
        if len(pyramid) == 1:
            return(pyramid[0][0])
        else:
            if index == 0:
                return(pyramid[len(pyramid) - 1][index] + longest_path(pyramid[0:len(pyramid) - 1], index = 0))
            elif index == len(pyramid[(len(pyramid) - 1)]) - 1:
                return(pyramid[len(pyramid) - 1][index] + longest_path(pyramid[0:len(pyramid) - 1], index = len(pyramid[(len(pyramid) - 1)]) - 2))
            else:
                choices = []
                left_choice = pyramid[len(pyramid) - 1][index] + longest_path(pyramid[0:len(pyramid) - 1], index - 1)
                right_choice = pyramid[len(pyramid) - 1][index] + longest_path(pyramid[0:len(pyramid) - 1], index)
                choices.append(left_choice)
                choices.append(right_choice)
                return(max(choices))
    distances = []
    for i in range(len(pyramid[len(pyramid) - 1])):
        distances.append(longest_path(pyramid, i))
    return(max(distances))
