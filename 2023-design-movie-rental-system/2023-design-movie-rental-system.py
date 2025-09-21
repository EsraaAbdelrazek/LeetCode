from sortedcontainers import SortedList

class MovieRentingShop:
    def __init__(self):
        self.id = None
        self.priceTable = {}
        self.shelf ={} # key : movieId(int), val: price(int)

    def rent(self, movie):
        if movie not in self.shelf:
            return None
        
        del self.shelf[movie]
        return self.priceTable[movie]

    def drop(self, movie):
        self.shelf[movie] = self.priceTable[movie]
        return self.priceTable[movie]
        
    def add(self, movie, price):
        if movie in self.shelf:
            return 
        self.shelf[movie] = price
        self.priceTable[movie] = price


    def moviePrice(self, movie):
        return self.priceTable[movie]

class MovieRentingMovie:
    def __init__(self):
        self.shops = set([])
        self.id = None

    def addShop(self, shop): # shop : MovieRentingShop
        self.shops.add(shop)

    def removeShop(self, shop):  # shop : MovieRentingShop
        self.shops.discard(shop)

    def search(self):
        heap = []
        for shop in self.shops:
           
            heapq.heappush(heap, (-shop.moviePrice(self.id), -shop.id))
            if len(heap) > 5:
                heapq.heappop(heap)

        return sorted(heap, reverse=True,key = lambda x: (x[0], x[1]))


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rentedMovies = SortedList() # [price, shopid]
        self.shops = defaultdict(MovieRentingShop)
        self.movies = defaultdict(MovieRentingMovie)
        self.cache = {}

        for shopId, movie, price in  entries:
            self.shops[shopId].id = shopId
            self.movies[movie].id = movie
            self.shops[shopId].add(movie, price)
            self.movies[movie].addShop(self.shops[shopId])


        

    def search(self, movie: int) -> List[int]:
        if movie in self.cache and self.cache[movie] is not None:
            return self.cache[movie]
        result = self.movies[movie].search()
     
        result = [-sid for price, sid in result]
        self.cache[movie] = result
        return self.cache[movie]

        

    def rent(self, shop: int, movie: int) -> None:
        self.cache[movie] = None
        price = self.shops[shop].rent(movie)
        if price is None:
            return
        self.movies[movie].removeShop(self.shops[shop])
        self.rentedMovies.add((price, shop, movie))




    def drop(self, shop: int, movie: int) -> None:
        self.cache[movie] = None
        price =  self.shops[shop].drop(movie)
        self.rentedMovies.remove((price, shop, movie))
        self.movies[movie].addShop(self.shops[shop])

        

    def report(self) -> List[List[int]]:
        
        return [(shop, movie) for price , shop, movie in self.rentedMovies[:5]]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()