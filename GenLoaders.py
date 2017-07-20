import config
import os


		
def genIni(prefix, file, move=False):
	with open('{0}/loader.ini'.format(file), "w") as f:
		f.write('[Rainmeter]\n')
		f.write('Update=-1\n')
		
		actions = "OnUpdateAction="
		for skin in config.skins:
			action = '{0}"{1}"]'.format(prefix,skin)
			actions+=action
			
			if move and config.skins[skin]:
				x=config.skins[skin][0]
				y=config.skins[skin][1]
				action = '[!Move "{0}" "{1}" "{2}"]'.format(x,y,skin)
				actions+=action
		actions+='[!DeactivateConfig "{0}\{1}"]\n\n'.format(config.name,file)
		f.write(actions)
		
		f.write("[meterLoading]\n")
		f.write("Meter=String")
			
if __name__ == '__main__':
	type="Loader"

	os.makedirs("{0}{1}".format(config.name,type), exist_ok=True)
	genIni('[!ActivateConfig ', '{0}{1}'.format(config.name,type), True)
	
	type="Unloader"
	os.makedirs("{0}{1}".format(config.name,type), exist_ok=True)
	genIni('[!DeactivateConfig ', '{0}{1}'.format(config.name,type))
	
	type="Refresher"
	os.makedirs("{0}{1}".format(config.name,type), exist_ok=True)
	genIni('[!Refresh ', '{0}{1}'.format(config.name,type), True)
	