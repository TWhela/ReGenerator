import json
import random
import sys

eye_colors_all = ["Dead","Grey","Sulfur","Green","Copper","Hazel","Blue","RedDevil","Red","Iron","Brown","BrownDark"]
hair_colors_all = ["White","Platinum","Grey","Blonde","DirtyBlonde","Amber","Copper","Ruby","SaltAndBrown","Brown","SaltAndPepper","BlackBrown","Auburn","Black","Jet","TealBlonde","Yellow","Violet","Flame","Blue","Fuchsia","AquaPurple","Teal"]
hair_colors_natural = ["White","Platinum","Grey","Blonde","DirtyBlonde","Amber","Copper","Ruby","SaltAndBrown","Brown","SaltAndPepper","BlackBrown","Auburn","Black","Jet"]
hair_colors_non_eu = ["White", "Grey", "SaltAndBrown", "Brown", "SaltAndPepper", "BlackBrown", "Black", "Jet"]

jewelry_colors = ["No_Tint","Gold","Copper","Red","Green","Blue","Purple","Pink","Black"]

eyebrow_options = ["Sparse","Standard","Fluffy","Apart","Stern","ThinArched","ThickArched","ThinFlat","Sliced","Simple","Connected"]

hair_all = [
    "Faded_Afro",
    "Mullet",
    "Short_Ponytail_HairMesh",
    "Finger_Waves",
    "Cornrows_HairMesh",
    "Straight_Bob",
    "Whitney_Curls",
    "Cropped_Bang",
    "Bob",
    "Hairspray_Bob",
    "OldGuy_Business",
    "Viking_Braids",
    "Dreadlocks_HairMesh",
    "Even_Buzz_Back",
    "Ponytail_HairMesh",
    "Hollywood_curls",
    "Messy_Business",
    "Unkempt",
    "Top_Bun",
    "Cropped",
    "Coily_Mohawk",
    "Natural_Fade",
    "Short_Afro",
    "Shaggy",
    "Flat_Top",
    "Messy_Bob",
    "Spiked",
    "Business",
    "Buzz_Mohawk",
    "High_and_Tight",
    "Wavy_Business",
    "CyberFade",
    "Tousled_Bob",
    "Mullet_Mohawk",
    "Undercut",
    "None",
    "Choppy_Bob",
    "Receding_Wizard",
    "Short_Loc",
    "Messy_Updo"
]

hair_male = [
    "Faded_Afro",
    "Mullet",
    "Cornrows_HairMesh",
    "OldGuy_Business_Receded",
    "OldGuy_Business",
    "Dreadlocks_HairMesh",
    "Even_Buzz_Back",
    "Messy_Business",
    "Unkempt",
    "Cropped",
    "Natural_Fade",
    "Short_Afro",
    "Flat_Top",
    "Spiked",
    "Business",
    "Buzz_Mohawk",
    "High_and_Tight",
    "Wavy_Business",
    "CyberFade",
    "Mullet_Mohawk",
    "Undercut",
    "None",
    "Receding_Wizard",
]

hair_female = [
    "Mullet",
    "Short_Ponytail_HairMesh",
    "Finger_Waves",
    "Cornrows_HairMesh",
    "Straight_Bob",
    "Whitney_Curls",
    "Cropped_Bang",
    "Bob",
    "Hairspray_Bob",
    "Viking_Braids",
    "Dreadlocks_HairMesh",
    "Ponytail_HairMesh",
    "Hollywood_curls",
    "Unkempt",
    "Top_Bun",
    "Cropped",
    "Coily_Mohawk",
    "Shaggy",
    "Messy_Bob",
    "Tousled_Bob",
    "None",
    "Choppy_Bob",
    "Short_Loc",
    "Messy_Updo"
]

beard_options = [
    "none",
    "Wildman",
    "ChinCurtain",
    "PirateThin",
    "ClassicBeard",
    "CleanThin",
    "PatchStache",
    "PirateThick",
    "PaintersMoustache",
    "BeardStache",
    "ChinFade",
    "HeavyStubble",
    "Goatee",
    "PencilMoustache",
    "Wolfchops",
    "Stubble_Light",
    "Stubble_Heavy",
    "Stubble_Patchy",
    "Patchy",
    "Full_rugged"
]

