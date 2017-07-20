

# A dict of the skins needed to be loaded/unloaded, as well as their positions.
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