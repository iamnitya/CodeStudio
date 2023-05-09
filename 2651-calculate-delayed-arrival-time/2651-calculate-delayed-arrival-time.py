class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        final = arrivalTime + delayedTime
        if final<24:
            return final
        else:
            return (final -24)