jewelry_options = [
    "none"
    "Hoops",
    "Lobe_Diamond",
    "Double_Earrings_Left",
    "Bridge_01",
    "Bridge_02",
    "Double_Earrings",
    "Double_Earrings_Right",
    "Lobe_Gauge",
    "Nostril_Ball",
    "Nostril_Ball_Left",
    "Nostril_Ball_Right",
    "Rings_Assorted",
    "Rings_Assorted_Left",
    "Rings_Assorted_Right",
    "Septum_01",
    "Septum_02",
    "Septum_03"
]

makeup_colors = [
    "NONE",
    "Red_True",
    "Red",
    "Red_2",
    "Red_Max",
    "Red_Pink",
    "Red_Dark",
    "Pink",
    "Pink_Subtle",
    "Orange",
    "Orange_Bright",
    "Orange_Petrov",
    "Orange_Petrov_2",
    "Clay",
    "Clay_Dark",
    "Grey_Light",
    "Grey_Dark",
    "Brown_3",
    "Berry",
    "Blue_mid",
    "Berry_Dark",
    "Purple",
    "Purple_Dark",
    "Purple_Light",
    "Blue",
    "Blue_2",
    "Blue_Dark",
    "Teal",
    "Teal_2",
    "Teal_Deep",
    "Green",
    "Green_2",
    "Green_3",
    "Green_Deep",
    "Yellow",
    "White",
    "Brown",
    "Brown_Light",
    "Brown_Mid",
    "Brown_Dark",
    "Black"
]

tattoo_colors = [
    "NONE",
    "Black",
    "Brown",
    "Red",
    "Pink",
    "Blue",
    "Teal",
    "Green",
    "DarkBlue",
    "Henna"
]

face_paint_colors = [
    "NONE",
    "Black",
    "White",
    "Red_Oily_Petrov",
    "Red_Nose_Petrov",
    "Black_Grease",
    "Red_Grease",
    "Orange_Grease",
    "Yellow_Grease",
    "Green_Grease",
    "Teal_Grease",
    "Blue_Grease",
    "Purple_Grease",
    "Magenta_Grease",
    "Pink_Grease",
    "Red_Grease_Dark",
    "Orange_Grease_Dark",
    "Green_Grease_Dark",
    "Teal_Grease_Dark",
    "Blue_Grease_Dark",
    "Purple_Grease_Dark",
    "Magenta_Grease_Dark",
    "Pink_Grease_Light"
]

