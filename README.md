# CodingChallenge
Coding Challenge

* So, I wasn't sure how I would get the distance, so I took the liberty of attaching an arbitrary x,y coordinates for each city
    -distance takes in a list of cities, and x,y coordinates, and from there linearly calculates the distances from city to city in the list
    -Returning a path with the minimal distance is the travelling salesman problem which is of NP-Hard problem. My approach to this would be from city[0] to city[n], I would consider each as a starting city, from there, I would connect the rest to the permutation of city[1:n], city[0]+city[2:n],...city[0:n-1] and for recursively make each node another starting point. Base case would be that there's only 1 city, and in such a case, the distance travelled is 0. However, if not, based on the permutations of the generated paths, get the minimal distance.

* To run the script, call ./test1 <file_input> [-type=miles or -type=km]
    -file_input takes in a "<City> | <x,y>" for each line

* If I was given more time, I would actually use Google's API for getting the real coordinates based on the city names via some type of Get request
  Furthermore, I would implement the TSP such that --optimize would work!

test2:
* I defined a class Deck such that it cannot see the whole list of cards! ("I abstracted it away as a stack since it seems to me that you were asking me for a function GetNextCard. But I could redefine it either way and have a GetCard(self,index). 
* The constructor of the class Deck linearly builds a deck from spades,ace...clubs,Q. Calling Shuffle would shuffle this list of cards.

* Shuffle shuffles the cards, and also I have a private/protected attribute of card_index. Here since we "restore" all cards and then shuffle, I just restore the card_index. This way, I don't need to delete items from the list of cards but rather give the illusion that I was deleting

* GetNextCard gets the "top" of the card from the deck, and if we've "ran out of cards" (abstracted away by the card_index, and caught by try except branch), then GetNextCard returns None

* As for the Card class, I protected suit and card_number. To get these, one would need to call get_card_number(self) and get_suit(self), and similarly for setting these values. 

* If for some reason calling the setters get weird parameters, then it defaults to "spades" and "ace" by default

* I designed the system this way because say someone invents a new game with cards and decks. Then from here, we can easily recycle these such that we just inherit from Card and Deck and override necessary methods/attributes!


****
comments:
  I realized I was supposed to do the coding challenge on Friday, (For some reason I thought I said Saturday! haha, my mistake) and I believe I started 30 min later

  Also I couldn't implement the TSP on the distance problem due to time constraint. But I described my algorithm and generating permutations should be easy! ( prolly around 10 to 20 depending on debugging)

  Similarly, for more precision on coordinates, I would use Google's API, but that's if I have more time (prolly around 20 to 30 min..I still need to get a key from them!)
****
