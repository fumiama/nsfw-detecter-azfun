import json
from io import BytesIO
from pathlib import Path

import tensorflow as tf
import tensorflow.keras as keras

SIZE = 256
DEVICE = "/CPU:0"

tags = ["1girl",
        "solo",
        "long_hair",
        "breasts",
        "blush", "looking_at_viewer", "smile", "short_hair", "open_mouth", "bangs", "blue_eyes", "multiple_girls",
        "blonde_hair", "skirt", "brown_hair", "large_breasts", "simple_background", "black_hair",
        "eyebrows_visible_through_hair", "thighhighs", "hair_ornament", "hat", "red_eyes", "gloves", "shirt", "1boy",
        "dress", "white_background", "ribbon", "long_sleeves", "bow", "navel", "brown_eyes", "cleavage", "animal_ears",
        "twintails", "holding", "medium_breasts", "bare_shoulders", "underwear", "sitting", "hair_between_eyes",
        "school_uniform", "very_long_hair", "jewelry", "green_eyes", "nipples", "blue_hair", "panties", "closed_mouth",
        "standing", "purple_eyes", "monochrome", "collarbone", "black_legwear", "hair_ribbon", "swimsuit",
        "closed_eyes", "tail", "comic", "jacket", "weapon", "yellow_eyes", "ponytail", "full_body", "purple_hair",
        "ass", "pink_hair", "greyscale", "braid", "flower", "silver_hair", "ahoge", "hair_bow", "upper_body", ":d",
        "short_sleeves", "white_shirt", "pantyhose", "heart", "bikini", "hetero", "male_focus", "nude", "pleated_skirt",
        "hairband", "red_hair", "boots", "sweat", "small_breasts", "sidelocks", "cowboy_shot", "lying", "thighs",
        "earrings", "white_hair", "detached_sleeves", "censored", "japanese_clothes", "food", "one_eye_closed",
        "green_hair", "wings", "multiple_boys", "frills", "white_legwear", "glasses", "multicolored_hair",
        "parted_lips", "necktie", "shoes", "sky", "open_clothes", "serafuku", "penis", "barefoot", "outdoors", "horns",
        "shorts", "pussy", "solo_focus", "day", "tongue", "sleeveless", "elbow_gloves", "alternate_costume", "choker",
        "striped", "teeth", "pointy_ears", "hairclip", "fang", "midriff", "sword", "looking_back", "black_gloves",
        "shiny", "tears", "belt", "puffy_sleeves", "cloud", "cat_ears", "white_gloves", "cum", "pants", "hair_flower",
        "spread_legs", "dark_skin", "miniskirt", "indoors", "2boys", "collared_shirt", "fingerless_gloves", "on_back",
        "sex", "hood", "wide_sleeves", "tongue_out", "pink_eyes", "armpits", "kimono", "grey_hair", "blunt_bangs",
        "sailor_collar", "black_skirt", "hand_up", "chibi", "bowtie", "water", "clothes_lift", "scarf", "cape",
        "star_(symbol)", "bag", "uniform", "yuri", "white_panties", "bra", "armor", "socks", "from_behind", "sweatdrop",
        "orange_hair", "necklace", "grey_background", "character_name", ":o", "rabbit_ears", "off_shoulder",
        "twitter_username", "black_eyes", "virtual_youtuber", "huge_breasts", "apron", "nail_polish", "white_dress",
        "grin", "flat_chest", "stomach", "hair_over_one_eye", "side_ponytail", "holding_weapon", "twin_braids",
        "medium_hair", "covered_nipples", "black_footwear", "mole", "vest", "vaginal", "high_heels", "aqua_eyes",
        "looking_at_another", "dated", "collar", "arms_up", "bracelet", "arm_up", "red_bow", "mosaic_censoring",
        "blurry", "feet", "black_dress", "zettai_ryouiki", "sketch", "two_side_up", "shiny_hair", "sweater", "lips",
        "from_side", "tree", "dark-skinned_female", "cup", "leotard", "red_ribbon", "groin", "english_text",
        "speech_bubble", "head_tilt", "puffy_short_sleeves", "two-tone_hair", "blue_skirt", "military", "shiny_skin",
        "blue_sky", "cat_tail", "wet", "fingernails", "gun", "book", "v-shaped_eyebrows", "kneehighs", "hand_on_hip",
        "neckerchief", "open_jacket", "wrist_cuffs", "torn_clothes", "maid", "plaid", "pillow", "legs", "gradient",
        "coat", "cosplay", "orange_eyes", "maid_headdress", "sash", "petals", "sleeves_past_wrists", "black_panties",
        "dutch_angle", "see-through", "pubic_hair", "one-piece_swimsuit", "loli", "fur_trim", "open_shirt", "ascot",
        "grey_eyes", "kneeling", "military_uniform", "gradient_background", "hug", "looking_to_the_side",
        "black_jacket", "4koma", "parted_bangs", "no_bra", "dress_shirt", "bare_arms", "short_shorts", "areolae",
        "symbol-shaped_pupils", "aqua_hair", "sparkle", "no_humans", "single_braid", "bare_legs", "crop_top", "window",
        "saliva", "bed", "clothing_cutout", "fox_ears", "double_bun", "bell", "animal_ear_fluff", "bodysuit", "v",
        "eyelashes", "hands_up", "no_panties", "blood", "streaked_hair", "mole_under_eye", "uncensored", "profile",
        "pussy_juice", "witch_hat", "sideboob", "strapless", "hoodie", "makeup", "underboob", "black_ribbon",
        "leaning_forward", "fruit", "alternate_hairstyle", "bar_censor", "capelet", "sleeveless_shirt", ":3",
        "headband", "^_^", "skindentation", "headgear", "bottomless", "cameltoe", "black_shirt", "side-tie_bikini",
        "mask", "black_bow", "covered_navel", "cum_in_pussy", "depth_of_field", "tattoo", "night", "headphones",
        "black_headwear", "sleeveless_dress", "anus", "neck_ribbon", "holding_hands", "gradient_hair", "glowing",
        "muscular", "detached_collar", "multiple_views", "chain", "siblings", "rose", "nose_blush", "shadow",
        "umbrella", "thigh_strap", "bed_sheet", "fox_tail", "floating_hair", "blue_dress", "facial_hair", "arm_support",
        "buttons", "red_skirt", "thigh_boots", "beret", "striped_legwear", "parody", "frown", "ocean",
        "traditional_media", "black_bikini", "low_twintails", "toes", "hair_tubes", "embarrassed", "turtleneck",
        "transparent_background", "one_side_up", "pantyshot", "wariza", "drill_hair", "halterneck", "mouth_hold",
        "heterochromia", "ass_visible_through_thighs", "from_above", "garter_straps", "swept_bangs", "back", "leaf",
        "plaid_skirt", "blush_stickers", "on_side", "magical_girl", "topless", "fangs", "eyebrows", "shirt_lift",
        "colored_skin", "chair", "bandages", "eating", "skirt_lift", "white_bikini", "blue_background", "obi",
        "grabbing", "on_bed", "scar", "pov", "eyepatch", "arms_behind_back", "clothes_pull", "wavy_mouth", "beach",
        "looking_away", "wavy_hair", "facial_mark", "thigh_gap", "bound", "cover", "chinese_clothes",
        "blurry_background", "short_dress", "moon", "flying_sweatdrops", "stuffed_toy", "crossed_arms", "highleg",
        "expressionless", "white_headwear", "hair_bun", "underwear_only", "brown_footwear", "heart-shaped_pupils",
        "blue_bow", "phone", "tentacles", "feet_out_of_frame", "sandals", "bdsm", "floral_print", "cat",
        "holding_sword", "leg_up", "soles", "school_swimsuit", "scrunchie", "looking_down", "lingerie", "from_below",
        "formal", "oral", "sunlight", "blazer", "bondage", "cleavage_cutout", "bat_wings", "cum_on_body",
        "female_pubic_hair", "thick_thighs"]