layer_options = {
    "Cheeks1": {
        "Sub": ["Blush", "Blush_Soft", "Blush_Sides"],
        "Col": makeup_colors
    },
    "Cheeks2": {
        "Sub": ["NONE","Blush_Upper","Blush_Soft_Small","Blush_Inner_Contour","Blush_Upper_Small"],
        "Col": makeup_colors
    },
    "Accents1": {
        "Sub": [
            "NONE",
            "Accents_UnderEyeBags",
            "Accents_SubtleEyeBags",
            "Accents_UnderEyeBags_Small",
            "Accents_UnderEyeCrease",
            "Accents_NasoLabialFolds",
            "Accents_ChinCleft",
            "Accents_CrowsFeet",
            "Accents_CrackedLips",
            "Accents_Lips",
            "Accents_RoughFace",
            "Accents_Moles_FaceNeck",
            "Accents_Moles_BaldHeadNeck",
            "Accents_Fullface_Wrinkles",
            "Accents_FullfaceMom_Wrinkles",
            "Blemish_VeinsMany"
        ],
        "Col": []
    },
    "Accents2": {
        "Sub": [
            "NONE",
            "Accents_UnderEyeBags",
            "Accents_SubtleEyeBags",
            "Accents_UnderEyeBags_Small",
            "Accents_UnderEyeCrease",
            "Accents_NasoLabialFolds",
            "Accents_ChinCleft",
            "Accents_CrowsFeet",
            "Accents_CrackedLips",
            "Accents_Lips",
            "Accents_RoughFace",
            "Accents_Moles_FaceNeck",
            "Accents_Moles_BaldHeadNeck",
            "Accents_Fullface_Wrinkles",
            "Accents_FullfaceMom_Wrinkles",
            "Blemish_VeinsMany"
        ],
        "Col": []
    },
    "ColorlessAccents1": {
        "Sub": [
            "NONE",
            "Accents_UnderEyeBags",
            "Accents_SubtleEyeBags",
            "Accents_UnderEyeBags_Small",
            "Accents_UnderEyeCrease",
            "Accents_NasoLabialFolds",
            "Accents_ChinCleft",
            "Accents_CrowsFeet",
            "Accents_CrackedLips",
            "Accents_Lips",
            "Accents_RoughFace",
            "Accents_Moles_FaceNeck",
            "Accents_Moles_BaldHeadNeck",
            "Accents_Fullface_Wrinkles",
            "Accents_FullfaceMom_Wrinkles",
            "Blemish_VeinsMany"
        ],
        "Col": []
    },
    "ColorlessAccents2": {
        "Sub": [
            "NONE",
            "Accents_UnderEyeBags",
            "Accents_SubtleEyeBags",
            "Accents_UnderEyeBags_Small",
            "Accents_UnderEyeCrease",
            "Accents_NasoLabialFolds",
            "Accents_ChinCleft",
            "Accents_CrowsFeet",
            "Accents_CrackedLips",
            "Accents_Lips",
            "Accents_RoughFace",
            "Accents_Moles_FaceNeck",
            "Accents_Moles_BaldHeadNeck",
            "Accents_Fullface_Wrinkles",
            "Accents_FullfaceMom_Wrinkles",
            "Blemish_VeinsMany"
        ],
        "Col": []
    },
    "Complexion1": {
        "Sub": [
            "NONE",
            "Color_Temperature_Purple",
            "Color_Temperature_Green",
            "Color_Temperature_Warm",
            "Color_Temperature_Yellow",
            "Color_Temperature_Cool",
            "Color_Temperature_Pink",
            "Crevice_Complexion_Warm",
            "Crevice_Complexion_Cool",
            "Crevice_Complexion_Jaundiced",
            "Vitiligo_1",
            "Vitiligo_2",
            "Vitiligo_3",
            "TriColor"
        ],
        "Col": []
    },
    "Complexion2": {
        "Sub": [
            "NONE",
            "Color_Temperature_Purple",
            "Color_Temperature_Green",
            "Color_Temperature_Warm",
            "Color_Temperature_Yellow",
            "Color_Temperature_Cool",
            "Color_Temperature_Pink",
            "Crevice_Complexion_Warm",
            "Crevice_Complexion_Cool",
            "Crevice_Complexion_Jaundiced",
            "Vitiligo_1",
            "Vitiligo_2",
            "Vitiligo_3",
            "TriColor"
        ],
        "Col": []
    },
    "ComplexionMask1": {
        "Sub": [
            "NONE",
            "Freckles_Nose",
            "Freckles_Forehead",
            "Freckles_Cheek",
            "Freckles_MidFace",
            "Freckles_Chin",
            "Freckles_Face",
            "Freckles_FullFace",
            "moles_Many_Small",
            "moles_Many_Small_02",
            "moles_Many_Small_03",
            "moles_Many_Small_04",
            "Moles_Bridge",
            "Moles_Cheek_L",
            "Moles_MidFace",
            "Moles_Cheek_R",
            "Moles_FaceSides",
            "Moles_Forehead",
            "Moles_Forehead_2",
            "Moles_Nose",
            "Moles_Chin",
            "Moles_UnderEye",
            "Liver_Spots",
            "Rosacea_Nose",
            "Rosacea_Cheeks",
            "Rosacea_FullFace",
            "Blemishes_Forehead",
            "Blemishes_MidFace",
            "Blemishes_LowerFace",
            "Blemishes_FullFace",
            "Blemishes_FullFace2",
            "Blemishes_FullFace3",
            "Veins",
            "Veins_2",
            "EyeSockets_Dark",
            "Complexion_Patchy",
            "Complexion_Patchy_2",
            "Complexion_WholeFace_Soft",
            "Complexion_WholeFace_Crevices_Soft",
            "Complexion_LowerFace_Crevices",
            "Complexion_Eye_Crevices",
            "Complexion_Crevices",
            "UnderEyeBags",
            "Cheeks_Sallow",
            "Stubble_Light",
            "Stubble_Heavy",
            "Stubble_Patchy"
        ],
        "Col": []
    },
    "ComplexionMask2": {
        "Sub": [
            "NONE",
            "Freckles_Nose",
            "Freckles_Forehead",
            "Freckles_Cheek",
            "Freckles_MidFace",
            "Freckles_Chin",
            "Freckles_Face",
            "Freckles_FullFace",
            "moles_Many_Small",
            "moles_Many_Small_02",
            "moles_Many_Small_03",
            "moles_Many_Small_04",
            "Moles_Bridge",
            "Moles_Cheek_L",
            "Moles_MidFace",
            "Moles_Cheek_R",
            "Moles_FaceSides",
            "Moles_Forehead",
            "Moles_Forehead_2",
            "Moles_Nose",
            "Moles_Chin",
            "Moles_UnderEye",
            "Liver_Spots",
            "Rosacea_Nose",
            "Rosacea_Cheeks",
            "Rosacea_FullFace",
            "Blemishes_Forehead",
            "Blemishes_MidFace",
            "Blemishes_LowerFace",
            "Blemishes_FullFace",
            "Blemishes_FullFace2",
            "Blemishes_FullFace3",
            "Veins",
            "Veins_2",
            "EyeSockets_Dark",
            "Complexion_Patchy",
            "Complexion_Patchy_2",
            "Complexion_WholeFace_Soft",
            "Complexion_WholeFace_Crevices_Soft",
            "Complexion_LowerFace_Crevices",
            "Complexion_Eye_Crevices",
            "Complexion_Crevices",
            "UnderEyeBags",
            "Cheeks_Sallow",
            "Stubble_Light",
            "Stubble_Heavy",
            "Stubble_Patchy"
        ],
        "Col": []
    },
    "Scars": {
        "Sub": [
            "NONE",
            "Scar_01",
            "Scar_AcrossNose",
            "Scar_EyeLeftHeavy",
            "Scar_EyeLeftLong",
            "Scar_EyeRightRagged",
            "Scar_ForeheadClaw",
            "Scar_LeftBrowSmall",
            "Scar_LipLeftHeavy",
            "Scar_Mouth_Scarification",
            "Scar_MouthSlit",
            "Scar_NoseGouges",
            "Scar_RaggedY",
            "Scar_RightBrowGouge",
            "Scar_RightBrowSmall",
            "Burn_LeftCheekManySmall",
            "Burn_RightCheekLarge",
            "Burn_ForeheadLeftEye",
            "Burn_Mouth",
            "Burn_RightFace",
            "Burn_FaceCenter",
            "Burn_AlloverLight",
            "Burn_EyeLeft",
            "Blemish_VeinsMany",
            "Burn_EzekielRightCheek"
        ],
        "Col": []
    },
    "Dermaesthetic": {
        "Sub": [
            "NONE",
            "Asian_Male_Ol1_Sk1",
            "Asian_Male_Ol1_Sk3",
            "Asian_Male_Ol1_Sk6",
            "Asian_Male_Ol1_Sk8",
            "Asian_Male_yo1_Sk1",
            "Asian_Male_yo1_Sk3",
            "Asian_Male_yo1_Sk6",
            "Asian_Male_yo1_Sk8",
            "European_Male_Md1_Sk1",
            "European_Male_md1_sk3",
            "European_Male_Md1_Sk6",
            "European_Male_Md1_Sk8",
            "European_Male_Md2_Sk1",
            "European_Male_Md2_Sk3",
            "European_Male_Md2_Sk6",
            "European_Male_Md2_Sk8",
            "European_Male_Ol1_Sk1",
            "European_Male_Ol1_Sk3",
            "European_Male_Ol1_Sk6",
            "European_Male_Ol1_Sk8",
            "European_Male_yo1_Sk1",
            "European_Male_yo1_Sk3",
            "European_Male_yo1_Sk6",
            "European_Male_yo1_Sk8",
            "African_Female_md1_Sk1",
            "African_Female_md1_Sk3",
            "African_Female_md1_Sk6",
            "African_Female_md1_sk8",
            "African_Female_ol1_Sk1",
            "African_Female_ol1_Sk3",
            "African_Female_ol1_Sk6",
            "African_Female_ol1_sk8",
            "African_Female_yo1_Sk1",
            "African_Female_yo1_Sk3",
            "African_Female_yo1_Sk6",
            "African_Female_yo1_sk8",
            "Asian_Female_md1_Sk1",
            "Asian_Female_md1_Sk3",
            "Asian_Female_MD1_SK6",
            "Asian_Female_md1_Sk8",
            "Asian_Female_ol1_Sk1",
            "Asian_Female_ol1_Sk3",
            "Asian_Female_ol1_Sk6",
            "Asian_Female_ol1_Sk8",
            "Asian_Female_yo1_Sk1",
            "Asian_Female_yo1_Sk3",
            "Asian_Female_yo1_Sk6",
            "Asian_Female_Yo1_Sk8",
            "European_Female_md1_Sk1",
            "European_Female_Md1_Sk3",
            "European_Female_md1_Sk6",
            "European_Female_md1_Sk8",
            "European_Female_md2_Sk1",
            "European_Female_md2_Sk3",
            "European_Female_md2_Sk6",
            "European_Female_md2_Sk8",
            "European_Female_ol1_Sk1",
            "European_Female_Ol1_Sk3",
            "European_Female_ol1_Sk6",
            "European_Female_ol1_Sk6",
            "European_Female_ol1_Sk8",
            "European_Female_yo1_Sk1",
            "European_Female_Yo1_Sk3",
            "European_Female_yo1_Sk6",
            "European_Female_yo1_Sk8",
            "African_Male_md1_Sk1",
            "African_Male_md1_Sk3",
            "African_Male_md1_Sk6",
            "African_Male_Md1_Sk8",
            "African_Male_ol1_Sk1",
            "African_Male_ol1_Sk3",
            "African_Male_ol1_Sk6",
            "African_Male_Ol1_Sk8",
            "African_Male_yo1_Sk1",
            "African_Male_yo1_Sk3",
            "African_Male_yo1_Sk6",
            "African_Male_Yo1_Sk8",
            "Asian_Male_md1_Sk1",
            "Asian_Male_md1_Sk3",
            "Asian_Male_md1_Sk6",
            "Asian_Male_md1_Sk8",
            "male_as_md2_sk1_Derm_color",
            "male_as_md2_sk3_Derm_color",
            "male_as_md2_sk6_Derm_color",
            "male_as_md2_sk8_Derm_color"
        ],
        "Col": []
    },
    "TattooMask": {
        "Sub": [
            "NONE",
            "Dagger",
            "Leaf",
            "Cat",
            "Circuits01",
            "Circuits02",
            "Dragon",
            "Eagle",
            "Geoflower01",
            "Geoflower02",
            "Geometric",
            "MummersMask",
            "skull",
            "Spacecat"
        ],
        "Col": tattoo_colors
    },
    "MakeupFullPaintMask1": {
        "Sub": [
            "NONE",
            "X_Eyes",
            "Mask_Antlered",
            "ChinLine",
            "CyberLines",
            "DarkTears",
            "Eyelines",
            "Masked",
            "Masked_2",
            "Moustache",
            "EyeBlack",
            "Eyesocket",
            "FullSkull",
            "WideTeeth",
            "Nose",
            "Maske_Airbrushed",
            "SpraySmile",
            "SkullEyes",
            "right_spray",
            "Left_Spray",
            "LowerFaceSpray",
            "Teeth"
        ],
        "Col": face_paint_colors
    },
    "MakeupFullPaintMask2": {
        "Sub": [
            "NONE",
            "X_Eyes",
            "Mask_Antlered",
            "ChinLine",
            "CyberLines",
            "DarkTears",
            "Eyelines",
            "Masked",
            "Masked_2",
            "Moustache",
            "EyeBlack",
            "Eyesocket",
            "FullSkull",
            "WideTeeth",
            "Nose",
            "Maske_Airbrushed",
            "SpraySmile",
            "SkullEyes",
            "right_spray",
            "Left_Spray",
            "LowerFaceSpray",
            "Teeth"
        ],
        "Col": face_paint_colors
    },
    "Lipstick1": {
        "Sub": [
            "NONE",
            "Lipstick_Standard",
            "Lipstick_Soft",
            "LipStain_Bottom",
            "LipStain_Top",
            "LipLiner_Thick"
        ],
        "Col": makeup_colors
    },
    "Lipstick2": {
        "Sub": [
            "NONE",
            "Lip_Liner",
            "Lip_Stain_Corners",
            "Lip_Stain_Center",
            "LipStain_Top",
            "LipStain_Bottom",
            "LipLiner_Thick"
        ],
        "Col": makeup_colors
    },
    "Eyeshadow1": {
        "Sub": [
            "NONE",
            "EyeShadow_Upper_01",
            "EyeShadow_Upper_02",
            "EyeShadow_Upper_03",
            "StrongEyeshadow_Upper",
            "TwotoneUpper_Inner",
            "Conservative_Eyeshadow_Upper_mask"
        ],
        "Col": makeup_colors
    },
    "Eyeshadow2": {
        "Sub": [
            "NONE",
            "EyeShadow_Lower_01",
            "EyeShadow_Lower_02",
            "EyeShadow_Lower_03",
            "StrongEyeshadow_Lower",
            "TwoToneUpper_Outer",
            "ConservativeEyeShadow_Lower_mask"
        ],
        "Col": makeup_colors
    },
    "Eyeliner1": {
        "Sub": [
            "NONE",
            "Eyeliner_Upper_01",
            "Eyeliner_Upper_02",
            "Eyeliner_Upper03",
            "Eyeliner_Lower_01",
            "Eyeliner_Lower_02",
            "Eyeliner_Lower_03",
            "EyeLinerNeon_Upper",
            "EyeLinerConservative_Upper",
            "EyeLinerLightning_Upper"
        ],
        "Col": makeup_colors
    },
    "Eyeliner2": {
        "Sub": [
            "NONE",
            "Eyeliner_Lower_01",
            "Eyeliner_Lower_02",
            "Eyeliner_Lower_03",
            "Eyeliner_Upper_01",
            "Eyeliner_Upper_02",
            "Eyeliner_Upper03",
            "EyeLinerConservative_Lower",
            "EyeLinerLightning_Lower",
            "EyeLinerNeon_Lower",
        ],
        "Col": makeup_colors
    }
}

