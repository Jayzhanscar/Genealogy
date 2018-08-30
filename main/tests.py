# from django.test import TestCase
#
# # Create your tests here.
#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# # class Stack:
# #     def __init__(self):
# #         self.items = []
# #
# #     def push(self, item):
# #         self.items.append(item)
# #
# #     def pop(self):
# #         return self.items.pop()
# #
# #     def clear(self):
# #         del self.items[:]
# #
# #     def empty(self):
# #         return self.size() == 0
# #
# #     def size(self):
# #         return len(self.items)
# #
# #     def top(self):
# #         return self.items[self.size()-1]
# #
# # a = Stack()
# # a.push('1')
# # a.push('23')
# # a.push('34')
# # a.clear()
# # print(a.items, a.size())
# #
# #
# #
# # import queue
# # q = queue.LifoQueue()
# # for i in range(5):
# #     q.put(i)
# #
# # while not q.empty():
# #     print(q.get())
# #
# # e = queue.Queue()
# #
# # for i in range(5):
# #     e.put(i)
# # while not e.empty():
# #     print(e.get())
#
# # myTree = ['a', ['b', [], []], ['e', [], []], ['c', ['f', [], []]]]
# # print(myTree[0])
# # print(myTree[1])
# # print(myTree[2])
#
# # li = [1, 3, 9, 6, 23, 5, 24, 5, 6, 7, 6]
# # print(list(set(li)), len(list(set(li))))
# #
# # if len(li) == 0:
# #     print(0)
# #
# # j = 0
# # for i in range(len(li)):
# #     print(i)
# #
# #
# # def removeDuplicates(nums):
# #     """
# #     :type nums: List[int]
# #     :rtype: int
# #     """
# #     if len(nums) == 0:
# #         return 0
# #     j = 0
# #     len_n = len(nums)
# #     for i in range(len_n):
# #         if nums[j] != nums[i]:
# #             nums[j + 1] = nums[i]
# #             j += 1
# #     return j + 1
# #
# # print(removeDuplicates(sorted(li)))
# # class Solution:
# #
# #     def lengthOfLongestSubstring(self, s):
# #         """
# #         :type s: str
# #         :rtype: int
# #         """
# #         res_list = []
# #         max = 0
# #         if len(s) == 0:
# #             return ''
# #         else:
# #             length  = len(s)
# #             for i in range(length):
# #                 tmp = s[i]
# #                 for j in range(i+1, length):
# #                     if s[j] not in tmp:
# #                         tmp+=s[j]
# #                     else:
# #                         break
# #                 res_list.append(tmp)
# #
# #         for i in res_list:
# #             if len(i)> max:
# #                 max = len(i)
# #         return  max
# #
# #
# #
# # a = Solution()
# #
# # b = a.lengthOfLongestSubstring('pwwkew')
# #
# # print
# # class Solution:
# #     def findMedianSortedArrays(self, nums1, nums2):
# #         """
# #         :type nums1: List[int]
# #         :type nums2: List[int]
# #         :rtype: float
# #         """
# #         result1 = 0
# #         result2 = 0
# #         if len(nums1) == 0 or len(nums2) == 0 :
# #             return 0
# #
# #         else:
# #             for i in nums2:
# #                 nums1.append(i)
# #             nums1.sort()
# #             k = len(nums1)
# #
# #             if k % 2 == 0:
# #                 return (float(nums1[int(k/2-1)]) + nums1[int(k/2)]) / 2
# #             else:
# #                 return nums1[int(k-1)/2]
# #
# #
# # a = Solution()
# #
# # b = a.findMedianSortedArrays([1, 2],[3,4])
# # print(b)
#
# class Solution():
#
#     def maxArea(self, height):
#         """
#
#         :param height: List[int]
#         :return:
#         """
#         max = []
#         l = 0
#         r = len(height) -1
#
#         if not height:
#             return 0
#
#         for i in range(r):
#             # for j, v in enumerate(height):
#             #     if k > v :
#             #         if max < abs(j - i) * v:
#             #             max = abs(j - i) * v
#             #     else:
#             #         if max < abs(j - i) * k:
#             #             max = abs(j - i) * k
#             while l < r:
#
#               max.append()
#
#         print(max)
#
#
#
#sudo certbot certonly --standalone -d example.com --agree-tos --email 你的@邮箱.com
#
#
#
#letsencrypt certonly --agree-tos --email youname@163.com -d www.gabin.top
#sudo certbot --nginx -d your-domian.com -d www.your-domain.com
#
#
#sudo certbot-auto  certonly --standalone -d example.com  -d www.example.com
# a = Solution()
# a.maxArea([0, 2])
#
#
#

import datetime


import MySQLdb

db = MySQLdb.connect("localhost", "root", "zlj941020", "jiapu", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

for i in range(16,500):
    import random
    set_name = ['吴','张','羽', '花', '古']
    father = ['吴','张','羽', '花', '古']
    gen = ['壹', '貮', '叁', '肆' , '伍']
    sex = ['男', '女']
    content = ' 鲁迅（1881年9月25日－1936年10月19日），原名周樟寿，后改名周树人，字豫山，后改豫才，“鲁迅”是他1918年发表《狂人日记》时所用的笔名，也是他影响最为广泛的笔名，浙江绍兴人。著名文学家、思想家，五四新文化运动的重要参与者，中国现代文学的奠基人。毛泽东曾评价：“鲁迅的方向，就是中华民族新文化的方向'
    sql = "INSERT INTO User(id, \
           name, father_id, generation, line, sex,content) \
           VALUES ('%d','%s', '%s', '%s', '%s','%s', '%s')" % \
          (i, set_name[random.randint(0,4)],father[random.randint(0,4)],gen[random.randint(0,4)],gen[random.randint(0,4)],
           sex[random.randint(0,1)], content[0])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('ok')
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)

# 关闭数据库连接
db.close()

# for i in range(16,500):
#     import random
#     set_name = ['吴','张','羽', '花', '古']
#     father = ['吴','张','羽', '花', '古']
#     print(i, set_name[random.randint(0,4)])