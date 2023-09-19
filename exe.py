#!/usr/bin/python3

# from models import storage
# from models.review import Review

# print(storage.all(), 'this is for all objects')

# for obj in storage.all(Review):
#     print(obj.values(), 'obj in loop')
# print(storage.all(Review), 'This is for the review objects')

from models import storage
from models.review import Review

review_list = []
print(type(storage.all(Review)))
for review in list(storage.all(Review).values()):
    # if review.place_id == self.id:
    review_list.append(review)
    print(review_list)
