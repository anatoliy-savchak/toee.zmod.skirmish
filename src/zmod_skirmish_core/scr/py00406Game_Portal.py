import toee, utils_storage, startup_zmod, utils_obj, const_proto_containers, debug, utils_pc, module_consts, const_toee
import py07710_skirmish_harbinger_monsters

def san_dialog(attachee, triggerer):
	triggerer.begin_dialog( attachee, 1 )
	return toee.SKIP_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	print("san_first_heartbeat {}".format(attachee))
	attachee.scripts[const_toee.sn_first_heartbeat] = 0
	zmod_startup()
	init_skirmisher()
	attachee.destroy()
	return toee.RUN_DEFAULT

def zmod_startup():
	utils_storage.Storage.reset()
	startup_zmod.zmod_conditions_apply_pc()
	return

def init_skirmisher():
	for pc in toee.game.party:
		pc.condition_add("SkirmisherStart")
	return