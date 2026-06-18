class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        answer = {} 

        for num in nums:
        
            if num not in answer:
                answer[num] = 1
        
            else: 
                answer[num] += 1

        # lines 6 through 11 could be written: answer[num] = answer.get(num, 0) + 1 // answer.get checks key in dict, if exists, returns current count @num, otherwise returns zero (defualt we provide) then adds one to whichever it gets back
        pairs = []

        for num, freq in answer.items():
            pairs.append((num, freq))

        pairs.sort(key = lambda x: x[1], reverse = True)

        result = []
        for i in range(k):
            num, frequency = pairs[i]
            result.append(num)
        return result