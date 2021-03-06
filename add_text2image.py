import pandas as pd
from pathlib import Path
from sys import exit



pd.set_option('display.max_colwidth', 99999)
pd.set_option('display.max_columns', 20)
pd.options.display.float_format = '{:.0f}'.format


class Database:
    # Contructor
    def __init__(self, path, sheet_names):
        self.sheets = self.load_dtb(path, sheet_names) # a dict to contain all sheets data frame
    # load dtb from excel or pickle files
    @staticmethod
    def load_dtb(path, sheet_names):
        # create data frames from pickle files if not create pickle files
        sheets = {}
        filename = Path(path).stem # get file name of ymme path
        pickled_dir_path = 'taboo_database'
        for sheet_name in sheet_names:
            # print('Processing ' + filename + '_sheet_' + sheet_name)
            # read pickle data
            try: 
                pickled_fpath = str(pickled_dir_path) + '\\' + filename + '_sheet_' + sheet_name
                print('read picked files: ', pickled_fpath)
                sheets[sheet_name] = pd.read_pickle(pickled_fpath)
            
            # if failed to read => read excel file and write pickle
            except FileNotFoundError as e:
                print('read excel files: ', path)
                sheets[sheet_name] = pd.read_excel(path, 
                                                   sheet_name=sheet_name, 
                                                   header=0, 
                                                   na_values='#### not defined ###', 
                                                   keep_default_na=False)

                pickled_fpath = str(pickled_dir_path) + '\\' + filename + '_sheet_' + sheet_name
                print('write picked files', pickled_fpath)
                sheets[sheet_name].to_pickle(pickled_fpath)
        return sheets

taboo_database = Database('taboo_database\\taboo_database.xlsx', ['taboo_database'])
df = taboo_database.sheets['taboo_database']


# import required classes
from PIL import Image, ImageDraw, ImageFont

 

def draw_word(draw_object, word, color, font, y_position):
    # draw guess word
    size = font.getsize(word)
    (x, y) = ((500 - size[0])/2, y_position)
    draw_object.text((x, y), word, align='left', fill=color, font=font)






for index, row in df.iterrows():
    # create Image object with the input image
    image = Image.open('taboo_template.jpg')
    # initialise the drawing context with
    # the image object as background
    draw_object = ImageDraw.Draw(image)


    word=row['guess word']
    color = 'rgb(255,255,255)' # white color
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=50)


    color = 'rgb(0,0,0)' # black color
    word=row['taboo word 1']
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=150)


    color = 'rgb(0,0,0)' # black color
    word=row['taboo word 2']
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=240)


    color = 'rgb(0,0,0)' # black color
    word=row['taboo word 3']
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=330)


    color = 'rgb(0,0,0)' # black color
    word=row['taboo word 4']
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=420)


    color = 'rgb(0,0,0)' # black color
    word=row['taboo word 5']
    # create font object with the font file and specify
    font = ImageFont.truetype('Roboto\\Roboto-Bold.ttf', size=45)
    draw_word(draw_object, word, color, font, y_position=510)


    # save the edited image
    image.save('cards\\' + word + '.jpg')

    break