# print(len(tags))

with tf.device(DEVICE):
    base_model = keras.applications.resnet.ResNet50(include_top=False, weights=None, input_shape=(SIZE, SIZE, 3))
    model = keras.Sequential([
        base_model,
        keras.layers.Conv2D(filters=len(tags), kernel_size=(1, 1), padding='same'),
        keras.layers.BatchNormalization(epsilon=1.001e-5),
        keras.layers.GlobalAveragePooling2D(name='avg_pool'),
        keras.layers.Activation("sigmoid")
    ])
    model.load_weights(str(Path(__file__).parent/'weights.27-1.3988.h5'))


@tf.function
def process_data(content):
    img = tf.io.decode_jpeg(content, channels=3)
    img = tf.image.resize_with_pad(img, SIZE, SIZE)
    img = tf.image.per_image_standardization(img)
    return img


def predict(content: bytes):
    with tf.device(DEVICE):
        data = process_data(content)
        data = tf.expand_dims(data, 0)
        out = model(data)[0]
    return dict((tags[i], out[i].numpy()) for i in range(len(tags)))


def predict_file(file: BytesIO, limit: float):
    data = predict(file.read())
    ret = filter(lambda x: x[1] > limit, data.items())
    ret = map(lambda x: (x[0], float(x[1])), ret)
    return dict(ret)


if __name__ == '__main__':
    pass
