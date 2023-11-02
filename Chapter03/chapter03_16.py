import glob 
from PIL import Image

class GifConverter: 

    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.git'
    
    def convert_git(self):
        print(self.path_in, self.path_out)

        img, *images = \
            [Image.open(f).resize((320,240), Image.ADAPTIVE) for f in sorted(glob.glob(self.path_in))]

        try :
            img.save(
            fp=self.path_out,
            format='GIF', 
            append_images = images, 
            save_all= True,
            loop = 0,
            duration=500
            )
        except IOError : 
            print('Can not convert')


if __name__ == '__main__':
    # PATH_IN = './Chapter03/Chapter03_resource/images_in/*.png'
    # PATH_OUT = './Chapter03/Chapter03_resource/images_out/result.png'
    # img, *images = [Image.open(f).resize((320,240), Image.ADAPTIVE) for f in sorted(glob.glob(PATH_IN))]
    print("="*6)    
    # img.save(
    #     fp=PATH_OUT,
    #     format='GIF', 
    #     append_images = images, 
    #     save_all= True,
    #     loop = 0,
    #     duration=500
    # )

    c = GifConverter('./Chapter03/Chapter03_resource/images_in/*.png', './Chapter03/Chapter03_resource/images_out/result.gif', (320, 240))
    c.convert_git()