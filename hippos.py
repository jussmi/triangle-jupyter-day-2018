'''A module for hippos...'''
from IPython.display import Image
import random
import time
from tqdm.autonotebook import tqdm
from typing import List

IMAGE_PATH = 'static/'
IMAGE_LIST = ['hippos_balloons.jpg', 'real_hippo_open_mouth.jpg', 
              'hippo_banana.jpg', 'hippopotamuse.jpg',
              'hippo_reading.jpg']
PAGE_LIST = ['berserk_try_two.jpg',
             'one_hippo.jpg',
             'seven_arrive_in_a_sack.jpg',
             'two_hippos_arrive.jpg'
]
BERSERK_IMAGE = 'hippos_berserk.jpg'
COVER_IMAGE = 'hippos_cover.jpg'

class Hippo(object):
    '''A hippo class.'''
    def __init__(self, arrival_method, attire, purpose):
        '''Initializes a new hippo to attend the party.
        
        Parameters
        ----------
        arrival_method : str
            How the hippo arrives to the party
        attire : str
            How the hippo is dressed
        purpose : str
            Here to work or here to party?
            
        Attributes
        ----------
        arrival_method : str
            How the hippo arrives to the party
        attire : str
            How the hippo is dressed
        purpose : str
            Here to work or here to party?
        '''
        self.arrival_method = arrival_method
        self.attire = attire
        self.purpose = purpose
        
    def go_berserk(self):
        '''If the hippo doesn't have to work, they'll go berserk!'''
        actions = ['Celebrate!', 'Rumpus!', 'Dance!', 'Stand.']
        if self.purpose == 'work':
            print("Can't berserk, have to work.")
        else:
            print(random.choice(actions))
            
    def leave(self):
        pass
    
def a_long_running_function(seconds: int) -> int:
    '''Sleeps for the seconds passed and returns the square.'''
    print('This might take some time.')
    for second in tqdm(range(seconds)):
        time.sleep(1)
    print('Returning the stuff!')
    return seconds*seconds


def a_function_with_a_problem():
    '''This function just takes up space and raises an error.'''
    print('Doing stuff and taking space')
    raise ValueError('This function is broken')
    print('It worked!')
    
def make_hippos() -> List[Hippo]:
    '''Makes all the hippo objects from the book.'''
    hippos = []
    
    criteria = [('host', 'birthday suit', 'party!'),
                ('called', 'bowtie', 'party!'),
                ('called', 'hair flower', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'suit and tie', 'party!'),
                ('front door', 'suit and tie', 'party!'),
                ('front door', 'suit and tie', 'party!'),
                ('front door', 'gown', 'party!'),
                ('front door', 'gown', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('in a sack', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('sneak in the back', 'birthday suit', 'party!'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work'),
                ('front door', 'birthday suit', 'work')]
    
    for criterium in criteria:
        hippos.append(Hippo(*criterium))
        
    return hippos

def all_the_hippos_go_berserk(hippos: List[Hippo]):
    '''ALL THE HIPPOS GO BERSERK!'''
    display(Image(IMAGE_PATH+BERSERK_IMAGE))
    hippo_copy = hippos.copy()
    random.shuffle(hippo_copy)
    for hippo in hippo_copy:
        hippo.go_berserk()
        
def display_cover_image():
    full_image_path = IMAGE_PATH+COVER_IMAGE
    display(Image(full_image_path))


def display_a_random_image(image_list: List[str]=IMAGE_LIST):
    full_image_path = IMAGE_PATH+random.choice(image_list)
    display(Image(full_image_path))
    
def display_a_random_page(image_list: List[str]=PAGE_LIST):
    full_image_path = IMAGE_PATH+random.choice(image_list)
    display(Image(full_image_path))
    
def closing_image():
    full_image_path = IMAGE_PATH+'real_hippo_open_mouth.jpg'
    display(Image(full_image_path))
        

if __name__ != '__main__':
#     display_a_random_page(IMAGE_LIST)
    pass