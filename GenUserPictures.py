from config import Users

UserPicture = """[Rainmeter]
Update=-1
OnRefreshAction=[!Move (#SCREENAREAWIDTH#/2)-55 (#SCREENAREAHEIGHT#/2)-120]

[meterUserPicBackground]
Meter=Shape
Shape=Rectangle 0,0,110,110,7,7 | FillColor 255,255,255,140 | StrokeWidth 0

[meterPassBackground]
Meter=Shape
Group=PasswordField
Shape=Rectangle 0,115,110,25,3,3 | FillColor 100,100,100,140 | StrokeWidth 0


;This is where the actual password checks happen. If the user enters password, we activate the LoginScreen Unloader, and activate my personal theme's Loader.
[measurePassword]
Measure=String
DynamicVariables=1
String=-
IfMatch={0}
IfMatchAction=[!ActivateConfig "LoginScreen\LoginScreenUnloader"][!ActivateConfig "{1}"][!DeactivateConfig]

[MeasureInputPassword]
Measure=Plugin
Plugin=InputText
SolidColor=100,100,100,140
FontColor=255,255,255,255
StringStyle=Italic
FontSize=10
Password=1
X=0
Y=115
H=25
W=110
Command1=[!SetOption measurePassword String "$UserInput$"][!ShowMeterGroup PasswordField][!Update]
OnDismissAction=[!ShowMeterGroup PasswordField][!Update]

[meterUserPic]
Meter=Image
ImageName={2}
X=5
Y=5
W=100
H=100
PreserveAspectRatio=1

[meterEnterPassword]
Meter=String
Group=PasswordField
X=1
Y=120
FontSize=10
FontColor=255,255,255,255
AntiAlias=1
Text=Enter Password..
LeftMouseUpAction=[!CommandMeasure "MeasureInputPassword" "ExecuteBatch 1-2"][!HideMeterGroup PasswordField][!Update]"""

def genIni():
	for user in Users.users:
		with open ('LoginScreenUserPicture\{0}.ini'.format(user), 'w') as f:
			data = Users.users[user]
			f.write(UserPicture.format(data['password'], data['loader'], data['image']))
	
	
if __name__ == '__main__':
	genIni()