ethnicities = ["af", "as", "eu"]
ages = ["yo1", "md1", "ol1"]
features = ["Cheeks", "Chin", "Ears", "Eyes", "Forehead", "Jaw", "Mouth", "Neck", "Nose"]

skin_color_options = {
    "eu": [0, 1, 2],
    "as": [3, 4, 5],
    "af": [6, 7, 8]
}

region_data_male = {
    "af_ol1": 40,
    "af_md1": 9,
    "af_yo1": 42,
    "eu_ol1": 14,
    "eu_md2": 12,
    "eu_yo1": 16,
    "as_ol1": 44,
    "as_md1": 1,
    "as_yo1": 46
}

region_data_female = {
    "af_ol1": 15,
    "af_md1": 9,
    "af_yo1": 13,
    "eu_ol1": 3,
    "eu_md2": 1,
    "eu_yo1": 17,
    "as_ol1": 11,
    "as_md1": 5,
    "as_yo1": 19,
}

sculpt_list_male = [72, 82, 26, 66, 30, 62, 50, 38, 22, 56, 34]

sculpt_data_male = {
    72: [73, 74, 75], # Cheeks
    82: [83, 84, 85], # Chin
    26: [27, 28, 29], # Ears
    66: [67, 68, 69], # Eyebrows
    30: [31, 32, 60, 65], # Eyes
    62: [63, 64], # Forehead
    50: [51, 52, 53, 54], # Head Shapes
    38: [39, 78, 79], # Jaw
    22: [24, 25, 76, 77], # Mouth
    56: [58, 80], # Neck
    34: [35, 36, 37, 70, 71, 86, 87, 88, 89] # Nose
}

