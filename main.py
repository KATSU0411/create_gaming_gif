import cv2
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

filepath = "input/"
imgname = "thumbsup"
frame = 20
hsvL = np.array([0, 50, 50])
hsvU = np.array([180, 255, 255])
duration = 80

check = True

def main():

    img = cv2.imread("{0}{1}.png".format(filepath, imgname))

    mask = hsvExtraction(img, hsvL, hsvU)
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    if check:
        cv2.imshow("mask", masked_img)
        cv2.waitKey(0)

    imgs = []
    for i in range(0, frame):
        img4 = move_Hue(masked_img, (180.0/frame) * i)
        img5 = pasting(img, img4, mask)
        # img6 = invisible(img5, mask)
        imgs.append(img5)

    pil_imgs = all_cv2pil(imgs)

    pil_img = Image.open("{0}{1}.png".format(filepath, imgname))

    shapes = cv2.imread("{0}{1}.png".format(filepath, imgname), cv2.IMREAD_UNCHANGED).shape[2]

    if shapes == 4:
        alpha = pil_img.split()[3]
        pil_img = pil_img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <= 1 else 0)
        save_gif_with_alpha(pil_imgs, mask)

    else:
        save_gif(pil_imgs)


def invisible(img, mask):
    img = cv2pil(img)
    mask = cv2pil(mask)

    img_a = img.copy()
    img_a.putalpha(mask)
    return img_a

def hsvExtraction(image, hsvLower, hsvUpper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 画像をHSVに変換
    if hsvLower[0] <= 0:
        mask1 = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
        hsvLower[0] = hsvLower[0] % 180
        hsvUpper[0] = 180
        print(hsvLower, hsvUpper)
        mask2 = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
        hsv_mask = mask1 | mask2
    else:
        hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成

    return hsv_mask

def move_Hue(img, hue):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSVに変換
    hsv = hsv.astype(np.uint16)  # uint8だと255以上で不定になるので型を変更
    hsv[:, :, 0] = (hsv[:, :, 0] + hue) % 180  # 回転処理
    hsv = hsv.astype(np.uint8)  # 型を戻す
    dst = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return dst

def pasting(img, roted_img, mask):
    inv_mask = cv2.bitwise_not(mask)
    inv_masked = cv2.bitwise_and(img, img, mask=inv_mask)

    adding = cv2.bitwise_or(inv_masked, roted_img)

    return adding

def all_cv2pil(imgs):
    pil_imgs = []
    for img in imgs:
        pil_imgs.append(cv2pil(img))

    return pil_imgs

def save_gif_with_alpha(imgs, mask):
    if check:
        mask.show()

    pasted = []
    for img in imgs:
        img = img.convert('RGBA')
        img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        img.paste(255,mask)
        pasted.append(img)

    # imgs[0].save("out.gif", save_all=True, append_images=imgs[1:], duration=80, loop=0, optimize=False)
    pasted[0].save("output/{0}gaming_{1}.gif".format(filepath, imgname), save_all=True, append_images=pasted[1:], duration=duration, loop=0, optimize=False, transparency=255)

def save_gif(imgs):
    # imgs[0].save("out.gif", save_all=True, append_images=imgs[1:], duration=80, loop=0, optimize=False)
    imgs[0].save("output/{0}gaming_{1}.gif".format(filepath, imgname), save_all=True, append_images=imgs[1:], duration=duration, loop=0, optimize=False)

def cv2pil(img):
    ''' OpenCV型 -> PIL型 '''
    new_image = img.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image



main()
