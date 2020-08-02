import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore


# STAGE 2
# if url == "bloomberg.com":
#     print(bloomberg_com)
# elif url == "nytimes.com":
#     print(nytimes_com)
# elif url == "exit":
#     break

# STAGE 3
# sites = {"nytimes.com": '''
# This New Liquid Is Magnetic, and Mesmerizing
#
# Scientists have created “soft” magnets that can flow
# and change shape, and that could be a boon to medicine
# and robotics. (Source: New York Times)
#
#
# Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
#
# Jessica Wade has added nearly 700 Wikipedia biographies for
#  important female and minority scientists in less than two
#  years.
#
# ''', "bloomberg.com": '''
# The Space Race: From Apollo 11 to Elon Musk
#
# It's 50 years since the world was gripped by historic images
#  of Apollo 11, and Neil Armstrong -- the first man to walk
#  on the moon. It was the height of the Cold War, and the charts
#  were filled with David Bowie's Space Oddity, and Creedence's
#  Bad Moon Rising. The world is a very different place than
#  it was 5 decades ago. But how has the space race changed since
#  the summer of '69? (Source: Bloomberg)
#
#
# Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
#
# Twitter and Square Chief Executive Officer Jack Dorsey
#  addressed Apple Inc. employees at the iPhone maker’s headquarters
#  Tuesday, a signal of the strong ties between the Silicon Valley giants.
# '''}
#
# nytimes_com = '''
# This New Liquid Is Magnetic, and Mesmerizing
#
# Scientists have created “soft” magnets that can flow
# and change shape, and that could be a boon to medicine
# and robotics. (Source: New York Times)
#
#
# Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
#
# Jessica Wade has added nearly 700 Wikipedia biographies for
#  important female and minority scientists in less than two
#  years.
#
# '''
#
# bloomberg_com = '''
# The Space Race: From Apollo 11 to Elon Musk
#
# It's 50 years since the world was gripped by historic images
#  of Apollo 11, and Neil Armstrong -- the first man to walk
#  on the moon. It was the height of the Cold War, and the charts
#  were filled with David Bowie's Space Oddity, and Creedence's
#  Bad Moon Rising. The world is a very different place than
#  it was 5 decades ago. But how has the space race changed since
#  the summer of '69? (Source: Bloomberg)
#
#
# Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
#
# Twitter and Square Chief Executive Officer Jack Dorsey
#  addressed Apple Inc. employees at the iPhone maker’s headquarters
#  Tuesday, a signal of the strong ties between the Silicon Valley giants.
# '''
#
# # write your code here
#
# def is_url(url):
#     correct = False
#     for letter in url:
#         if letter == ".":
#             return True
#     return correct
#
# def create_foler(name):
#     if not os.path.exists(name):
#         os.mkdir(name)
#
# def remove_dot(url):
#     reverse_url = url[::-1]
#     for char in reverse_url:
#         if char != ".":
#             reverse_url = reverse_url.lstrip(char)
#         else:
#             reverse_url = reverse_url.lstrip(char)
#             break
#     return reverse_url[::-1]
#
#
# args = sys.argv
# history = deque()
# temp_url = ""
# if len(args) == 2:
#     while True:
#
#         url = input()
#         # print(remove_dot(url))
#         try:
#             if is_url(url):
#                 create_foler(args[1])
#                 print(sites[url])
#                 new_file = open(args[1] + "/" + remove_dot(url)+ ".txt", "w")
#                 new_file.write(sites[url])
#                 new_file.close()
#                 if is_url(temp_url):
#                     history.append(temp_url)
#                 temp_url = url
#
#
#             elif url == "exit":
#                 break
#             elif url == "back":
#                 print(sites[history.pop()])
#             else:
#                 new_file = open(args[1] + "/" + url + ".txt", "r")
#                 print(new_file.read())
#                 new_file.close()
#         except FileNotFoundError:
#             print("Error: Incorrect URL")
#         except KeyError:
#             print("Error: Incorrect URL")

def is_url(url):
    correct = False
    for letter in url:
        if letter == ".":
            return True
    return correct


def create_foler(name):
    if not os.path.exists(name):
        os.mkdir(name)


def remove_dot(url):
    reverse_url = url[::-1]
    for char in reverse_url:
        if char != ".":
            reverse_url = reverse_url.lstrip(char)
        else:
            reverse_url = reverse_url.lstrip(char)
            break
    return reverse_url[::-1]


def add_http(url):
    if url.startswith("https://"):
        return url
    else:
        return "https://" + url


def remove_tags(html_data, file):
    html = BeautifulSoup(html_data.text, "html.parser")
    mass_of_tags = list(html.find_all(TAGS, string=True))

    for tag in mass_of_tags:
        if tag.name == "a":
            print(Fore.BLUE + tag.get_text())
        else:
            print(tag.get_text())
        file.write(tag.get_text())


TAGS = ['a', 'p', 'ul', 'ol', 'li', 'span']
init(autoreset=True)

args = sys.argv
history = deque()
temp_url = ""
if len(args) == 2:
    while True:

        url = input()
        try:
            if is_url(url):
                data = requests.get(add_http(url))
                create_foler(args[1])
                new_file = open(args[1] + "/" + remove_dot(url) + ".txt", "w", encoding="utf-8")

                remove_tags(data, new_file)

                new_file.close()
                if is_url(temp_url):
                    history.append(temp_url)
                temp_url = url

            elif url == "exit":
                break

            elif url == "back":
                history_file = open(args[1] + "/" + remove_dot(history.pop()) + ".txt", "r")
                for sentence in history_file.readlines():
                    print(sentence)
            else:
                new_file = open(args[1] + "/" + url + ".txt", "r")
                print(new_file.read())
                new_file.close()
        except FileNotFoundError:
            print("Error: Incorrect URL")
        except KeyError:
            print("Error: Incorrect URL")