sculpt_list_female = [46, 33, 56, 60, 64, 71, 23, 37, 41, 29, 50]

sculpt_data_female = {
    46: [47, 48, 49], # Cheeks
    33: [34, 35, 36], # Chin
    56: [57, 58, 59], # Ears
    60: [61, 62, 63], # Eyebrows
    64: [65, 67, 69, 70], # Eyes
    71: [72, 73], # Forehead
    23: [24, 25, 26, 27], # Head Shapes
    37: [38, 39, 40], # Jaw
    41: [42, 43, 44, 45], # Mouth
    29: [30, 31], # Neck
    50: [51, 52, 53, 54, 55, 75, 77, 78, 79] # Nose
}

andro = False

def generate_constrained_float(min_val, max_val, mu, sigma):
    """Generates a random float using a Gaussian distribution, clamped to min/max."""
    return max(min_val, min(random.gauss(mu, sigma), max_val))

def build_morph_sliders(sex, primary, secondary):
    """Programmatically constructs valid Starfield morph string identifiers."""
    
    morphs = []
    # Select a primary and secondary ethnicity to blend
    
    
    # Generate 5-9 active morph sliders to prevent face breaking
    #active_features = random.sample(features, k=random.randint(5, 9))
    
    for feature in features:
        rand = random.random()

        primary_morph = f"{sex.lower()}_{primary}_{feature}"
        secondary_morph = f"{sex.lower()}_{secondary}_{feature}"
        val = generate_constrained_float(0.0, 1.0, 1.0, 0.25)

        morphs.append({
            "Name": primary_morph if rand > 0.3 else secondary_morph,
            "Value": val
        })

        morphs.append({
            "Name": secondary_morph if rand > 0.3 else primary_morph,
            "Value": 1.0 - val
        })
    return morphs

