from unittest import TestCase
from src.auction.exceptions import InvalidBid
from src.auction.domain import User, Bid, Auction


class TestAuction(TestCase):
    smallest_bid = 100.0
    biggest_bid = 150.0

    def setUp(self):
        self.nathan = User('Nathan', 2000)
        self.brunno = User('Brunno', 1500)

        self.nathan_bid = Bid(self.nathan, TestAuction.biggest_bid)
        self.brunno_bid = Bid(self.brunno, TestAuction.smallest_bid)

        self.auction = Auction('Notebook')

    def test_evaluate(self):
        self.auction.bid(self.brunno_bid)
        self.auction.bid(self.nathan_bid)

        self.assertEqual(TestAuction.smallest_bid, self.auction.smallest_bid,
                         f'The highest bid must be {TestAuction.smallest_bid}, but was {self.auction.smallest_bid}')
        self.assertEqual(TestAuction.biggest_bid, self.auction.biggest_bid,
                         f'The lowest bid must be {TestAuction.biggest_bid}, but was {self.auction.biggest_bid}')

    def test_should_return_the_highest_and_lowest_bid_when_there_are_three_bids(self):
        habib = User('Habib', 1000)
        habib_bid = Bid(habib, 135)
        self.auction.bid(self.brunno_bid)
        self.auction.bid(habib_bid)
        self.auction.bid(self.nathan_bid)

        self.assertEqual(TestAuction.smallest_bid, self.auction.smallest_bid,
                         f'The highest bid must be {TestAuction.smallest_bid}, but was {self.auction.smallest_bid}')
        self.assertEqual(TestAuction.biggest_bid, self.auction.biggest_bid,
                         f'The lowest bid must be {TestAuction.biggest_bid}, but was {self.auction.biggest_bid}')

    def test_should_return_the_highest_and_lowest_bid_when_there_are_one_bid(self):
        habib_bid_value = 135
        habib = User('Habib', 1000)
        habib_bid = Bid(habib, habib_bid_value)
        self.auction.bid(habib_bid)

        self.assertEqual(habib_bid_value, self.auction.smallest_bid,
                         f'The highest bid must be {habib_bid_value}, but was {self.auction.smallest_bid}')
        self.assertEqual(habib_bid_value, self.auction.biggest_bid,
                         f'The lowest bid must be {habib_bid_value}, but was {self.auction.biggest_bid}')

    def test_must_allow_a_bid_if_the_last_bid_has_different_user(self):
        self.auction.bid(self.brunno_bid)
        self.auction.bid(self.nathan_bid)

        self.assertEqual(2, len(self.auction.bids),
                         f'There are {len(self.auction.bids)} bids where must has 2')

    def test_should_not_allow_a_bid_if_the_last_bid_was_from_the_same_user(self):
        with self.assertRaises(InvalidBid):
            self.auction.bid(self.brunno_bid)
            self.auction.bid(self.brunno_bid)

    def test_must_not_allow_a_bid_if_the_value_is_less_than_the_last_bid(self):
        with self.assertRaises(InvalidBid):
            self.auction.bid(self.nathan_bid)
            self.auction.bid(self.brunno_bid)
