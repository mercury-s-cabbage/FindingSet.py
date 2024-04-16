
cards = [
        {
            "id": 6,
            "color": 1,
            "shape": 2,
            "fill": 3,
            "count": 1
        },
        {
            "id": 21,
            "color": 3,
            "shape": 1,
            "fill": 3,
            "count": 2
        },
        {
            "id": 3,
            "color": 1,
            "shape": 1,
            "fill": 3,
            "count": 3
        },
        {
            "id": 24,
            "color": 3,
            "shape": 2,
            "fill": 3,
            "count": 1
        },
        {
            "id": 15,
            "color": 2,
            "shape": 2,
            "fill": 3,
            "count": 2
        },
        {
            "id": 5,
            "color": 1,
            "shape": 2,
            "fill": 2,
            "count": 3
        },
        {
            "id": 25,
            "color": 3,
            "shape": 3,
            "fill": 1,
            "count": 1
        },
        {
            "id": 27,
            "color": 3,
            "shape": 3,
            "fill": 3,
            "count": 2
        },
        {
            "id": 10,
            "color": 3,
            "shape": 3,
            "fill": 2,
            "count": 3
        }]
Q = len(cards)
f_card = {"color": 2,
          "shape": 1,
          "fill": 1,
          "count": 3
          }

def printCard(card):
    colors = ["red", "blue", "green"]
    shapes = ["ovals", "waves", "diamonds"]
    fills = ["white", "color", "sripped"]
    counts = ["one", "two", "three"]

    print("id = ", card['id'])
    print("color = ", colors[int(card['color'])-1])
    print("shape = ", shapes[int(card['color']) - 1])
    print("fill = ", fills[int(card['color']) - 1])
    print("count = ", counts[int(card['color']) - 1])
    print("\n")


for i in range(Q-1):
    for j in range(i+1, Q):

        # determine the remaining card
        for key in ['color', 'shape', "fill", "count"]:
            f_card[key] = cards[i][key] if cards[i][key] == cards[j][key] else (
                    6 - int(cards[i][key]) - int(cards[j][key]))

        # find third card
        for k in range(j+1, Q):
            a = 0
            for key in f_card:
                if f_card[key] != cards[k][key]:
                    break
                else:
                    a += 1

                if a == 4:
                    printCard(cards[i])
                    printCard(cards[j])
                    printCard(cards[k])