def build_morph_regions(sex, primary, secondary): # Region Morphs
    # Ethnicity Morphs
    region_data = -1
    sculpt_data = -1
    sculpt_list = -1
    regions = []

    #print(sex, primary, secondary)

    if (sex == "Male"):
        region_data = region_data_male
        sculpt_data = sculpt_data_male
        sculpt_list = sculpt_list_male
    elif (sex == "Female"):
        region_data = region_data_female
        sculpt_data = sculpt_data_female
        sculpt_list = sculpt_list_female

    iPrimary = region_data[primary]
    iSecondary = region_data[secondary]

    sliderPrimary = []
    sliderSecondary = []

    for feature in features:
        rand = random.random()

        val = generate_constrained_float(0.0, 1.0, 0.75, 0.25)

        sliderPrimary.append({
            "GroupName": feature,
            "ID": 0,
            "Value": val
        })

        sliderSecondary.append({
            "GroupName": feature,
            "ID": 0,
            "Value": 1.0 - val
        })

    regions.append({
        "RegionID": iPrimary,
        "SlidersA": sliderPrimary
    })

    regions.append({
        "RegionID": iSecondary,
        "SlidersA": sliderSecondary
    })

    # Sculpt Morphs

    for sculpt in sculpt_list:
        sliders = []

        for group in sculpt_data[sculpt]:
            val = 0
            if (sex == "Male" and sculpt == 50) or (sex == "Female" and sculpt == 23):
                val = generate_constrained_float(0.0, 1.0, 0.25, 0.1)
            else:
                val = generate_constrained_float(-1.0, 1.0, 0.0, 0.5)

            sliders.append({
                "GroupName": "",
                "ID": group,
                "Value": val
            });
        
        regions.append({
            "RegionID": sculpt,
            "SlidersA": sliders
        })

    return regions

