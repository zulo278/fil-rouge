import os

objects = ['client','comments','event-bus','moderation','posts-clusterip','query']

for object in objects:
    os.system(f'kubectl delete deployment {object}-deployment')
    os.system(f'kubectl delete svc {object}-srv')