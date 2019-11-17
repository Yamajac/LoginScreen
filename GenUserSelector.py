from config import Users
import traceback

Selector = """[Rainmeter]
Update=-1
OnRefreshAction=[!Move (#SCREENAREAWIDTH#/2)-{0} (#SCREENAREAHEIGHT#/2)-145]

[userStyle]
FontSize=16
FontFace=Arial
Group = tester
StringEffect=Border
FontEffectColor=180,180,180,120
AntiAlias=1
DynamicVariables=1
X=(75 - ([#CurrentSection#:W]/2))r
y=150r"""

User = """[{0}]
Meter=Image
ImageName={1}
X={2}
W=150
H=150
PreserveAspectRatio=1
LeftMouseUpAction=[!DeactivateConfig]{3}

[{0}String]
Meter=String
MeterStyle=userStyle
Text={0}"""

def genIni():
	
	with open("LoginScreenUserSelector\selector.ini", "w") as f:
		x=((len(Users.users)-1)*160+150)/2
		f.write(Selector.format(x))
		f.write('\n\n')
		
		for i, user in enumerate(Users.users):
			loader = '[!ActivateConfig "LoginScreen\LoginScreenUserPicture" "{0}.ini"]'.format(user) if Users.users[user]['password'] else '[!ActivateConfig "LoginScreen\LoginScreenUnloader"][!ActivateConfig "{0}"]'.format(Users.users[user]['loader'])
			f.write(User.format(user, Users.users[user]['image'], i*160, loader))
			f.write('\n\n')
	
if __name__ == '__main__':
	try:
		genIni()
	except:
		input(traceback.print_exc())
	