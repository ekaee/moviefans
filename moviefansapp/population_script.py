import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviefansapp.settings")

import django

django.setup()
from main.models import Movie, Genre, Comments


def populate():
    action_movies = [
        {
            "name": "The Suicide Squad",
            "description": "Supervillains Harley Quinn, Bloodsport, Peacemaker and a collection of nutty cons at Belle Reve prison join the super-secret, super-shady Task Force X as they are dropped off at the remote, enemy-infused island of Corto Maltese.",
            "img": "the_suicide_squad.jpg",
            "rating": 55,
            "views": 4444,
        },
        {
            "name": "Jolt",
            "description": "A bouncer with a slightly murderous anger-management problem that she controls with the help of an electrode-lined vest she uses to shock herself back to normalcy whenever she gets homicidal.",
            "img": "jolt.jpg",
            "rating": 41,
            "views": 22221,
        },
        {
            "name": "Loki",
            "description": "The mercurial villain Loki resumes his role as the God of Mischief in a new series that takes place after the events of “Avengers: Endgame.”",
            "img": "loki.jpg",
            "rating": 31,
            "views": 1000,
        },
    ]

    comedy_movies = [
        {
            "name": "Jungle Cruise",
            "description": "Based on Disneyland's theme park ride where a small riverboat takes a group of travelers through a jungle filled with dangerous animals and reptiles but with a supernatural element.",
            "img": "jungle_cruise.jpg",
            "rating": 21,
            "views": 1000,
        },
        {
            "name": "Ted Lasso",
            "description": "Follows an American football coach Ted Lasso who heads to the U.K. to manage a struggling London football team in the top flight of English football.",
            "img": "ted_lasso.jpg",
            "rating": 80,
            "views": 900,
        },
        {
            "name": "Space Jam: A New Legacy",
            "description": "A rogue artificial intelligence kidnaps the son of famed basketball player LeBron James, who then has to work with Bugs Bunny to win a basketball game.",
            "img": "space_jam.jpg",
            "rating": 23,
            "views": 800,
        },
    ]

    horror_movies = [
        {
            "name": "The Forever Purge",
            "description": "All the rules are broken as a sect of lawless marauders decides that the annual Purge does not stop at daybreak and instead should never end.",
            "img": "the_forever_purge.jpg",
            "rating": 2,
            "views": 30,
        },
        {
            "name": "Blood Red Sky",
            "description": "A woman with a mysterious illness is forced into action when a group of terrorists attempt to hijack a transatlantic overnight flight.",
            "img": "blood_red_sky.jpg",
            "rating": 5,
            "views": 5,
        },
        {
            "name": "The Walking Dead",
            "description": "Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins and must lead a group of survivors to stay alive.",
            "img": "the_walking_dead.jpg",
            "rating": 0,
            "views": 1,
        },
    ]

    romance_movies = [
        {
            "name": "Outer Banks",
            "description": "A group of teenagers from the wrong side of the tracks stumble upon a treasure map that unearths a long buried secret.",
            "img": "outer_banks.jpg",
            "rating": 1,
            "views": 10,
        },
        {
            "name": "Virgin River",
            "description": "Seeking a fresh start, nurse practitioner Melinda Monroe moves from Los Angeles to a remote Northern California town and is surprised by what and who she finds.",
            "img": "virgin_river.jpg",
            "rating": 44,
            "views": 4433,
        },
        {
            "name": "The Last Letter from Your Lover",
            "description": "A pair of interwoven stories set in the past and present follow an ambitious journalist determined to solve the mystery of a forbidden love affair at the center of a trove of secret love letters from 1965.",
            "img": "last_letter.jpg",
            "rating": 22,
            "views": 1233,
        },
    ]

    drama_movies = [
        {
            "name": "Old",
            "description": "A vacationing family discovers that the secluded beach where they're relaxing for a few hours is somehow causing them to age rapidly, reducing their entire lives into a single day.",
            "img": "old.jpg",
            "rating": 2,
            "views": 333,
        },
        {
            "name": "The Green Knight",
            "description": "A fantasy re-telling of the medieval story of Sir Gawain and the Green Knight.",
            "img": "green_knight.jpg",
            "rating": 222,
            "views": 2222,
        },
        {
            "name": "Dune",
            "description": "Feature adaptation of Frank Herbert's science fiction novel, about the son of a noble family entrusted with the protection of the most valuable asset and most vital element in the galaxy.",
            "img": "dune.jpg",
            "rating": 90,
            "views": 1111,
        },
    ]

    animation_movies = [
        {
            "name": "Soul",
            "description": "After landing the gig of a lifetime, a New York jazz pianist suddenly finds himself trapped in a strange land between Earth and the afterlife.",
            "img": "soul.jpg",
            "rating": 8,
            "views": 10,
        },
        {
            "name": "Luca",
            "description": "On the Italian Riviera, an unlikely but strong friendship grows between a human being and a sea monster disguised as a human.",
            "img": "luca.jpg",
            "rating": 10,
            "views": 100,
        },
        {
            "name": "Attack on Titan",
            "description": "After his hometown is destroyed and his mother is killed, young Eren Jaeger vows to cleanse the earth of the giant humanoid Titans that have brought humanity to the brink of extinction.",
            "img": "titan.jpg",
            "rating": 890,
            "views": 213422,
        },
    ]

    fantasy_movies = [
        {
            "name": "Masters of the Universe: Revelation",
            "description": "The war for Eternia begins again in what may be the final battle between He-Man and Skeletor. A new animated series from writer-director Kevin Smith.",
            "img": "master.jpg",
            "rating": 2,
            "views": 23,
        },
        {
            "name": "Game of Thrones",
            "description": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
            "img": "game.jpg",
            "rating": 2333,
            "views": 123123,
        },
        {
            "name": "Lucifer",
            "description": "Lucifer Morningstar has decided he's had enough of being the dutiful servant in Hell and decides to spend some time on Earth to better understand humanity. He settles in Los Angeles - the City of Angels.",
            "img": "luci.jpg",
            "rating": 55,
            "views": 2321,
        },
    ]

    genres = [
        {"name": "Action", "pages": action_movies},
        {"name": "Comedy", "pages": comedy_movies},
        {"name": "Horror", "pages": horror_movies},
        {"name": "Romance", "pages": romance_movies},
        {"name": "Drama", "pages": drama_movies},
        {"name": "Animation", "pages": animation_movies},
        {"name": "Fantasy", "pages": fantasy_movies},
    ]

    for gx in genres:
        g = add_genre(gx['name'])
        for mx in gx['pages']:
            add_movie(g, mx['name'], mx['description'], mx['img'], mx['rating'], mx['views'])


def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g


def add_movie(genre, name, description, img, rating, views):
    m = Movie.objects.get_or_create(
        genre_id=genre, name=name, description=description, thumbnail=img, rating=rating, views=views)[0]
    m.save()
    return m


if __name__ == '__main__':
    print("Running populate script")
    populate()
