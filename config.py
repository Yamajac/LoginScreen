
class Loaders:

    # A dict of the loader skins, and the skins they need to load. Along with the coordinates the skins need to be set to. 
    # If a skin sets it's own coordinates, you can set the skins coordinate to False and it won't be moved.
    # The skins in your theme do not need to all be from the same parent skin. You can mix illustro, homebrew, etc. Just make sure you put the correct config names in.
    # You can also have the script generate arbitrary bangs into the loader skin if you need more complicated stuff to happen.
    # "Loader Name" : {
    #    "ConfigToBeLoaded" : [x,y,variant],
    #    "ConfigToBeLoaded" : False,
    #    "bangs"            : [list of arbitrary bangs to be run, not including the brackets]
    # }
    # If you need your bangs to be run before the skins are loaded, put the bangs at the start of the list.
    # If you need them to be run after the skins are loaded, put the bangs at the end of the list.
    # You can run GenLoaders.py to generate all of the loader skins.
    # They will be generated in the Loaders folder, and the skins will be called LoaderNameLoader \ LoaderNameUnloader \ LoaderNameRefresher
    # The initial setup of these can be a bit tedious, but once it's setup, modifying it is very simple.
    skins = {
        "LoginScreen" : {
            "LoginScreen\LoginScreenBackground"  :[0,     0],
            "LoginScreen\LoginScreenUserSelector" :False
        },
        
        "FLEXTRAA" : {
            "TRAA\Launcher"             : [1368,540],
            "TRAA\Wallpaper"            : [0,     0],
            "TRAA\Calendar"             : [0,   272],
            "Yamachat\YamaChat"         : [0,     0],
            "TiredClock"                : [1560,  0],
            "Tester\Sliders"            : [0,   680],
            "Tester\\UnitConversion"    : [1168, 10],
            "RainGame\Main"             : [55,  345],
            "RainGame\ScreenEditor"     : [744, 265],
            "bangs"                     : [
                '!WriteKeyValue Variables Name FLEXTRAA "#@#Variables.inc"',
                '!WriteKeyValue Variables Unloader "LoginScreen\FLEXTRAAUnloader" "#@#Variables.inc"',
            ]
        },
        
        "DEVKIT" : {
            "DevKit\Wallpaper"          : [0,     0],
            "DevKit\Clock"              : [909, 836],
            "DevKit\RainManager"        : [0,     0],
            "bangs"                     : [
                '!WriteKeyValue Variables Name DEVKIT "#@#Variables.inc"',
                '!WriteKeyValue Variables Unloader "LoginScreen\DEVKITUnloader" "#@#Variables.inc"',
            ]
            
        },
        
        "MINIMAL" : {
            "MinimalSuite\Wallpaper"    : [0,     0]
        }
        
        
    }


class Users:
    
    # A dict of all the users you want to generate.
    # If you set password to False, then clicking the user's profile at the selection screen will sign you into that profile.
    # Otherwise, you'll be sent to a separate screen where you need to input the correct password.
    # USER: {
    #    "loader"   : "your custom loader config",
    #    "password" : "User's Password",
    #    "image"    : "Path to user profile picture. Relative to the loginscreen skin"
    # }
    # You can use GenUserPictures.py to generate all of the user skins in the LoginScreenUserPicture folder, with the file names being the user name.
    # GenUserSelector.py will re-create a LoginScreenUserSelector skin using this information, so make sure all of the profiles you want access to are in this dict.
    users = {
        "FLEXTRAA": {
            "loader"   : "LoginScreen\FLEXTRAALoader",
            "password" : False,
            "image"    : "#@#Images\TraaPic.png"
        },
        
        "Skin Devver": {
            "loader"   : "LoginScreen\DEVKITLoader",
            "password" : False,
            "image"    : "#@#Images\OpenSourcerer.png"
        },
        
        "Minimalist": {
            "loader"   : "LoginScreen\MINIMALLoader",
            "password" : "minimalism",
            "image"    : "#@#Images\Minimalist.png"
        }
        
    }