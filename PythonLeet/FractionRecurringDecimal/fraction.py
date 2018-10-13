class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        before_decimal = str(numerator/denominator)
        new_numerator = numerator % denominator
        non_repeating, repeating = self.post_decimal(new_numerator, denominator)
        
        if repeating != "":
            repeating = "(" + repeating + ")"        

        
        second_half = non_repeating + repeating
        
        return before_decimal + "." + second_half

    def post_decimal(self, remainder, denominator):
        non_repeating = ""
        repeating = ""
        remainder_map = {}
        index = 0
        while remainder != 0:
            curr_num = (remainder*10)/denominator
            non_repeating += str(curr_num)
            remainder = (remainder*10)%denominator
            if curr_num in remainder_map:
                non_repeating = non_repeating[:-1]
                begin_index = remainder_map[curr_num]                
                temp = non_repeating[:begin_index]
                repeating = non_repeating[begin_index:]
                non_repeating = temp
                break
            else:
                remainder_map[curr_num] = index 
            index += 1
        # print("")
        # print(remainder_map)
        
        return non_repeating, repeating


    # def second_half(self, numerator, denominator):
    #     non_repeating = ""
    #     repeating_pattern = ""
    #     index = 1
    #     remainder_map = {}
    #     non_repeating += str((numerator*10)/denominator)
    #     curr_remainder = (numerator*10)%denominator     
    #     remainder_map[curr_remainder] = index 
    #     index += 1           
    #     while curr_remainder != 0:             
    #         non_repeating += str((curr_remainder*10)/denominator)
    #         curr_remainder = (curr_remainder*10) % denominator

    #         if curr_remainder in remainder_map:
    #             repeat_index =remainder_map[curr_remainder]
    #             temp = non_repeating[:repeat_index]
    #             repeating_pattern = non_repeating[repeat_index:]
    #             if temp == repeating_pattern:
    #                 temp = temp[:-1]
    #             non_repeating = temp
    #             break
    #         else:
    #             remainder_map[curr_remainder] = index 
    #         index += 1
    #     return non_repeating, repeating_pattern
def main():
    s = Solution()
    print(s.fractionToDecimal(2,6))
    print(s.fractionToDecimal(5,8))
    print(s.fractionToDecimal(3227,555))
    print(s.fractionToDecimal(4,333))
    print(s.fractionToDecimal(1,6))

main()

# # # 1/4
# # #    25
# # # 4 10
# # #    8
# # #    2

# # print(50%8)
# # print(50/8)

s = "Hello"
print(s[0:])