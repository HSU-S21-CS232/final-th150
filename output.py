import os

def output_wrapper():
    os.system('cls')
    return 'this program will automatically accept your League of Legends queue, no more missing queues for you'

def output_message(message):
    print(output_wrapper())
    print(message)
