import custom_math as c_math
from random import randint, seed as r_seed
from concurrent.futures import ProcessPoolExecutor


def play_war(p1: c_math.Deck, p2: c_math.Deck, max_rounds: int | None = None, war_card_count: int = 2, print_events: bool = False) -> tuple[int,int]:
    winning_size = len(p1) + len(p2)
    if (print_events): print(f"Starting War with {winning_size} cards total")
    
    round = 1
    # Go until any player has all the cards, or the round limit is reached
    while (len(p1) != winning_size and len(p2) != winning_size and round != max_rounds):
        if (print_events): 
            print(f"Round {round}: Player 1 has {len(p1)} card(s) left, player 2 has {len(p2)} card(s) left")
            if (max_rounds != None): print(f" {max_rounds - round} round(s) left")
            else: print()
        
        c1 = [p1.pop_top()]
        c2 = [p2.pop_top()]
        if (print_events): print(f"Player 1 reveals {c1[-1]} ({c1[-1].value}), player 2 reveals {c2[-1]} ({c2[-1].value})")
        
        while (c1[-1].value == c2[-1].value):
            # Each player adds the next 2 cards of their decks to their piles
            # This continues until the last revealed cards are not the same, or a player runs out of cards
            if (len(p1) < war_card_count and len(p2) < war_card_count):
                if (print_events): print("Both players managed to run out of cards. Tie")
                break
            elif (len(p1) < war_card_count):
                if (print_events): print("Plauer 1 has run out of cards, player 2 wins")
                break
            elif (len(p2) < war_card_count):
                if (print_events): print("Plauer 2 has run out of cards, player 1 wins")
                break
            for i in range(war_card_count):
                c1.append(p1.pop_top())
                c2.append(p2.pop_top())
            if (print_events): print(f"\tPlayer 1 reveals {c1[-1]} ({c1[-1].value}), player 2 reveals {c2[-1]} ({c2[-1].value})")
        
        top_c1 = c1[-1].value
        top_c2 = c2[-1].value
        if (top_c1 > top_c2):
            for card in (c2 + c1): 
                p1.push_bottom(card)
        else:
            for card in (c1 + c2): 
                p2.push_bottom(card)
            
        round += 1
        
    if (print_events): print(f"Player 1 {len(p1)}, player 2 {len(p2)}")
    return (1 if len(p1) > len(p2) else 2, round)

def worker(seed_start, seed_end):
    p1_wins = 0
    p2_wins = 0
    longest_round = 0
    longest_seed = None
    shortest_round = 1e9
    shortest_seed = None
    
    for seed in range(seed_start, seed_end):
        r_seed(None)
        deck = c_math.Deck(deck_style = "s+")
        deck.shuffle(seed)
        s_deck = deck.split()
        
        player_1, player_2 = s_deck[0], s_deck[1]
        
        winner, length = play_war(player_1, player_2)
        
        if (winner == 1): p1_wins += 1
        else: p2_wins += 1
        
        if (length >= longest_round):
            longest_round = length
            longest_seed = seed
            
        if (length <= shortest_round):
            shortest_round = length
            shortest_seed = seed
        
    # print(f"{id} - Out of {n:,} rounds, player 1 won {p1_wins:,} and player 2 won {p2_wins:,}.\nThe longest round was {longest_round:,} rounds (seed = {longest_seed}). The shortest round was {shortest_round:,} rounds (seed = {shortest_seed}). ")
    return (seed_end - seed_start, p1_wins, p2_wins, longest_round, longest_seed, shortest_round, shortest_seed)

if __name__ == "__main__":
    cards = ["AS", "KS", "QS", "JS", "10S"]
    deck = c_math.create_deck_from_string(cards)
    print(deck)
    print(c_math.get_hands(deck))