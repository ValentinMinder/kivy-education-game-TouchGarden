# registering fonts, as suggested by
# http://cheparev.com/kivy-connecting-font/
# https://github.com/eviltnan/kivy-font-example

KIVY_FONTS = [
    {
        "name": "Roboto",
        "fn_regular": "fonts/Roboto/Roboto-Regular.ttf",
        "fn_bold": "fonts/Roboto/Roboto-Bold.ttf",
        "fn_italic": "fonts/Roboto/Roboto-Italic.ttf",
        "fn_bolditalic": "fonts/Roboto/Roboto-BoldItalic.ttf",
    },
    {
        "name": "RobotoCondensed",
        "fn_regular": "fonts/Roboto/Roboto-Light.ttf",
        "fn_bold": "fonts/Roboto/Roboto-Medium.ttf",
        "fn_italic": "fonts/Roboto/Roboto-LightItalic.ttf",
        "fn_bolditalic": "fonts/Roboto/Roboto-MediumItalic.ttf",
    },
    {
        "name": "CorporativeSansRd",
        "fn_regular": "fonts/CorporativeSansRd/CorporativeSansRd-Light.otf",
        "fn_bold": "fonts/CorporativeSansRd/CorporativeSansRdAlt-Bold.otf",
        "fn_italic": "fonts/CorporativeSansRd/CorporativeSansRd-LightIt.otf",
        "fn_bolditalic": "fonts/CorporativeSansRd/CorporativeSansRdAlt-BoldIt.otf",
    },
    {
        "name": "CorporativeSans",
        "fn_regular": "fonts/CorporativeSans/CorporativeSans-Regular.otf",
        "fn_bold": "fonts/CorporativeSans/CorporativeSans-Bold.otf",
        "fn_italic": "fonts/CorporativeSans/CorporativeSans-Italic.otf",
        "fn_bolditalic": "fonts/CorporativeSans/CorporativeSans-BoldItalic.otf",
    },
]

# this is used everywhere as default (and Label class uses this default)
KIVY_DEFAULT_FONT = "CorporativeSans"

