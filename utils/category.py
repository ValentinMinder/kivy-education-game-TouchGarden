# coding=utf-8
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
import random

from utils import texts as txt
from utils import sizes
from utils.gui import ImageWrap

sound_cat = SoundLoader.load("audio/chat.wav")


class Category(object):
    # has: name, el1, el2, target
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


# draggable element scatter (touchable by children)
class ElementScatter(Scatter):
    def __init__(self, **kwargs):
        super(ElementScatter, self).__init__()
        # has: name, first
        # defaults: positive, correction

        self.do_rotation = self.do_scale = False  # disable other moves than translation (drag & drop)
        self.touch_enabled = True  # enable the reaction to touch
        self.positive = True  # if False, should define positive_ref
        self.correction = False  # if true, should define correction_no and correction_yes
        for k, v in kwargs.items():
            setattr(self, k, v)

        # _orig to replace object at their correct original placement
        self.x_orig = sizes.width_border_left
        self.y_orig = sizes.height_left_first if self.first else sizes.height_left_second
        self.pos = (self.x_orig, self.y_orig)
        self.size_hint = (None, None)
        self.size = (sizes.width_left_elements, sizes.width_left_elements)

        self.image.source = self.source
        self.image.size = (sizes.width_left_images, sizes.width_left_images)
        self.image.pos = (sizes.border_small, sizes.border_small)


