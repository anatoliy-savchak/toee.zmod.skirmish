import toee, templeplus.pymod, tpdp, debug, sys

###################################################

def GetConditionName():
	return "Base_Num_Attack"

print("Registering " + GetConditionName())
###################################################

def Base_Num_Attack_OnGetNumAttacksBase(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	
	v = args.get_arg(0)
	evt_obj.return_val = v
	return 0

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0 - number of base num attacks
modObj.AddHook(toee.ET_OnGetNumAttacksBase, toee.EK_NONE, Base_Num_Attack_OnGetNumAttacksBase, ())

