from config import Users

Selector = """[Rainmeter]
Update=-1
OnRefreshAction=[!Move (#SCREENAREAWIDTH#/2)-{0} (#SCREENAREAHEIGHT#/2)-145]

[userStyle]
FontSize=16
FontFace=Arial
StringEffect=Border
FontEffectColor=180,180,180,120
AntiAlias=1
y=126r"""

User = """[meter{0}]
Meter=Image
ImageName={1}
X={2}
W=150
H=150
PreserveAspectRatio=1
LeftMouseUpAction=[!DeactivateConfig "LoginScreen\LoginScreenUserSelector"][!ActivateConfig "LoginScreen\LoginScreenUserPicture" "{0}.ini"]

[meter{0}String]
Meter=String
X=0r
MeterStyle=userStyle
Text={0}"""

def genIni():
	
	with open("LoginScreenUserSelector\selector.ini", "w") as f:
		x=((len(Users.users)-1)*160+150)/2
		f.write(Selector.format(x))
		f.write('\n\n')
		
		for i, user in enumerate(Users.users):
			f.write(User.format(user, Users.users[user]['image'], i*160))
			f.write('\n\n')
	
if __name__ == '__main__':
	genIni()
	