# init for all categories all the possible elements and scenario (including positive, negative and some recover)
def init_category_struct(frame):
    duration_start = 3
    duration_end = 4

    def rand_elem():
        # bad element has 2/4 chances to be on top
        return random.choice([True, False, False, False])

    def anim_setup_p1():
        animal = ImageWrap(
            pos=(0, sizes.height * 0.4),
            size=(88, 73),
            source='images/animations/eaux/grenouille_saute.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_start_p1():
        return Animation(pos=sizes.event_c1pos, duration=duration_start)

    def anim_start_n1():
        return Animation(pos=sizes.event_c1neg, duration=duration_start)

    def anim_end_p1(animal):
        heart = ImageWrap(source='images/animations/eaux/coeur.zip',
                          size=(40, 40),
                          pos=sizes.event_c1pos_heart,
                          anim_delay=0.1)
        frame.add_widget(heart)

        def after(*any):
            animal.static.image.source = 'images/non_animes/etang_final.png'
            animal.static.image.anim_loop = 0
            frame.remove_widget(heart)

        animal.image.source = 'images/scenery/transparency.png'
        animal.static.image.source = 'images/animations/eaux/grenouille_love.zip'
        f = 15
        d = 0.2
        animal.static.image.anim_delay = d
        animal.static.image.anim_loop = 1
        anim = Animation(duration=f * d + 0.9)
        anim.bind(on_complete=after)
        return anim

    def anim_end_n1(animal):
        def after(a, i):
            animal.static.image.source = 'images/animations/eaux/piscine_scintille.zip'
            animal.static.image.anim_loop = 0

        animal.static.image.source = 'images/animations/eaux/piscine_plouf.zip'
        animal.static.image.anim_loop = 1
        animal.image.source = 'images/scenery/transparency.png'
        anim = Animation(duration=duration_end)
        anim.bind(on_complete=after)
        return anim

    def anim_end_n1alt(animal):
        def after(*any):
            animal.flip()

        def forward (*any):
            animal.static.image.source = 'images/animations/eaux/piscine_scintille.zip'
            animal.static.image.anim_loop = 0
            animal.image.size = (88, 73)
            anim = Animation(pos=sizes.event_c1altanimal1, duration=duration_end * 0.2)
            anim += Animation(pos=(-50, sizes.height * 0.4), duration=duration_end * 0.8)
            anim.start(animal.image)


        animal.static.image.source = 'images/animations/eaux/piscine_plouf.zip'
        animal.static.image.anim_loop = 1
        f = 18
        d = 0.15
        animal.static.image.anim_delay = d
        animal.flip()
        animal.image.size = 0, 0

        anim = Animation(pos=sizes.event_c1altanimal2, duration= f * d)
        anim.bind(on_complete=forward)
        anim.start(animal.image)

        wait = Animation(duration=f * d + duration_end)
        return wait

    p1 = ElementScatter(name=txt.txt_cat_pond,
                        first=rand_elem(),
                        source='images/non_animes/etang.png',
                        txt_info=txt.txt_info_pond,
                        info_img="images/scenery/transparency.png",
                        event_pos=sizes.event_c1pos_heart,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_p1,
                        anim_end=anim_end_p1)
    n1 = ElementScatter(name=txt.txt_cat_pool,
                        first=not p1.first,
                        positive=False,
                        positive_ref=p1,
                        source='images/animations/eaux/piscine_scintille.zip',
                        txt_info = txt.txt_info_pool,
                        info_img="images/scenery/transparency.png",
                        event_pos=sizes.event_c1neg,
                        anim_setup=anim_setup_p1,
                        anim_start=anim_start_n1,
                        anim_end=anim_end_n1,
                        anim_end_alt=anim_end_n1alt,
                        correction=True,
                        correction_no='images/corrections/piscine_echelle_no.png',
                        correction_yes='images/corrections/piscine_echelle_yes.png',
                        correction_img=ImageWrap(source='images/corrections/piscine_echelle_v1.png',
                                                 size=(22, 20),
                                                 pos=(sizes.event_c1alt))  # sizes.width_left_margin + 265, 503))
                        )
    t1 = ImageWrap(pos=sizes.pos_c1,
                   size=sizes.size_c1,
                   source='images/animations/zones/eaux.zip')
    c1 = Category(name=txt.txt_cat_water,
                  element1=p1, element2=n1, target=t1)

    def anim_setup_p2():
        animal = ImageWrap(
            pos=(sizes.width, sizes.height / 2),
            size=(75, 52),
            source='images/animations/haies/mesange_vole.zip',
            anim_delay=0.2)
        frame.add_widget(animal)
        return animal

    def anim_start_p2():
        return Animation(pos=sizes.event_c2, duration=duration_start)

    def anim_end_p2(animal):
        def forward(a, i):
            anim = Animation(x=sizes.width_ref - 100, duration=duration_end * (1.5 - 2 * f))
            animal.image.source = 'images/animations/haies/mesange_vole.zip'
            animal.image.anim_delay = 0.2
            anim.start(animal.image)

        animal.image.source = 'images/animations/haies/mesange_mange.zip'
        animal.image.anim_delay = 0.1
        f = 0.5
        anim = Animation(x=animal.image.x - 25, y=animal.image.y - 10, duration=duration_end * f)
        anim += Animation(x=animal.image.x - 50, y=animal.image.y + 10, duration=duration_end * f)
        anim.bind(on_complete=forward)
        anim.start(animal.image)

        wait = Animation(duration=duration_end * 1.5)
        return wait

    def anim_end_n2(animal):
        animal.image.source = 'images/animations/haies/mesange_fachee.zip'
        f = 0.2
        anim = Animation(x=animal.image.x - 25, y=animal.image.y - 10, duration=duration_end * f)
        anim += Animation(x=animal.image.x - 50, y=animal.image.y + 10, duration=duration_end * f)
        anim += Animation(pos=(sizes.width_ref - 100, sizes.height / 3), duration=duration_end * f)
        return anim

    p2 = ElementScatter(name=txt.txt_cat_hedge_good,
                        first=rand_elem(),
                        source='images/non_animes/haie_diverses_especes.png',
                        txt_info=txt.txt_info_hedge_good,
                        info_img="images/photos/haies.jpg",
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p2,
                        anim_start=anim_start_p2,
                        anim_end=anim_end_p2)
    n2 = ElementScatter(name=txt.txt_cat_hedge_bad,
                        first=not p2.first,
                        positive=False,
                        positive_ref=p2,
                        source='images/non_animes/haie_de_thuya.png',
                        txt_info=txt.txt_info_hedge_bad,
                        info_img="images/scenery/transparency.png",
                        event_pos=sizes.event_c2,
                        anim_setup=anim_setup_p2,
                        anim_start=anim_start_p2,
                        anim_end=anim_end_n2,
                        anim_end_alt=anim_end_p2,
                        correction=False)
    t2 = ImageWrap(pos=sizes.pos_c2,
                   size=sizes.size_c2,
                   source='images/animations/zones/haies.zip')
    c2 = Category(name=txt.txt_cat_hedge,
                  element1=p2, element2=n2, target=t2)

    def anim_setup_p3():
        animal = ImageWrap(
            pos=(sizes.width, 0),
            size=(52, 44),
            source='images/animations/abris/herisson_marche.zip',
            anim_delay=0.1)
        # bring static image to front
        frame.add_widget(animal, 4)
        return animal

    def anim_setup_n3a():
        # change anims of nice barrier p3 to have the correct animal and speeds
        p3.anim_setup = anim_setup_n3a_alt
        p3.anim_start = anim_start_n3a
        p3.anim_end = anim_end_p3_alt
        animal = ImageWrap(
            pos=(sizes.width, 0),
            size=(200, 200),
            source='images/animations/mur/ecureuil_court.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_setup_n3a_alt():
        animal = ImageWrap(
            pos=(sizes.width, 0),
            size=(200, 200),
            source='images/animations/mur/ecureuil_court.zip',
            anim_delay=0.1)
        frame.add_widget(animal, 4)
        return animal

    def anim_start_p3():
        return Animation(pos=sizes.event_c32, duration=duration_start * 2.5)

    def anim_start_n3a():
        anim = Animation(pos=sizes.event_c32alt, duration=duration_start * 1.5)
        return anim

    def anim_end_p3(animal):
        anim = Animation(x=sizes.width_left_margin, y=sizes.height, duration=duration_end)
        return anim

    def anim_end_p3_alt(animal):
        anim = Animation(x=sizes.width_left_margin - 50, y=sizes.height, duration=duration_end * 0.5)
        return anim

    def anim_end_n3a_alt(animal):
        def after(a, i):
            #the squirrel is BEHIND THE WALL
            frame.remove_widget(animal)
            frame.add_widget(animal, 4)
            anim = Animation(x=animal.image.x, y=animal.image.y - 80, duration=duration_end * 0.1)
            anim += Animation(x=sizes.width_left_margin - 80, y=sizes.height - 80, duration=duration_end * 0.3)
            anim.start(animal.image)

        def onwall(a,i):
            animal.image.source = 'images/animations/mur/ecureuil_court.zip'
            animal.image.anim_delay = 0.1
            anim = Animation(x=animal.image.x - 28, y=animal.image.y + 16, duration=duration_end * 0.1)
            anim.bind(on_complete=after)
            anim.start(animal.image)

        def climb(a, i):
            animal.image.source = 'images/animations/mur/ecureuil_grimpe.zip'
            animal.image.anim_delay = 0.2
            anim = Animation(y=animal.image.y + 80, duration=duration_end * 0.5)
            anim.bind(on_complete=onwall)
            anim.start(animal.image)

        def fire(a, i):
            animal.image.source = 'images/animations/mur/ecureuil_snif.zip'
            animal.image.anim_delay = 0.1
            anim = Animation(duration=duration_end * 0.4)
            anim.bind(on_complete=climb)
            anim.start(animal.image)

        wait = Animation(duration=duration_end * 1.5)
        wait.bind(on_start=fire)
        return wait

    def anim_end_n3a(animal):
        def fall(a, i):
            animal.image.source = 'images/animations/mur/ecureuil_tombe.zip'
            animal.image.anim_delay = 0.2
            animal.image.y += 20

        def fire(a, i):
            animal.image.source = 'images/animations/mur/ecureuil_snif.zip'
            animal.image.anim_delay = 0.1
            anim = Animation(duration=duration_end * 0.5)
            anim.bind(on_complete=fall)
            anim.start(animal.image)

        wait = Animation(duration=duration_end)
        wait.bind(on_start=fire)
        return wait

    def anim_end_n3b(animal):
        animal.image.source = 'images/animations/abris/herisson_mal.zip'
        animal.image.anim_delay = 0.2
        anim = Animation(duration=2)
        return anim

    def anim_end_n3b_alt(animal):
        # the hole in the barrier was added above the fence
        # here we remove the fence and replace the hole with the whole fence with hole in transparency
        # therefore the animal will travel "though the hole and behind the fence"
        animal.static.image.source = 'images/scenery/transparency.png'

        n3b.correction_img.image.source = 'images/corrections/barriere_trou_whole.png'
        n3b.correction_img.image.size = (sizes.size_c3)
        n3b.correction_img.image.pos = (sizes.pos_c3)

        return anim_end_p3(animal)

    p3 = ElementScatter(name=txt.txt_cat_fence_space,
                        first=rand_elem(),
                        source='images/non_animes/barrieres_espacee.png',
                        txt_info=txt.txt_info_fence_space,
                        info_img="images/photos/clotures.png",
                        event_pos=sizes.event_c31,
                        anim_setup=anim_setup_p3,
                        anim_start=anim_start_p3,
                        anim_end=anim_end_p3)
    n3a = ElementScatter(name=txt.txt_cat_fence_wall,
                         first=rand_elem(),
                         positive=False,
                         positive_ref=p3,
                         source='images/non_animes/barriere_beton.png',
                         txt_info=txt.txt_info_fence_wall,
                        info_img="images/photos/murs.jpg",
                         event_pos=sizes.event_c31,
                         anim_setup=anim_setup_n3a,
                         anim_start=anim_start_n3a,
                         anim_end=anim_end_n3a,
                         anim_end_alt=anim_end_n3a_alt,
                         correction=True,
                         correction_no='images/corrections/barriere_lierre_no.png',
                         correction_yes='images/corrections/barriere_lierre_yes.png',
                         correction_img=ImageWrap(source='images/corrections/barriere_lierre.png',
                                                  size=(126, 117),
                                                  pos=(sizes.event_c31alt)))
    n3b = ElementScatter(name=txt.txt_cat_fence_space,
                         first=not n3a.first,
                         positive=False,
                         positive_ref=p3,
                         source='images/non_animes/barrieres_ras_de_sol.png',
                         txt_info=txt.txt_info_fence_nospace,
                        info_img="images/photos/clotures.png",
                         event_pos=sizes.event_c31,
                         anim_setup=anim_setup_p3,
                         anim_start=anim_start_p3,
                         anim_end=anim_end_n3b,
                         anim_end_alt=anim_end_n3b_alt,
                         correction=True,
                         correction_no='images/corrections/barriere_trou_no.png',
                         correction_yes='images/corrections/barriere_trou_yes.png',
                         correction_img=ImageWrap(source='images/corrections/barriere_trou.png',
                                                  size=(19, 28),
                                                  pos=(sizes.event_c31)))
    t3 = ImageWrap(pos=sizes.pos_c3,
                   size=sizes.size_c3,
                   source='images/animations/zones/mur.zip')
    c3 = Category(name=txt.txt_cat_fence,
                  element1=n3a, element2=n3b, target=t3)

    def anim_setup_p4():
        animal = ImageWrap(
            pos=(sizes.width, sizes.height / 10),
            size=(75, 85),  # (64,36) for marche
            source='images/animations/terrasses/musaraigne_marche.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_start_p4():
        return Animation(pos=sizes.event_c4_step1, duration=duration_start)

    def anim_end_p4(animal):
        anim = Animation(pos=sizes.event_c4_step2, duration=duration_end * 0.5)
        anim += Animation(pos = sizes.event_c4_step3, duration=duration_end * 0.5)
        anim += Animation(x=sizes.width_ref, y=sizes.height / 3, duration=duration_end * 0.8)
        return anim

    def anim_end_n4(animal):
        def forward(a, i):
            animal.image.source = 'images/scenery/transparency.png'

        animal.image.source = 'images/animations/terrasses/musaraigne_flambe.zip'
        animal.image.anim_delay = 0.2
        animal.image.anim_loop = 1
        anim = Animation(pos=sizes.event_c4_step2, duration=duration_end)
        anim.start(animal.image)

        wait = Animation(duration=duration_end)
        wait.bind(on_complete=forward)
        return wait

    p4 = ElementScatter(name=txt.txt_cat_floor_grass,
                        first=rand_elem(),
                        source='images/non_animes/terrasse_pave_drainant.png',
                        txt_info=txt.txt_info_floor_grass,
                        info_img="images/photos/terrasses.jpg",
                        event_pos=sizes.event_c4_step1,
                        anim_setup=anim_setup_p4,
                        anim_start=anim_start_p4,
                        anim_end=anim_end_p4)
    n4 = ElementScatter(name=txt.txt_cat_floor_stone,
                        first=not p4.first,
                        positive=False,
                        positive_ref=p4,
                        source='images/non_animes/terrasse_gres_noir.png',
                        txt_info = txt.txt_info_floor_stone,
                        info_img="images/photos/terrasses.jpg", #"images/scenery/transparency.png",
                        event_pos=sizes.event_c4_step1,
                        anim_setup=anim_setup_p4,
                        anim_start=anim_start_p4,
                        anim_end=anim_end_n4,
                        correction=False)
    t4 = ImageWrap(pos=sizes.pos_c4,
                   size=sizes.size_c4,
                   source='images/animations/zones/terrasse.zip')
    c4 = Category(name=txt.txt_cat_floor,
                  element1=p4, element2=n4, target=t4)

    def anim_setup_p5():
        animal = ImageWrap(
            pos=(sizes.width / 2 + 140, sizes.height_ref),
            size=(52, 44),
            source='images/animations/abris/herisson_marche.zip',
            anim_delay=0.1)
        frame.add_widget(animal, 2)
        return animal

    def anim_setup_n5():
        animal = ImageWrap(
            pos=(sizes.width / 2, sizes.height_ref),
            size=(55, 56),
            source='images/animations/abris/abeille.zip',
            anim_delay=0.05)
        frame.add_widget(animal)
        return animal

    def anim_start_p5():
        return Animation(pos=sizes.event_c5, duration=duration_start * 1.5)

    def anim_start_n5():
        return Animation(pos=sizes.event_c5, duration=duration_start * 0.5)

    def anim_end_p5(animal):
        animal.image.source = 'images/animations/abris/herisson_zzz.zip'
        f = 0.5
        n = 7
        animal.image.anim_delay = f
        animal.image.size = (133, 84)


        #put back the "animal" zzz in front
        frame.remove_widget(animal)
        frame.add_widget(animal)
        return Animation(duration= (n-1) * f * 2)

    def anim_end_n5(animal):
        a2 = ImageWrap(
            pos=(sizes.width / 2 - 370, sizes.height_ref),
            size=(55, 56),
            source='images/animations/abris/abeille.zip',
            anim_delay=0.05)
        a3 = ImageWrap(
            pos=(sizes.width / 2 - 150, sizes.height_ref),
            size=(55, 56),
            source='images/animations/abris/abeille.zip',
            anim_delay=0.05)
        frame.add_widget(a2)
        frame.add_widget(a3)

        def after(a, i):
            frame.remove_widget(a2)
            frame.remove_widget(a3)
            animal.flip()
            pass


        m = 1.8
        f = m / 3.0

        def forward(a, i):
            animal.flip()
            d_end = duration_end * (m - 2 * f)
            anim = Animation(pos=(sizes.width * 2 / 3 + 100, sizes.height), duration=d_end)
            anim.start(animal.image)
            anim = Animation(pos=(sizes.width * 2 / 3 - 150, sizes.height), duration=d_end)
            anim.start(a2.image)
            anim = Animation(pos=(sizes.width * 2 / 3 - 450, sizes.height), duration=d_end)
            anim.start(a3.image)
            anim.bind(on_complete=after)

        anim = Animation(x=animal.image.x - 10, y=animal.image.y + 10, duration=duration_end * f)
        anim += Animation(x=animal.image.x - 20, y=animal.image.y - 10, duration=duration_end * f)
        anim2 = Animation(x=animal.image.x - 15, y=animal.image.y - 10, duration=duration_end * f)
        anim2 += Animation(x=animal.image.x - 35, y=animal.image.y + 10, duration=duration_end * f)
        anim3 = Animation(x=animal.image.x + 5, y=animal.image.y - 50, duration=duration_end * f)
        anim3 += Animation(x=animal.image.x - 10, y=animal.image.y - 35, duration=duration_end * f)

        anim.bind(on_complete=forward)
        anim.start(animal.image)
        anim2.start(a2.image)
        anim3.start(a3.image)

        wait = Animation(duration=duration_end * m)
        return wait

    p5 = ElementScatter(name=txt.txt_cat_shelter_wood,
                        first=rand_elem(),
                        source='images/non_animes/tas_de_bois.png',
                        txt_info=txt.txt_info_shelter_wood,
                        info_img="images/photos/bois.jpg",
                        event_pos=sizes.event_c5,
                        anim_setup=anim_setup_p5,
                        anim_start=anim_start_p5,
                        anim_end=anim_end_p5)
    n5 = ElementScatter(name=txt.txt_cat_shelter_flower,
                        first=not p5.first,
                        source='images/non_animes/prairie_fleurie.png',
                        txt_info=txt.txt_info_shelter_flower,
                        info_img="images/photos/prairie.jpg",
                        event_pos=sizes.event_c5,
                        anim_setup=anim_setup_n5,
                        anim_start=anim_start_n5,
                        anim_end=anim_end_n5)
    t5 = ImageWrap(pos=sizes.pos_c5,
                   size=sizes.size_c5,
                   source='images/animations/zones/abris.zip')
    c5 = Category(name=txt.txt_cat_shelter,
                  element1=p5, element2=n5, target=t5)

    def anim_setup_p6():
        animal = ImageWrap(
            pos=(sizes.pos_c6),
            size=(sizes.size_c6),
            source='images/animations/animaux/chevre.zip',
            anim_delay=0.4)
        frame.add_widget(animal)
        frame.remove_widget(frame.static)
        return animal

    def anim_setup_n6():
        animal = ImageWrap(
            pos=(sizes.pos_c6),
            size=(sizes.size_c6_cat),
            source='images/animations/animaux/chat_marche.zip',
            anim_delay=0.3)
        frame.add_widget(animal, 2)
        frame.remove_widget(frame.static)
        return animal

    def anim_start_p6():
        frame.tree.image.source = 'images/non_animes/arbre_oiseau.png'
        return Animation(pos=sizes.event_c6, duration=duration_start)

    def anim_start_n6():
        frame.tree.image.source = 'images/non_animes/arbre_oiseau.png'
        anim = Animation(pos=sizes.event_c6, duration=duration_start)
        return anim

    def anim_end_p6(animal):
        def papillon1 (a, i):
            anim = Animation(x=pap.image.x + 5, y = pap.image.y + 5, duration=duration_end * 0.1)
            anim += Animation(x=pap.image.x - 5, y=pap.image.y + 5, duration=duration_end * 0.1)
            anim += Animation(x=pap.image.x + 5, y=pap.image.y - 5, duration=duration_end * 0.1)
            anim += Animation(x=pap.image.x - 5, y=pap.image.y - 5, duration=duration_end * 0.1)
            anim += Animation(x=pap.image.x, y=pap.image.y, duration=duration_end * 0.1)
            anim.bind(on_complete=papillon1)
            anim.start(pap.image)

        def after(a, i):
            animal.image.source = 'images/scenery/transparency.png'

            # replace animal by static (animal is removed)
            frame.static.image.source = 'images/animations/animaux/chevre_mange_loop.zip'
            frame.static.image.anim_delay = 0.3
            frame.static.image.anim_loop = 0
            frame.static.image.pos = animal.image.pos
            frame.static.image.size = animal.image.size
            frame.add_widget(frame.static, 2)

        animal.image.source = 'images/animations/animaux/chevre_mange_intro.zip'
        animal.image.pos = (sizes.event_c6[0] - 15, sizes.event_c6[1])

        f = 11
        d = 0.3
        animal.image.anim_delay = d
        animal.image.anim_loop = 1
        anim = Animation(duration=(f - 1) * d)
        anim.bind(on_complete=after)
        anim.start(animal.image)

        pap = ImageWrap(
            pos=(sizes.width / 3, sizes.height_ref),
            size=(50, 65),
            source='images/animations/fleurs/papillon_rouge.zip',
            anim_delay=0.1)
        pap.flip()
        frame.add_widget(pap)
        animp = Animation(pos=sizes.event_c6, duration= (f - 1) * d)
        animp.bind(on_complete=papillon1)
        animp.start(pap.image)

        wait = Animation(duration= f * d + duration_end * 0.7)
        return wait

    def anim_end_n6(animal):
        return anim_end_n6_internal(animal)

    def anim_end_n6_internal(animal, recover=False):
        def after(a, i):
            animal.image.source = 'images/scenery/transparency.png'
            animal.image.anim_loop = 0

            # replace animal by static (animal is removed)
            frame.static.image.source = 'images/animations/animaux/chat_couche_loop.zip'
            frame.static.image.anim_delay = 0.1
            frame.static.image.anim_loop = 0
            frame.static.image.pos = animal.image.pos
            frame.static.image.size = animal.image.size
            frame.static.image.flip()
            frame.add_widget(frame.static)

            if recover:
                frame.cat_reverse = False
            else:
                frame.cat = frame.static.image
                frame.cat_reverse = True

        def forward(a, i):
            animal.image.source = 'images/animations/animaux/chat_couche_intro.zip'
            animal.image.anim_delay = 0.1
            animal.image.size = sizes.size_c6_cat
            #animal.image.pos = (sizes.event_c6[0] - 161, sizes.event_c6[1] - 7)
            animal.image.anim_loop = 1

            animal.image.flip()
            if (recover):
                animal.image.pos = (sizes.event_c6[0] + 5, sizes.event_c6[1] - 7)
                frame.tree.image.source = 'images/non_animes/arbre_oiseau.png'
            else:
                animal.image.pos = (sizes.event_c6[0] + 49 - 5, sizes.event_c6[1] - 7)

                frame.tree.image.source = 'images/non_animes/arbre_plume.png'
            f = 4
            d = 0.1
            animal.image.anim_delay = d
            anim = Animation(duration=f * d)
            anim.bind(on_complete=after)
            anim.start(animal.image)

        frame.tree.image.source = 'images/scenery/transparency.png'

        if (recover):
            animal.image.source = 'images/animations/animaux/chat_grimpe_fail.zip'
            f = 16
        else:
            animal.image.source = 'images/animations/animaux/chat_grimpe.zip'
            f = 17

        animal.image.size = (274, 245)
        animal.image.pos = (sizes.width_left_margin + 350, 175)

        animal.image.anim_loop = 1

        d = 0.1
        animal.image.anim_delay = d

        anim = Animation(duration=f * d)
        anim.bind(on_complete=forward)
        anim.start(animal.image)

        sound_cat.play()

        wait = Animation(duration=(f + 4) * d + 1.5)
        return wait

    def anim_end_n6_alt(animal):
        return anim_end_n6_internal(animal, True)

    p6 = ElementScatter(name=txt.txt_cat_animal_goat,
                        first=rand_elem(),
                        source='images/animations/animaux/chevre.zip',
                        txt_info=txt.txt_info_animal_goat,
                        info_img='images/photos/chevres.jpg',
                        event_pos=sizes.event_c6,
                        anim_setup=anim_setup_p6,
                        anim_start=anim_start_p6,
                        anim_end=anim_end_p6)
    n6 = ElementScatter(name=txt.txt_cat_animal_cat,
                        first=not p6.first,
                        positive=False,
                        positive_ref=p6,
                        source='images/animations/animaux/chat_marche.zip',
                        txt_info=txt.txt_info_animal_cat,
                        info_img="images/scenery/transparency.png",
                        txt_info_alt=txt.txt_info_animal_cat_sol,
                        info_img_alt='images/photos/chats.jpg',
                        event_pos=sizes.event_c6,
                        anim_setup=anim_setup_n6,
                        anim_start=anim_start_n6,
                        anim_end=anim_end_n6,
                        anim_end_alt=anim_end_n6_alt,
                        correction=True,
                        correction_no='images/corrections/arbre_cone_no.png',
                        correction_yes='images/corrections/arbre_cone_yes.png',
                        correction_img=ImageWrap(source='images/corrections/arbre_cone.png',
                                                 size=(48, 29),
                                                 pos=(sizes.width_left_margin + 454 - 10 - 19, 225 + 22)))
    t6 = ImageWrap(pos=sizes.pos_c6,
                   size=sizes.size_c6,
                   source='images/animations/zones/animaux.zip')
    c6 = Category(name=txt.txt_cat_animal,
                  element1=p6, element2=n6, target=t6)

    def anim_setup_p7():
        animal = ImageWrap(
            pos=(sizes.width, sizes.height * 2 / 3),
            size=(50, 65),
            source='images/animations/fleurs/papillon_rouge.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_setup_n7():
        animal = ImageWrap(
            pos=(sizes.width, sizes.height * 2 / 3),
            size=(50, 65),
            source='images/animations/fleurs/papillon_jaune.zip',
            anim_delay=0.1)
        frame.add_widget(animal)
        return animal

    def anim_start_p7():
        return Animation(pos=sizes.event_c7, duration=duration_start * 0.5)

    def anim_end_p7(animal):
        a2 = ImageWrap(
            pos=(sizes.width, sizes.height * 2 / 3),
            size=(50, 65),
            source='images/animations/fleurs/papillon_rouge.zip',
            anim_delay=0.1)
        a3 = ImageWrap(
            pos=(sizes.width, sizes.height * 2 / 3 + 110),
            size=(50, 65),
            source='images/animations/fleurs/papillon_rouge.zip',
            anim_delay=0.1)
        a4 = ImageWrap(
            pos=(sizes.width, sizes.height * 2 / 3 - 70),
            size=(50, 65),
            source='images/animations/fleurs/papillon_jaune.zip',
            anim_delay=0.1)
        frame.add_widget(a2)
        frame.add_widget(a3)
        frame.add_widget(a4)

        def after(a, i):
            frame.remove_widget(a2)
            frame.remove_widget(a3)
            frame.remove_widget(a4)

        f = 0.6

        def forward(a, i):
            animal.image.source = 'images/animations/fleurs/papillon_rouge.zip'
            anim = Animation(x= sizes.width / 3, y =sizes.height, duration=duration_end * f)
            anim.bind(on_complete=after)
            anim.start(animal.image)
            anim = Animation(x=sizes.width / 3 + 260, y=sizes.height, duration=duration_end * f)
            anim.start(a2.image)
            anim = Animation(x=sizes.width / 3 + 120, y=sizes.height, duration=duration_end * f)
            anim.start(a3.image)
            anim = Animation(x=sizes.width / 3 + 70, y=sizes.height, duration=duration_end * f)
            anim.start(a4.image)

        animal.image.source = 'images/animations/fleurs/papillon_rouge_butine.zip'

        anim = Animation(x=animal.image.x - 10, y=animal.image.y + 10, duration=duration_end * f)
        anim += Animation(x=animal.image.x - 20, y=animal.image.y - 10, duration=duration_end * f)
        anim2 = Animation(x=animal.image.x - 15, y=animal.image.y - 10, duration=duration_end * f)
        anim2 += Animation(x=animal.image.x - 35, y=animal.image.y + 10, duration=duration_end * f)
        anim3 = Animation(x=animal.image.x + 5, y=animal.image.y + 5, duration=duration_end * f)
        anim3 += Animation(x=animal.image.x - 10, y=animal.image.y - 15, duration=duration_end * f)
        anim4 = Animation(x=animal.image.x + 5, y=animal.image.y - 25, duration=duration_end * f)
        anim4 += Animation(x=animal.image.x - 15, y=animal.image.y - 10, duration=duration_end * f)

        anim.bind(on_complete=forward)
        anim.start(animal.image)
        anim2.start(a2.image)
        anim3.start(a3.image)
        anim4.start(a4.image)

        wait = Animation(duration=duration_end * f * 3)
        return wait

    def anim_end_n7(animal):
        def after(a, i):
            animal.flip()

        animal.flip()
        anim = Animation(pos=(sizes.width, sizes.height * 2 / 3), duration=duration_end * 0.6)
        anim.bind(on_complete=after)
        return anim

    p7 = ElementScatter(name=txt.txt_cat_balcony_herbs,
                        first=rand_elem(),
                        source='images/non_animes/bac_herbes_aromatiques.png',
                        txt_info=txt.txt_info_balcony_herbs,
                        info_img="images/scenery/transparency.png", # TODO: change image here for herbes aromatiques
                        event_pos=sizes.event_c7,
                        anim_setup=anim_setup_p7,
                        anim_start=anim_start_p7,
                        anim_end=anim_end_p7)
    n7 = ElementScatter(name=txt.txt_cat_balcony_geranium,
                        first=not p7.first,
                        positive=False,
                        positive_ref=p7,
                        source='images/non_animes/bac_geraniums.png',
                        txt_info=txt.txt_info_balcony_geranium,
                        info_img="images/scenery/transparency.png",
                        event_pos=sizes.event_c7,
                        anim_setup=anim_setup_n7,
                        anim_start=anim_start_p7,
                        anim_end=anim_end_n7,
                        correction=False)
    t7 = ImageWrap(pos=sizes.pos_c7,
                   size=sizes.size_c7,
                   source='images/animations/zones/fleurs.zip')
    c7 = Category(name=txt.txt_cat_balcony_plants,
                  element1=p7, element2=n7, target=t7)

    categories = {c1, c2, c3, c4, c5, c6, c7}
    categories = random.sample(categories, categories.__len__())
    return categories
