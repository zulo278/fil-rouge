import os

directories = ['client','comments','event-bus','moderation','posts','query']

for directory in directories:
    os.system(f'docker build -t {directory} ./{directory}')