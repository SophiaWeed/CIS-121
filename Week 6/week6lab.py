def hailstone(n):
    hailstone_list = []
    while n > 1:
        if n%2 == 0:
            n /= 2
            hailstone_list.append(n)
        else:
            n = (3*n+1)
            hailstone_list.append(n)
    return hailstone_list

print(hailstone(17))

# In blackjack, cards are counted as -1, 0, 1. 2-6 are counted as 1,
#  7-9 are 0, and 10,j,q,k,a are counted as -1

#Write a function that takes a list called cards, counts the number, and returns it from the list of
#cards provided.

def blackjack_score(card_list):
    score = 0
    for card in card_list:
        if str(card) in ["2", "3", "4", "5", "6"]:
            score += 1
        elif str(card) in ["10", "j", "q", "k", "a"]:
            score -= 1
    print(score)

cards = [2, 8, "k"]

blackjack_score(cards)


def is_acronym(s,words):
    combined_letters = ""
    # if s == first letters of words concatonated return true
    if len(s) != len(words):
        return False
    else:
        for word in words:
            if word == "":
                return False
            first_letter = word[0]
            combined_letters += first_letter
        if combined_letters != s:
            return False
        return True
        
words = ["the", "fuck's", "sake"]
s = "tfs"
print(is_acronym(s,words))
        
            

# compare the length of the strin and words
# first_letter = word[0]


        
