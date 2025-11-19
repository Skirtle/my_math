from dataclasses import dataclass, field, InitVar
from typing import Optional
from random import seed as rand_seed, shuffle as rand_shuffle

@dataclass
class Card:
    rank: str
    suit: str
    value: int = 0
    
    def __init__(self, rank: str, suit: str, value: int = 0):
        self.rank = str(rank)
        self.suit = str(suit)
        self.value = value
        
    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"
    
    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"
    
    def __eq__(self, other: object) -> bool:
        if (not isinstance(other, Card)): return NotImplemented
        return self.rank == other.rank and self.suit == other.suit
        
@dataclass
class Deck:
    STANDARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    STANDARD_SUITS = [x for x in "SDCH"]
    STANDARD_VALUES = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11 }
    STANDARD_PLUS_VALUES = { "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14 }
    
    # Optional arguments
    cards: list[Card] = field(default_factory = list)
    # post_init arguments
    deck_style: InitVar[str] = "s"
    custom_values: InitVar[Optional[dict]] = None
    include_jokers: InitVar[int] = 0
    do_post_init: InitVar[bool] = True
    
    def __post_init__(self, deck_style: str, custom_values: Optional[dict], include_jokers: int = 0, do_post_init: bool = True) -> None:
        if (not do_post_init): return
        
        # Set up variables
        deck_style = deck_style.lower()
        allowed_styles = [
            "s", # Standard deck, Face value = 10, ace = 11
            "s+", # Standard plus, J = 11, Q = 12, K = 13, A = 14
            "c", # Custom style, must implement custom_values dict. Any card not given a value in custom_values with use the Standard card's value
            "", # No values assigned
            None # No values assigned
        ] # Any style not in this list will result in an error
        if (custom_values == None): custom_values = self.STANDARD_VALUES
        
        for i in range(include_jokers):
            self.cards.append(Card("JOKER", "RED" if i % 2 == 0 else "BLACK"))
        
        if (deck_style == "s"): chosen_style = self.STANDARD_VALUES
        elif (deck_style == "s+"): chosen_style = self.STANDARD_PLUS_VALUES
        elif (deck_style == "c"): chosen_style = custom_values
        else: raise NotImplementedError(f"Deck style {deck_style} not implemented. Allowed styles are 's' for Standard, 's+' for Standard plus, and 'c' for custom")
            
        for suit in self.STANDARD_SUITS:
            for rank in self.STANDARD_RANKS:
                # Check if rank exists
                if (rank not in chosen_style):
                    self.cards.append(Card(rank, suit, self.STANDARD_VALUES[rank]))
                    continue
                
                # If it does exist, use it
                self.cards.append(Card(rank, suit, chosen_style[rank]))
    
    def __str__(self) -> str:
        s = "["
        for index,c in enumerate(self.cards):
            s += f"{c.rank}{c.suit}"
            if (index != len(self.cards) - 1):
                s += ","
        return s + "]"
       
    def __len__(self) -> int:
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)
    
    def peek_top(self) -> Card:
        return self.cards[0]
    
    def peek_bottom(self) -> Card:
        return self.cards[len(self.cards) - 1]
    
    def pop_top(self) -> Card:
        card = self.cards.pop(0)
        return card
    
    def pop_bottom(self) -> Card:
        card = self.cards.pop()
        return card
    
    def push_top(self, card: Card) -> None:
        self.cards.insert(0, card)
    
    def push_bottom(self, card: Card) -> None:
        self.cards.append(card)
    
    def shuffle(self, seed = None) -> None:
        rand_seed(seed)
        rand_shuffle(self.cards)
        
    def split(self, n = 2, discard_excess: bool = False) -> list["Deck"]:
        # Determine initial card counts
        arr = []
        cards_per_person = [len(self) // n for i in range(n)]
        extra_cards = len(self) % n
        
        person = 0
        # Determine if players get extra cards
        while (extra_cards > 0 and not discard_excess):
            cards_per_person[person] = cards_per_person[person] + 1
            extra_cards -= 1
            person += 1
        
        # Give each player their cards
        cards_split = 0
        for index,card_count in enumerate(cards_per_person):
            arr.append(Deck(self.cards[cards_split:cards_split + card_count], do_post_init = False))
            cards_split += card_count
        
        # Any excess cards get their own deck
        if (extra_cards > 0): arr.append(Deck(self.cards[cards_split:], do_post_init = False))
        
        return arr
    
    def has(self, suit: str = None, rank: str = None) -> bool:
        if (suit == None and rank == None): return len(self) != 0 # A deck with nothing cannot have anything. A deck with cards can have 'nothing'

        for card in self:
            if (card.suit == suit or suit == None):
                if (card.rank == rank or rank == None):
                    return True
        return False

    def sort(self, mode: str = "rank") -> None:
        mode = mode.lower()
        # When mode is rank, sort by rank first, then by suit
        # When mode is suit, sort by suit first, then by rank
        if (mode == "rank"):
            self.cards.sort(key = lambda c: c.suit)
            self.cards.sort(key = lambda c: c.value, reverse = True)
        elif (mode == "suit"):
            self.cards.sort(key = lambda c: c.value, reverse = True)
            self.cards.sort(key = lambda c: c.suit)
        else:
            raise NotImplementedError(f"Sorting mode '{mode}' not implemented. Only 'rank' and 'suit' are allowed.")

    def get_cards(self, rank: str = None, suit: str = None) -> list[Card]:
        cards = []
        for card in self:
            if (card.rank != rank and rank != None): continue
            if (card.suit != suit and suit != None): continue

            cards.append(card)

        return cards

    def get_card_counts(self) -> dict[str,int]:
        counts = {}
        for rank in self.STANDARD_RANKS:
            cards_of_rank = self.get_cards(rank = rank)
            counts[rank] = len(cards_of_rank)
        
        for suit in self.STANDARD_SUITS:
            cards_of_suit = self.get_cards(suit = suit)
            counts[suit] = len(cards_of_suit)

        return counts

def get_hands(deck: Deck) -> list[str]:
    # Royal flush, straight flush, 4OAK, Full house, straight, 3OAK, 2 pair, pair, high card
    # Returns a list of valid hands the deck has, sorted from highest ranking hand to lowest
    hands = []
    counts = deck.get_card_counts()
    has_4, has_3, has_2 = False, False, False
    has_flush, has_straight, has_rf = False, False, False

    # 4, 3, and 2 of a kind
    for rank in deck.STANDARD_RANKS:
        if (counts[rank] >= 4): has_4 = True
        if (counts[rank] >= 3): has_3 = True
        if (counts[rank] >= 2): has_2 = True

    # Flush logic
    for suit in deck.STANDARD_SUITS:
        if (counts[suit] >= 5): 
            has_flush = True
            break

    # Royal flush logic
    for suit in deck.STANDARD_SUITS:
        for rank in ["A", "K", "Q", "J", "10"]:
            if (not deck.has(suit, rank)):
                break
        else:
            has_rf = True
            break

    # Straight logic
    # TODO - do it

    # rf - Royal flush - A-10 straight flush
    if (has_rf): hands.append("rf")

    # sf - Straight flush - Any straight, same suit
    

    # 4oak - 4 of a kind - 4 cards of the same rank
    if (has_4): hands.append("4oak")
    
    # fh - Full house - 3 of a kind of one rank and a 2 of a kind of another rank
    found_2, found_3 = False, False
    for rank in deck.STANDARD_RANKS:
        if (counts[rank] >= 3 and not found_3):
            found_3 = True
        elif (counts[rank] >= 3):
            found_2 = True # We found 3+ and a different 3+, which counts as 2

        elif (counts[rank] >= 2):
            found_2 = True

        if (found_3 and found_2): 
            hands.append("fh")
            break

    #  f - flush - 5 cards of the same suit
    if (has_flush): hands.append("f")

    # s - Straight - 5 cards in a where each card is sequential (A K Q J 10 9 8 7 6 5 4 3 2 A), does not wrap around
    if (has_straight): hands.append("s") # TODO - Implement logic

    # 3oak - 3 of a kind - 3 cards of the same rank
    if (has_3): hands.append("3oak")
    
    # 2p - Two pair - 2 cards of the same rank
    if (has_2): hands.append("2p")
    
    # hc - High card - Just a card
    if (len(deck) > 0): hands.append("hc") # High card, always a hand if the deck has at least one card
    return hands

def create_deck_from_string(str_cards: list[str], deck_style: str = "s", custom_values: dict = None, include_jokers: int = 0) -> Deck:
    cards = []
    for str_card in str_cards:
        if (len(str_card) == 3):
            rank = str_card[:2]
            suit = str_card[2:]
        else:
            rank = str_card[0]
            suit = str_card[1]
        
        card = Card(rank, suit)
        cards.append(card)

    print(cards)
    deck = Deck(deck_style = deck_style, custom_values = custom_values, include_jokers = include_jokers, do_post_init = False)
    for card in cards:
        deck.push_bottom(card)
    
    return deck