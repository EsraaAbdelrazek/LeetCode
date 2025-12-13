from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        category_order = {cat: i for i, cat in enumerate(valid_categories)}
        valid_coupons = []

        for i in range(len(code)):
            if (
                code[i] and
                re.match(r'^[a-zA-Z0-9_]+$', code[i]) and
                businessLine[i] in valid_categories and
                isActive[i]
            ):
                valid_coupons.append((businessLine[i], code[i]))

        valid_coupons.sort(key=lambda x: (category_order[x[0]], x[1]))

        return [coupon[1] for coupon in valid_coupons]
