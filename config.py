

# A dict of the skins needed to be loaded/unloaded, as well as their positions.
# The skins in your theme do not need to all be from the same parent skin. You can mix illustro, homebrew, etc. Just make sure you put the correct config names in.
# ConfigName : [x,y]
# If the skin sets its own position then
# ConfigName : False

skins = {
	"LoginScreen\LoginScreenBackground"  :[0,     0],
	"LoginScreen\LoginScreenUserPicture" :False
}

# The loader skins will be called nameLoader\nameUnloader
# EG: LoginScreenLoader \ LoginScreenUnloader
name = "LoginScreen"