import instaloader
import os
import random


def load_explore():
    ig_username = os.environ['ig_username']
    ig_password = os.environ['ig_password']

    L = instaloader.Instaloader()
    L.login(ig_username, ig_password)

    posts = L.get_explore_posts()

    post_count = 0
    for post in posts:
        L.save_metadata_json(f"instagram_meme/{post_count}", post)
        post_count += 1
        if (post_count == 20):
            break


def get_explore():

    onlyfiles = next(os.walk('instagram_meme/'))[2]
    if (len(onlyfiles) == 0):
        load_explore()

    memes = []

    for filename in os.listdir('instagram_meme/'):
        memes.append(filename)

    meme = random.choice(memes)
    return meme


def del_memes(meme_name):
    def_file = meme_name
    os.remove(f"instagram_meme/{def_file}")


def reset_memes():
    for filename in os.listdir('instagram_meme/'):
        file_name = filename
        os.remove(f"instagram_meme/{file_name}")
