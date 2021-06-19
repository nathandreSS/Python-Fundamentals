import sys
from src.auction.exceptions import InvalidBid


class User:

    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def bid(self, value, auction):
        self._check_funds(value)
        user_bid = Bid(self, value)
        auction.bid(user_bid)
        self.__wallet -= value

    def __str__(self):
        return self.__name

    def _check_funds(self, value):
        if value > self.__wallet:
            raise InvalidBid('Saldo insuficiente!')


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value

    def __str__(self):
        return f'{self.user} deu um lance de {self.value}'


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.smallest_bid = sys.float_info.max
        self.biggest_bid = sys.float_info.min

    def bid(self, bid):
        if self._validate_bid(bid):
            if bid.value > self.biggest_bid:
                self.biggest_bid = bid.value
            if bid.value < self.smallest_bid:
                self.smallest_bid = bid.value
            self.__bids.append(bid)

    @property
    def bids(self):
        return self.__bids[:]

    def _validate_bid(self, bid):
        return self._no_bids() or (self._user_is_differente_from_the_last_bid(bid)
                                   and self._bid_amount_is_greater_than_the_last(bid))

    def _no_bids(self):
        return not self.__bids

    def _user_is_differente_from_the_last_bid(self, bid):
        if not self.__bids[-1].user != bid.user:
            raise InvalidBid('O usuário não pode dar dois lances seguidos!')
        return True

    def _bid_amount_is_greater_than_the_last(self, bid):
        if not self.__bids[-1].value < bid.value:
            raise InvalidBid('O valor do lance deve ser maior do que o último!')
        return True