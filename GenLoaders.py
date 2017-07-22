from config import Loaders
import os, traceback


		
def genIni(prefix, file, type, move=False):
	with open('Loaders/{0}{1}/loader.ini'.format(file, type), "w") as f:
		f.write('[Rainmeter]\n')
		f.write('Update=-1\n')
		
		print(file)
		actions = "OnUpdateAction="
		for skin in Loaders.skins[file]:
			if skin=='bangs':
				if move:
					print('   {0}'.format(Loaders.skins[file][skin]))
					actions+=''.join('[{0}]'.format(d) for d in Loaders.skins[file][skin])
				continue
			action = '{0}"{1}"]'.format(prefix,skin)
			actions+=action
			
			print('   {0}'.format(skin))
			if move and Loaders.skins[file][skin]:
				x=Loaders.skins[file][skin][0]
				y=Loaders.skins[file][skin][1]
				action = '[!Move "{0}" "{1}" "{2}"]'.format(x,y,skin)
				actions+=action
		actions+='[!DeactivateConfig]\n\n'
		f.write(actions)
		
		f.write("[meterLoading]\n")
		f.write("Meter=String")
		
def main():
	for loader in Loaders.skins:
	
		type="Loader"
		os.makedirs("Loaders/{0}{1}".format(loader,type), exist_ok=True)
		genIni('[!ActivateConfig ', loader, type, True)
		
		type="Unloader"
		os.makedirs("Loaders/{0}{1}".format(loader,type), exist_ok=True)
		genIni('[!DeactivateConfig ', loader, type)
		
		type="Refresher"
		os.makedirs("Loaders/{0}{1}".format(loader,type), exist_ok=True)
		genIni('[!Refresh ', loader, type, True)
			
if __name__ == '__main__':

	try:
		main()
	except Exception as e:
		input(traceback.format_exc())