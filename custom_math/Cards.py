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