def generate_npc_structure(sex):
    sex_prefix = f"Human_{sex}"
    primary_eth, secondary_eth = random.sample(ethnicities, 2)
    age = random.choice(ages)
    primary = f"{primary_eth}_{age}"
    secondary = f"{secondary_eth}_{age}"

    if ("eu_md1" in primary):
        primary = primary.replace("eu_md1", "eu_md2")

    if ("eu_md1" in secondary):
        secondary = secondary.replace("eu_md1", "eu_md2")
    
    # Build Layers

    skin_options = ["Dermaesthetic","ComplexionMask1","Complexion1","Complexion2","ComplexionMask2","Scars","Accents1","Accents2","ColorlessAccents1","ColorlessAccents2"]
    paint_options = ["TattooMask","MakeupFullPaintMask1","MakeupFullPaintMask2"]
    makeup_options = ["Cheeks1","Cheeks2","Lipstick1","Lipstick2","Eyeshadow1","Eyeshadow2","Eyeliner1","Eyeliner2"]
    
    customization_layers = []

    # Skin Options - All
    for _ in range(random.randint(2, 8)):
        iOption = random.randint(0, len(skin_options) - 1)
        sOption = skin_options[iOption]

        customization_layers.append({
            "Intensity": generate_constrained_float(0.0, 0.8, 0.4, 0.2),
            "ModulationValue": { # Colours
                "Value": random.choice(layer_options[sOption]["Col"]) if len(layer_options[sOption]["Col"]) > 0 else ""
            },
            "Name": sOption,
            "Value": { # Subtypes
                "Value": random.choice(layer_options[sOption]["Sub"])
            } # Placeholder for actual texture map references
        })

        skin_options.pop(iOption)

    # Paint Options - Low chance
    if (random.random() > 0.95):
        for _ in range(random.randint(1, 2)):
            iOption = random.randint(0, len(paint_options) - 1)
            sOption = paint_options[iOption]

            customization_layers.append({
                "Intensity": generate_constrained_float(0.0, 0.8, 0.4, 0.2),
                "ModulationValue": { # Colours
                    "Value": random.choice(layer_options[sOption]["Col"]) if len(layer_options[sOption]["Col"]) > 0 else ""
                },
                "Name": sOption,
                "Value": { # Subtypes
                    "Value": random.choice(layer_options[sOption]["Sub"])
                } # Placeholder for actual texture map references
            })

            paint_options.pop(iOption)

    # Makeup - female and medium chance or male and low chance
    if ((sex == "Female" and random.random() > 0.75) or (sex == "Male" and random.random() > 0.9)):
        for _ in range(random.randint(1, 2)):
            iOption = random.randint(0, len(makeup_options) - 1)
            sOption = makeup_options[iOption]

            customization_layers.append({
                "Intensity": generate_constrained_float(0.0, 0.8, 0.4, 0.2),
                "ModulationValue": { # Colours
                    "Value": random.choice(layer_options[sOption]["Col"]) if len(layer_options[sOption]["Col"]) > 0 else ""
                },
                "Name": sOption,
                "Value": { # Subtypes
                    "Value": random.choice(layer_options[sOption]["Sub"])
                } # Placeholder for actual texture map references
            })

            makeup_options.pop(iOption)

    # Head Parts
    hair_part = f"{sex_prefix}_Hair_{random.choice(hair_all)}" if andro == True else f"{sex_prefix}_Hair_{random.choice(hair_male)}" if sex == "Male" else f"{sex_prefix}_Hair_{random.choice(hair_female)}" if sex == "Female" else random.choice(hair_all)
    eyebrow_part = f"{sex_prefix}_Eyebrow_{random.choice(eyebrow_options)}"
    beard_part = f"{sex_prefix}_Beard_{random.choice(beard_options)}" if (sex == "Male" and random.random() > 0.75) else "none"
    jewelry_part = f"{sex_prefix}_Jewelry_{random.choice(jewelry_options)}_{sex[0]}" if (sex == "Female" and random.random() > 0.75) else "none"
    right_eye_part = f"{sex_prefix}_RightEye" if random.random() > 0.2 else (random.choice([f"{sex_prefix}_RightEye_Jaundice", f"{sex_prefix}_RightEye_Bloodshot"]))
    left_eye_part = f"{sex_prefix}_LeftEye" if random.random() > 0.2 else (random.choice([f"{sex_prefix}_LeftEye_Jaundice", f"{sex_prefix}_LeftEye_Bloodshot"]))

    head_parts = [
        "",
        f"{sex_prefix}_Head",
        right_eye_part,
        hair_part,
        beard_part,
        "",
        eyebrow_part,
        jewelry_part,
        "",
        f"{sex_prefix}_Teeth",
        "",
        "",
        left_eye_part,
        f"{sex_prefix}_Eyelashes_01_Top" if random.random() > 0.5 else f"{sex_prefix}_Eyelashes_02_Top"
    ]
    
    # hair_color = ""
    # if (andro == True):
    #     hair_color = random.choice(hair_colors_all)
    # elif (primary_eth == "eu"):
    #     hair_color = random.choice(hair_colors_natural)
    # else:
    #     hair_color = random.choice(hair_colors_non_eu)

    hair_color = random.choice(hair_colors_all) if andro == True else random.choice(hair_colors_natural) if primary_eth == "eu" else random.choice(hair_colors_non_eu)

    npc_data = {
        "RaceFormID": "HumanRace",
        #"BodyMorphRegionValuesA": [0.0, generate_constrained_float(0.0, 0.8, 0.2, 0.1), 0.0, 0.0, 0.0],
        "SkinTone": random.choice(skin_color_options[primary_eth]),
        "Sex": sex,
        "HairColor": hair_color,
        "EyeColor": random.choice(eye_colors_all),
        "BrowHairColor": hair_color,
        "FacialHairColor": hair_color if sex == "Male" else "",
        "JewelryColor": random.choice(jewelry_colors),
        "TeethCustomization": "Teeth_Clean" if random.random() > 0.1 else random.choice(["Teeth_Dirty", "Teeth_Dead","Teeth_Blackened"]),
        "FacialBoneRegionDataA": build_morph_regions(sex, primary, secondary),
        "FacialMorphSliderDataA": build_morph_sliders(sex, primary, secondary),
        "MorphWeights": {
            "x": generate_constrained_float(0.0, 1.0, 0.5, 0.25),
            "y": generate_constrained_float(0.0, 1.0, 0.5, 0.25),
            "z": generate_constrained_float(0.1, 0.9, 0.0, 0.2)
        },
        "PostBlendFaceCustomization": {"LayersA": customization_layers},
        "UniqueHeadPartsA": head_parts,
        "MiscHeadPartsA": [],
    }

    return npc_data

if __name__ == "__main__":
    if (len(sys.argv) > 0):
        if (sys.argv[0].lower() == "1"):
            andro = True
            print("Androgynous Mode")
        else:
            print("Non-androgynous Mode")
    else:
        print("Non-androgynous Mode")

    for i in range(5):
        generated_npc = generate_npc_structure("Male")
        with open(f"ReGeneration_M_{i + 1}.npc", 'w') as f:
            json.dump(generated_npc, f, indent=3)
        print(f"NPC ReGeneration Male {i + 1} created.")

    for i in range(5):
        generated_npc = generate_npc_structure("Female")
        with open(f"ReGeneration_F_{i + 1}.npc", 'w') as f:
            json.dump(generated_npc, f, indent=3)
        print(f"NPC ReGeneration Female {i + 1} created.")
        