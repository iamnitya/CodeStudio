class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        fav_restaurant = {}
        res_list = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    fav_restaurant[list1[i]] = i + j
                    
        for i in fav_restaurant:
            if fav_restaurant[i] == fav_restaurant[min(fav_restaurant, key=fav_restaurant.get)]:
                res_list.append(i)
        return res_list