"""

This file is written by Rebecca Hanlon.  Lab assignment to build a Voting App.

"""


import chalk



def display_ballot(candidates):
    """
    Prints the ballot dict.  Uses dict() 1.
    
    :param candidates: dict
    :return: None
    """

    print('Here are your candidates for President of the Gecko Federation: ', end='\n')

    for index, key in enumerate(candidates, start=1):
        chalk.yellow(str(index) + '------> ' + key)



# def add_to_cands(i_choose, candidates):
#     """
#     Adds the votes to the appropriate candidate and keep total.
#
#     >>> test_cands = {'Candi': 0, 'Bambi': 0, 'Timi': 0, "Bobi": 0,}
#
#     >>> add_to_cands('Bambi', test_cands)
#     {'Candi': 0, 'Bambi': 1, 'Timi': 0, 'Bobi': 0}
#
#     >>> add_to_cands('Timi', test_cands)
#     {'Candi': 0, 'Bambi': 1, 'Timi': 1, 'Bobi': 0}
#
#     >>> add_to_cands('Timi', test_cands)
#     {'Candi': 0, 'Bambi': 1, 'Timi': 2, 'Bobi': 0}
#
#     :param choice:
#     :param candidates:
#     :return:
#     """
#
#
#     return candidates


# def vote_tally(candidates):
#     """
#     Print out the total votes for each candidate.  Print out the winner with the most votes.
#
#
#     :return:
#     """
#
#     print(f"Total votes per candidate:" + str(candidates))
#     quit()


def input_is_valid(i_choose):
    """
    Validating input.  Kept, may use at a later date.
    :param i_choose: dict
    :return: True
    """
    return True


def candidate_input(candidates):
    """
    Presents the list of candidates, asks user to vote until done, prints the results of the voting.
    
    :param candidates: dict
    :return: 
    """
    options = {index: goof for index, goof in enumerate(candidates, start=1)}

    while True:
        display_ballot(candidates)
        i_choose = input("Enter your choice for President or type 'done' to see the results. ➙  ")

        try:
            i_choose = int(i_choose)

        except ValueError:

            if i_choose == 'done':
                chalk.cyan(f"Total votes per candidate: {candidates}")
                winner = max(candidates.items(), key=lambda t: t[-1])
                chalk.magenta(f"The winner is {winner[0]} with {winner[1]} votes.")
                break

            chalk.red('Please enter the number to the left of the name.')
            continue

        if input_is_valid(i_choose):

            choice = options[i_choose]

            candidates[choice] += 1


if __name__ == '__main__':

    test_candidates = {'Dolby-Doo': 0,
                    'Alphone-so': 0,
                    'Su-zetto': 0,
                    'Kiwi-si': 0,
                    'Oi-oh': 0,
                    'Demi-tree': 0}

    candidate_input(test_candidates)

