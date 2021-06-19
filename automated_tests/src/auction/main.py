from automated_tests.src.auction.domain import User, Bid, Auction, Evaluator

nathan = User('Nathan')
brunno = User('Brunno')

brunno_bid = Bid(brunno, 100.0)
nathan_bid = Bid(nathan, 150.0)

auction = Auction('Notebook')

auction.bids.extend([brunno_bid, nathan_bid])

for bid in auction.bids:
    print(f'{bid.user} deu um lance de R${bid.value}')

evaluator = Evaluator()
evaluator.evaluate(auction)

print(f'O menor lance foi R${evaluator.smallest_bid}')
print(f'O maior lance foi R${evaluator.biggest_bid}')