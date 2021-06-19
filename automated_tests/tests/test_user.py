import pytest
from src.auction.domain import Auction, User, Bid
from src.auction.exceptions import InvalidBid


@pytest.fixture
def nathan():
    return User('Nathan', 2000)


@pytest.fixture
def auction():
    return Auction('Notebook')


def test_should_subtract_from_user_wallet_when_he_bids(nathan, auction):
    nathan.bid(200, auction)

    assert 1800 == nathan.wallet


def test_should_allow_the_bid_when_the_value_is_lesser_than_wallet(nathan, auction):
    nathan.bid(200, auction)

    assert len(auction.bids) == 1

def test_should_allow_the_bid_when_the_value_is_equal_to_wallet(nathan, auction):
    nathan.bid(2000, auction)

    assert len(auction.bids) == 1


def test_should_not_allow_the_bid_when_the_value_is_higher_than_wallet(nathan, auction):
    with pytest.raises(InvalidBid):
        nathan.bid(2001, auction)

