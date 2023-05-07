class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in items1 :
            for j in items2:
                if i[0]==j[0]:
                     i[1]+=j[1]

        for k in items2:
            flag = True
            for l in items1:
                if k[0]==l[0]:
                    flag = False
            if flag == True:
                items1.append(k)
        items1.sort()
        return(items1)