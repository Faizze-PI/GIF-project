import imageio.v3 as iio

cat_images = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

for cat_photo in cat_images:
    images.append(iio.imread(cat_photo))

iio.imwrite('nyan_cat.gif', images, duration=100, loop=0)
