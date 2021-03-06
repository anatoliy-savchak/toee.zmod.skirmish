import toee, tpactions, debug

def GetActionName():
	return "Inspect"

def GetActionDefinitionFlags():
	return toee.D20ADF_Python
	
def GetTargetingClassification():
	return toee.D20TC_Target0

def GetActionCostType():
	return toee.D20ACT_Move_Action

def AddToSequence(d20action, action_seq, tb_status):
	action_seq.add_action(d20action)
	return toee.AEC_OK
