import toee, debug, tpdp, utils_storage, utils_npc_spells, const_toee, utils_tactics, const_proto_weapon, utils_item, const_proto_armor, const_proto_scrolls, ctrl_behaviour, utils_toee
import const_proto_potions, utils_obj, const_proto_food, utils_npc, utils_target_list, const_proto_wands, utils_sneak, const_deseases, utils_npc_spells, utils_npc
import const_proto_items, const_proto_rings, const_proto_cloth, const_proto_wondrous, utils_races, utils_npc_build, const_proto_npc, utils_npc_spells_tactics

THIS_SCRIPT_ID = 7710
def ctrl(npc): return ctrl_behaviour.get_ctrl(npc.id)
def san_start_combat(attachee, triggerer): return ctrl_behaviour.san_start_combat(attachee, triggerer)
def san_enter_combat(attachee, triggerer): return ctrl_behaviour.san_enter_combat(attachee, triggerer)
def san_end_combat(attachee, triggerer): return ctrl_behaviour.san_end_combat(attachee, triggerer)
def san_exit_combat(attachee, triggerer): return ctrl_behaviour.san_exit_combat(attachee, triggerer)
def san_will_kos(attachee, triggerer): return ctrl_behaviour.san_will_kos(attachee, triggerer)
def san_dialog(attachee, triggerer): return ctrl_behaviour.san_dialog(attachee, triggerer)
def san_heartbeat(attachee, triggerer): return ctrl_behaviour.san_heartbeat(attachee, triggerer)
def san_wield_off(attachee, triggerer): return ctrl_behaviour.san_wield_off(attachee, triggerer)

def get_character_classes():
	result = [\
		CtrlLGClericOfOrderAsPC\
		, CtrlLGClericOfYondallaAsPC\
		, CtrlLGDwarfAxefighter\
		, CtrlLGEmberHumanMonk
		, CtrlLGEvokersApprentice
		, CtrlLGHalflingVeteran
		, CtrlLGHoundArchon
		, CtrlLGHumanCommoner
		, CtrlLGLargeEarthElemental
		, CtrlLGManAtArms
		, CtrlLGSunSoulInitiate
		, CtrlLGSwordofHeironeousAsPC
		, CtrlLGTordekDwarfFighter
		, CtrlCGJozanClericOfPelor
		, CtrlCGArcaneArcherAsPC
		, CtrlCGAxeSister
		, CtrlCGCentaur
		, CtrlCGClericOfCorellonLarethianAsPC
		, CtrlCGCrestedFelldrake
		, CtrlCGDevisHalfElfBard
		, CtrlCGElfArcher
		, CtrlCGElfPyromancer
		, CtrlCGHumanWanderer
		, CtrlCGKruskHalfOrcBarbarian
		, CtrlCGLiddaHalflingRogue
		, CtrlLGNebinGnomeIllusionist
		, CtrlCGVadaniaHalfElfDruidAsPC
		, CtrlCGWildElfBarbarian
		, CtrlCGWoodElfSkirmisher
		, CtrlLEAzerRaider
		, CtrlLEHalfOrcMonk
		, CtrlLEDireBoar
		, CtrlLELizardfolk
		, CtrlLEShamblingMound
		, CtrlLEWolf
		, CtrlCEThriKreenRanger
		, CtrlLEBarghest
		, CtrlLEBeardedDevil
		, CtrlLEDisplacerBeast
		, CtrlLEGoblinSneak
		, CtrlCGHalfOrcFighterAsPC
		, CtrlLEHellHound
		, CtrlLEHumanBlackguardAsPC
		, CtrlLEHumanExecutioner
		, CtrlLEHumanThug
		, CtrlLEKoboldWarrior
		, CtrlLEMedusa
		, CtrlLEMindFlayer
		, CtrlLEMummy
	]
	return result

def get_enemy_classes():
	result = [\
		CtrlLGClericOfOrder\
		, CtrlLGClericOfYondalla\
		, CtrlLGDwarfAxefighter\
		, CtrlLGEmberHumanMonk
		, CtrlLGEvokersApprentice
		, CtrlLGHalflingVeteran
		, CtrlLGHoundArchon
		, CtrlLGHumanCommoner
		, CtrlLGLargeEarthElemental
		, CtrlLGManAtArms
		, CtrlLGSunSoulInitiate
		, CtrlLGSwordofHeironeous
		, CtrlLGTordekDwarfFighter
		, CtrlCGJozanClericOfPelor
		, CtrlCGArcaneArcher
		, CtrlCGAxeSister
		, CtrlCGCentaur
		, CtrlCGClericOfCorellonLarethian
		, CtrlCGCrestedFelldrake
		, CtrlCGDevisHalfElfBard
		, CtrlCGElfArcher
		, CtrlCGElfPyromancer
		, CtrlCGHumanWanderer
		, CtrlCGKruskHalfOrcBarbarian
		, CtrlCGLiddaHalflingRogue
		, CtrlLGNebinGnomeIllusionist
		, CtrlCGVadaniaHalfElfDruid
		, CtrlCGWildElfBarbarian
		, CtrlCGWoodElfSkirmisher
		, CtrlLEAzerRaider
		, CtrlLEHalfOrcMonk
		, CtrlLEDireBoar
		, CtrlLELizardfolk
		, CtrlLEShamblingMound
		, CtrlLEWolf
		, CtrlCEThriKreenRanger
		, CtrlLEBarghest
		, CtrlLEBeardedDevil
		, CtrlLEDisplacerBeast
		, CtrlLEGoblinSneak
		, CtrlCGHalfOrcFighter
		, CtrlLEHellHound
		, CtrlLEHumanBlackguard
		, CtrlLEHumanExecutioner
		, CtrlLEHumanThug
		, CtrlLEKoboldWarrior
		, CtrlLEMedusa
		, CtrlLEMindFlayer
		, CtrlLEMummy
	]
	return result

class CtrlSkirmisher(ctrl_behaviour.CtrlBehaviour):
	@classmethod
	def get_commander_level(cls): return 0

	@classmethod
	def get_price(cls): return 0

	@classmethod
	def get_alignment_group(cls): return toee.ALIGNMENT_NEUTRAL

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group()]

	def setup_name(self, npc, title):
		if (self.get_proto_id() // 1000 == 13):
			npc.obj_set_string(toee.obj_f_pc_player_name, title)
			return

		name_id = utils_toee.make_custom_name(title)
		if (name_id):
			npc.obj_set_int(toee.obj_f_critter_description_unknown, name_id)
			npc.obj_set_int(const_toee.obj_f_description_correct, name_id)
		return

	@staticmethod
	def _hide_loot(item):
		assert isinstance(item, toee.PyObjHandle)
		item.item_flag_set(toee.OIF_NO_LOOT)
		item.item_flag_set(toee.OIF_WONT_SELL)
		item.item_flag_set(toee.OIF_NO_PICKPOCKET)
		item.item_flag_set(toee.OIF_NO_DROP)
		item.item_flag_set(toee.OIF_NO_TRANSFER)
		return item

	@staticmethod
	def _lower_weight_small(item):
		assert isinstance(item, toee.PyObjHandle)
		item.obj_set_int(toee.obj_f_item_weight, item.obj_get_int(toee.obj_f_item_weight) // 2)
		return item

	@classmethod
	def get_title(cls): return None

	@classmethod
	def is_unique(cls): return False

	@classmethod
	def get_stats(cls): return {}

class CtrlSkirmisherLG(CtrlSkirmisher):
	@classmethod
	def get_alignment_group(cls): return toee.ALIGNMENT_LAWFUL_GOOD

class CtrlLGClericOfOrder(CtrlSkirmisherLG):
	# COMMANDER EFFECT: Followers rallied by this creature can take their turn normally if they	rally successfully.				
	# SPECIAL ABILITIES: Turn Undead 4 *.				
	# SPELLS: 1st-command ** (range 6; Stun; DC 13), shield of faith * (touch; +2 AC); 2nd—major resistance ** (touch; Save +3).
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_commander_level(cls): return 5

	@classmethod
	def get_price(cls): return 24

	@classmethod
	def get_title(cls): return "Cleric of Order"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "4", 
			"Spd": "6", 
			"AC": "16", 
			"HP": "25", 
			"Type": "Humanoid (Human)",
			"Melee": "+4 (5)",
			"Special Abilities": {
				"Turn Undead": "4"
			},
			"Commander Effect": "Followers rallied by this creature can take their turn normally if they rally successfully.",
			"Spells": "1st—command ❑❑ (range 6; Stun; DC 13), shield of faith ❑ (touch; +2 AC); 2nd—major resistance ❑❑ (touch; Save +3)."
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_cleric, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 4 chain shirt + 2 dex
		#SPD 40 (6) should be light armor
		#HP 25 = 1d8 + 3d8 + 4*x => 8 + 1 + 4.5 + 1 + 4.5 + 1 + 4.5 + 1 = 8 + 4 + 13.5 = 25 => con: 12

		#STR: 12 due to atk is 4 = 3 bab (lv 4) + 1 str; but dmg will be 1d6+1 = 7 not 5!
		#DEX: 14 due to AC dex mod = 2
		#CON: 12, see HP calculation
		#WIS: 14 due to 1st level DC: 13 => 10 + 1 lv + 2 mod wis
		#INT: 08 any
		#CHA: 12 due to Turn undead 4 times = 3 + 1 mod cha

		utils_npc.npc_abilities_set(npc, [12, 14, 12, 8, 14, 12])

		npc.obj_set_int(toee.obj_f_critter_portrait, 1070) #ELM_1070_b_adamo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.good)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.law)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_righteous_warrior)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_white
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_IVORY_TEMPLE_AIR, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_command, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_command, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_shield_of_faith, toee.stat_level_cleric, 1)

		npc.spell_memorized_add(toee.spell_resist_elements, toee.stat_level_cleric, 2)
		npc.spell_memorized_add(toee.spell_resist_elements, toee.stat_level_cleric, 2)
		npc.spells_pending_to_memorized()

		#utils_npc.npc_generate_hp_avg_first(npc)
		utils_npc.ensure_hp(npc, int(self.get_stats()["HP"]))
		npc.item_wield_best_all()
		return

class CtrlLGClericOfOrderAsPC(CtrlLGClericOfOrder):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HUMAN_MAN

class CtrlLGClericOfYondalla(CtrlSkirmisherLG):
	# COMMANDER EFFECT: Attack +2 against larger creatures. WARBAND BUILDING: Halflings of any faction are legal in your warband.
	# SPECIAL ABILITIES: Turn Undead 2 *.				
	# SPELLS: 1st-cure light wounds ** (touch; heal 5 hp), magic weapon * (touch; attack +1, ignore DR).
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFLING_MAN

	@classmethod
	def get_commander_level(cls): return 3

	@classmethod
	def get_price(cls): return 14

	@classmethod
	def get_title(cls): return "Cleric of Yondalla"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "2", 
			"Spd": "3", 
			"AC": "23", 
			"HP": "15", 
			"Type": "Small Humanoid (Halfling)",
			"Melee": "+0 (5)",
			"Special Abilities": {
				"Turn Undead": "4",
				"Save": "+4"
			},
			"Commander Effect": "Attack +2 against larger creatures. WARBAND BUILDING: Halflings of any faction are legal in your warband.",
			"Spells": "1st—cure light wounds ❑❑ (touch; heal 5 hp), magic weapon ❑ (touch; attack +1, ignore DR)."
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_cleric, int(self.get_stats()["Lvl"]))
		#AC 23 = 10 + 8 full plate + 0 dex + 1 small being + 4 tower shield
		#SPD 15 (2)
		#HP 15 = 1d8 + 1d8 + 2*x => 8 + 4 + 1 + 2*1 = 15 => con: 12

		#STR: 10 due to atk is 0 = 1 bab (lv 2) + 1 small - 2 tower; dmg will be 1d10 = 4 not 5!
		#DEX: 10 due to AC dex mod = 0
		#CON: 12, see HP calculation
		#WIS: 14 due to 1st level DC: 13 => 10 + 1 lv + 2 mod wis
		#INT: 08 any
		#CHA: 08 due to Turn undead 2 times = 3 - 1 mod cha

		utils_npc.npc_abilities_set(npc, [12, 8, 12, 12, 12, 8]) # -2 STR, +2 DEX

		npc.obj_set_int(toee.obj_f_critter_portrait, 10) #GNM_0010_b_illusionist
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_YONDALLA)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.good)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.protection)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_illusionist)

		#npc.feat_add(toee.feat_martial_weapon_proficiency_short_sword, 1)
		#npc.feat_add(toee.feat_martial_weapon_proficiency_longsword, 1)
		npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword, 1)
		npc.feat_add(toee.feat_tower_shield_proficiency, 1)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_GILDED_GLOVES, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_PLUMED_SILVER, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc)))
		#item = self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc)))
		#item.item_condition_add_with_args("Shield Enhancement Bonus", 1)
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_TOWER_STEEL, npc)))

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc)))

		#self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc)))
		#self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc)))
		item = self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD, npc)))
		item.obj_set_int(toee.obj_f_size, toee.STAT_SIZE_SMALL)

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_cure_light_wounds, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_cure_light_wounds, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_magic_weapon, toee.stat_level_cleric, 1)
		npc.spells_pending_to_memorized()

		#utils_npc.npc_generate_hp_avg_first(npc)
		utils_npc.ensure_hp(npc, int(self.get_stats()["HP"]))
		npc.item_wield_best_all()
		return

class CtrlLGClericOfYondallaAsPC(CtrlLGClericOfYondalla):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HALFLING_MAN

class CtrlLGDwarfAxefighter(CtrlSkirmisherLG):
	# SPECIAL ABILITIES: Cleave; Save +4.
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN

	@classmethod
	def get_price(cls): return 12

	@classmethod
	def get_title(cls): return "Dwarf Axefighter"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "3", 
			"Spd": "4", 
			"AC": "19", 
			"HP": "30", 
			"Type": "Humanoid (Dwarf)",
			"Melee": "+7 (10)",
			"Special Abilities": {
				"Cleave": "",
				"Save": "+4"
			}
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 19 = 10 + 5 chain mail + 2 dex + 2 heavy shield
		#SPD 20 (4)
		#HP 30 = 1d10 + 2d10 + 3*x => 10 + 2*10/2 + 1 + 3*2 = 31 => con: 14

		#STR: 16 due to atk is 7 = 3 bab (lv 3) + 2 str + 1 wpn foc + 1 mkw; dmg will be 1d8 + 2 = 10
		#DEX: 12 due to AC dex mod = 1
		#CON: 12, see HP calculation
		#WIS: 12 any
		#INT: 08 any
		#CHA: 08 due to Turn undead 2 times = 3 - 1 mod cha

		utils_npc.npc_abilities_set(npc, [14, 14, 12, 8, 12, 8]) # -2 CHA, +2 CON

		npc.obj_set_int(toee.obj_f_critter_portrait, 2000) #DWM_2000_b_fighter
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_weapon_focus_battleaxe, 0)
		npc.feat_add(toee.feat_cleave, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_GENERIC, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL_RED, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_MASTERWORK, npc))

		#utils_npc.npc_generate_hp_avg_first(npc)
		utils_npc.ensure_hp(npc, int(self.get_stats()["HP"]))
		npc.item_wield_best_all()
		return

class CtrlLGEmberHumanMonk(CtrlSkirmisherLG):
	# SPECIAL ABILITIES: Unique. Deflect Arrows (+4 AC against ranged attacks); Mobility (+4 AC against attacks of opportunity); Save +4; Stunning Attack ** (DC 15).
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	@classmethod
	def get_price(cls): return 18

	@classmethod
	def get_title(cls): return "Ember, Human Monk"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "6", 
			"Spd": "10", 
			"AC": "20", 
			"HP": "35", 
			"Type": "Humanoid (Human)",
			"Unique": "1",
			"Melee": "+7/+7 (5 magic)",
			"Special Abilities": {
				"Deflect Arrows": "+4 AC against ranged attacks",
				"Mobility": "+4 AC against attacks of opportunity",
				"Save": "+4",
				"Stunning Attack": {"Charges": "2", "DC": "15"}
			}
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_monk, int(self.get_stats()["Lvl"]))
		#AC 20 = 10 + 3 wis + 4 dex + 1 monk
		#SPD 20 (4)
		#HP 30 = 1d8 + 5d8 + 3*x => 8 + 5*(8+1)/2 + 6*1 = 36 => con: 12

		#STR: 16 due to atk is 7 = 4 bab (lv 6) + 1 str + 2 wpn foc + 1 magic - 1 flurry; dmg will be 1d6 + 2 = 5
		#DEX: 18 due to AC dex mod = 4
		#CON: 12, see HP calculation
		#WIS: 16 due to AC wis bonus = 3
		#INT: 08 any
		#CHA: 08 any

		utils_npc.npc_abilities_set(npc, [12, 18, 12, 8, 14, 8]) 

		npc.obj_set_int(toee.obj_f_critter_portrait, 570) #HUF_0570_b_monk
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_weapon_focus_quarterstaff, 0)
		npc.feat_add(toee.feat_greater_weapon_focus_quarterstaff, 0)
		npc.feat_add(toee.feat_dodge, 0)
		npc.feat_add(toee.feat_weapon_finesse_quarterstaff, 0)
		npc.feat_add(toee.feat_mobility, 1)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BRACERS_OF_ARMOR_PLUS_2, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_NATURAL_ARMOR_PLUS_1, npc))

		item = self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc))
		item.item_condition_add_with_args("Weapon Enhancement Bonus", 1)

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLGEvokersApprentice(CtrlSkirmisherLG):
	# SPELLS: 1st—magic missile * (sight; 5 damage), magic weapon * (touch; attack +1, ignore DR).
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 10

	@classmethod
	def get_title(cls): return "Evoker's Apprentice"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "1", 
			"Spd": "6", 
			"AC": "12", 
			"HP": "5", 
			"Type": "Humanoid (Human)",
			"Melee": "+0 (5)",
			"Spells": "1st—magic missile ❑ (sight; 5 damage), magic weapon ❑ (touch; attack +1, ignore DR)."
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_wizard, int(self.get_stats()["Lvl"]))
		#AC 12 = 10 + 2 dex
		#SPD 30 (6) should be light armor
		#HP 5 = 1d4 + 1 => con: 12

		#STR: 8 atk 0
		#DEX: 14 due to AC dex mod = 2
		#CON: 12, see HP calculation
		#INT: 12 wiz
		#WIS: 12 
		#CHA: 8 any

		utils_npc.npc_abilities_set(npc, [10, 14, 12, 12, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6200) #NPC_6201_m_Mickey
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_WHITE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_QUARTERSTAFF, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_magic_missile, toee.stat_level_wizard, 1)
		npc.spell_memorized_add(toee.spell_magic_weapon, toee.stat_level_wizard, 1)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLGHalflingVeteran(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFLING_MAN

	@classmethod
	def get_price(cls): return 11

	@classmethod
	def get_title(cls): return "Halfling Veteran"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "5", 
			"Spd": "4", 
			"AC": "19", 
			"HP": "35", 
			"Type": "Small Humanoid (Halfling)",
			"Melee": "+9/+9 (5)"
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 19 = 10 + 5 chain mail + 2 dex + 1 dodge + 1 twd
		#SPD 20 (4)
		#HP 35 = 1d10 + 4d10 + 3*x => 32 + 5*1 = 37 => con: 12

		#STR: 14 due to atk is 9 = 5 bab (lv 5) + 4 dex + 1 wpf + 1 mkw - 2 twf; dmg will be 1d4 + 1 = 5, str-2
		#DEX: 18 due to AC dex mod = 3 and 4 finesse
		#CON: 12, see HP calculation
		#INT: 08 any
		#WIS: 10
		#CHA: 08 any

		utils_npc.npc_abilities_set(npc, [14, 16, 12, 8, 10, 8]) # -2 STR, +2 DEX

		npc.obj_set_int(toee.obj_f_critter_portrait, 2520) #HAM_2520_b_cabral
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		#npc.feat_add(toee.feat_weapon_focus_dagger, 0)
		#npc.feat_add(toee.feat_greater_weapon_focus_quarterstaff, 0)
		npc.feat_add(toee.feat_dodge, 0)
		npc.feat_add(toee.feat_weapon_finesse_dagger, 0)
		npc.feat_add(toee.feat_two_weapon_fighting, 1)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc)))
		#self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL, npc)))

		dagger1 = self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER_MASTERWORK, npc))
		dagger2 = self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER_MASTERWORK, npc))

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		npc.item_wield(dagger1, toee.item_wear_weapon_primary)
		npc.item_wield(dagger2, toee.item_wear_weapon_secondary)
		return

class CtrlLGHoundArchon(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_JACKALWERE_EMPTY

	@classmethod
	def get_price(cls): return 31

	@classmethod
	def get_title(cls): return "Hound Archon"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "6", 
			"Spd": "8", 
			"AC": "19", 
			"HP": "35", 
			"Type": "Outsider",
			"Melee": "+8/+3 (10)",
			"Special Abilities": {
				"DR": "5",
				"Spell Resistance": "11",
			},
			"Spells": "4th—dimension door (unlimited uses) (self; place this creature in any space it can see at least part of)."
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [15, 10, 13, 10, 13, 12])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 2500) #HAM_2500_b_rogue
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 9) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		npc.condition_add_with_args("Spell Resistance", 11)
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30

		npc.feat_add(toee.feat_improved_initiative, 0)
		#npc.feat_add(toee.feat_power_attack, 1)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD, npc)) # avg 10

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLGHumanCommoner(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 3

	@classmethod
	def get_stats(cls): return {
			"Lvl": "1", 
			"Spd": "6", 
			"AC": "10", 
			"HP": "5", 
			"Type": "Humanoid (Human)",
			"Difficult": "7",
			"Melee": "+0 (5)",
			"Difficult": "7"
		}

	@classmethod
	def get_title(cls): return "Human Commoner"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 4, 0)
		utils_npc.npc_abilities_set(npc, [10, 10, 12, 10, 10, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6210) #NPC_6211_m_Tupperelo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_GREEN, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SCYTHE, npc))

		npc.feat_add(toee.feat_martial_weapon_proficiency_scythe, 1)
		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLGLargeEarthElemental(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELEMENTAL_EARTH_LARGE_EMPTY

	@classmethod
	def get_price(cls): return 35

	@classmethod
	def get_title(cls): return "Large Earth Elemental"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "8", 
			"Spd": "4", 
			"AC": "18", 
			"HP": "70", 
			"Type": "Large Elemental",
			"Difficult": "12",
			"Melee": "+4/+4 (25)",
			"Special Abilities": {
				"Requires Commander Ally": "",
				"Burrow": "4",
				"Cleave": "",
				"DR": "5",
				"Melee Reach": "2"
			}
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [25, 8, 19, 6, 11, 11])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 2500) #HAM_2500_b_rogue
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 10) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 6)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 2)

		# atk 12 = 6 bab (Elemental HD 8*3/4) + 7 str - 1 large
		# atk must be 4 => power attack -8

		# atk +4/+4 => -3/-3 dmg 2d8+7 + 8=> (17 + 31)/2=24
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_slap)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 6) # bab 6?
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2)
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("2d8").packed)

		npc.feat_add(toee.feat_cleave, 0)
		npc.feat_add(toee.feat_power_attack, 0)

		npc.condition_add("Monster Subdual Immunity")
		npc.condition_add("Monster Special Fade Out")
		npc.condition_add("Monster Plant")
		npc.condition_add_with_args("Monster DR Magic", 5)

		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal("Set Power Attack Value", 8) # should go after refresh status, as it will be reset
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLGManAtArms(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 3

	@classmethod
	def get_title(cls): return "Man-at-Arms"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "1", 
			"Spd": "4", 
			"AC": "19", 
			"HP": "5", 
			"Type": "Humanoid (Human)",
			"Melee": "+3 (5)"
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 4, 0)
		utils_npc.npc_abilities_set(npc, [10, 10, 12, 10, 10, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6880) #NPC_6881_m_L_Guard
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_GILDED_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_GREAT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_HALF_PLATE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc))

		npc.feat_add(toee.feat_martial_weapon_proficiency_short_sword, 1)
		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLGSunSoulInitiate(CtrlSkirmisherLG):
	# SPECIAL ABILITIES: Deflect Arrows (+4 AC against ranged attacks); Mobility (+4 AC against attacks of opportunity); Save +4; Stunning Attack * (DC 13).					
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 8

	@classmethod
	def get_title(cls): return "Sun Soul Initiate"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "3", 
			"Spd": "8", 
			"AC": "15", 
			"HP": "15", 
			"Type": "Humanoid (Human)",
			"Melee": "+3/+3 (5)",
			"Special Abilities": {
				"Deflect Arrows": "+4 AC against ranged attacks",
				"Mobility": "+4 AC against attacks of opportunity",
				"Save +4": "",
				"Stunning Attack": "Charges: 1, DC: 13",
			}
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_monk, int(self.get_stats()["Lvl"]))
		#AC 15 = 10 + 2 wis + 3 dex + 0 monk
		#SPD 20 (4)
		#HP 15 = 1d8 + 2d8 + 3*x => 8 + 5*(8+1)/2 + 3*0 = 16 => con: 10

		#STR: 14 due to atk is 3 = 2 bab (lv 3) + 1 str + 1 wf - 2 flurry; dmg will be 1d6 + 2 = 6
		#DEX: 16 due to AC dex mod = 3
		#CON: 10, see HP calculation
		#INT: 08 any
		#WIS: 14 due to Stunning Attack 13 (10 + 1(1/2 lv) + wis 2)
		#CHA: 08 any

		utils_npc.npc_abilities_set(npc, [14, 16, 10, 8, 14, 8]) 

		npc.obj_set_int(toee.obj_f_critter_portrait, 7880) #NPC_7881_m_Vincent
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		#npc.feat_add(toee.feat_weapon_focus_unarmed_strike_medium_sized_being, 0)
		npc.feat_add(toee.feat_weapon_finesse_unarmed_strike_medium_sized_being, 0)
		npc.feat_add(toee.feat_mobility, 1)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_MONK_BROWN, npc))

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLGSwordofHeironeous(CtrlSkirmisherLG):
	# COMMANDER EFFECT: Attack +2 against larger creatures. WARBAND BUILDING: Halflings of any faction are legal in your warband.
	# SPECIAL ABILITIES: Fearless; Smite Evil +5 *.	
	# SPELLS: 2nd—cure moderate wounds * (touch; heal 10 hp).
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	@classmethod
	def get_commander_level(cls): return 7

	@classmethod
	def get_price(cls): return 29

	@classmethod
	def get_title(cls): return "Sword of Heironeous"

	def get_stats(cls): return {
			"Lvl": "5", 
			"Spd": "4", 
			"AC": "20", 
			"HP": "35", 
			"Type": "Humanoid (Human)",
			"Melee": "+8 (10 magic)",
			"Special Abilities": {
				"Fearless": "",
				"Smite Evil": "+5"
			},
			"Commander Effect": "+1 AC.",
			"Spells": "2nd—cure moderate wounds ❑ (touch; heal 10 hp).",
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_paladin, int(self.get_stats()["Lvl"]))
		#AC 23 = 10 + 8 full plate + 2 heavy shield
		#SPD 20 (4)
		#HP 35 => con: 12

		#STR: 14 due to atk is 8 = 5 bab (lv 5) + 3 str + 1 magic - 1 pwr; dmg~9.5
		#DEX: 10 due to AC dex mod = 0
		#CON: 12, see HP calculation
		#INT: 08 any
		#WIS: 13
		#CHA: 10 as Smite Evil +5 = +5 lv + 0 cha

		utils_npc.npc_abilities_set(npc, [16, 10, 12, 8, 13, 10])

		npc.obj_set_int(toee.obj_f_critter_portrait, 580) #HUF_0580_b_paladin
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.good)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.protection)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvf_pious)

		npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword, 0)
		npc.feat_add(toee.feat_power_attack, 0)
		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal(toee.S_SetPowerAttack, 1) # should go after refresh status, as it will be reset
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_medium
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_GILDED_GLOVES, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_PLUMED_SILVER, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_STEEL, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_cure_moderate_wounds, toee.stat_level_paladin, 1)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLGSwordofHeironeousAsPC(CtrlLGSwordofHeironeous):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HUMAN_WOMAN

class CtrlLGTordekDwarfFighter(CtrlSkirmisherLG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN # 14638

	@classmethod
	def get_price(cls): return 5

	@classmethod
	def get_title(cls): return "Tordek, Dwarf Fighter"

	def get_stats(cls): return {
			"Lvl": "1", 
			"Spd": "4", 
			"AC": "17", 
			"HP": "15", 
			"Type": "Humanoid (Dwarf)",
			"Melee": "+5 (5)",
			"Special Abilities": {
				"Save": "+4"
			},
			"Unique": "1",
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 5 chain mail + 0 dex + 2 shield
		#SPD 20 (4) should be med armor
		#HP 10 = 1d10 + 5 => con: 14

		#STR: 14 due to atk is 5 = 1 bab (lv 1) + 2 str + 1 mkw + 1 focus; dmg will be 1d8+2 ~ 6.5
		#DEX: 10 due to AC dex mod = 0
		#CON: 20, see HP calculation
		#INT: 08 any
		#WIS: 12 
		#CHA: 08 
		utils_npc.npc_abilities_set(npc, [14, 10, 20-2, 12, 12, 10])

		npc.obj_set_int(toee.obj_f_critter_portrait, 2030) # DWM_2030_b_fighter
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())

		npc.feat_add(toee.feat_weapon_focus_battleaxe, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_longhair
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL_RED, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_BATTLEAXE_MASTERWORK, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_4, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlSkirmisherCG(CtrlSkirmisher):
	@classmethod
	def get_alignment_group(cls): return toee.ALIGNMENT_CHAOTIC_GOOD

class CtrlCGJozanClericOfPelor(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 4

	@classmethod
	def get_title(cls): return "Jozan, Cleric Of Pelor"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD]

	def get_stats(cls): return {
			"Lvl": "4", 
			"Spd": "4", 
			"AC": "16", 
			"HP": "10", 
			"Type": "Humanoid (Human)",
			"Melee": "+2 (5)",
			"Special Abilities": {
				"Turn Undead": "4",
			},
			"Unique": "1",
			"Spells": "1st—command ❑ (range 6; Stun; DC 13), cure light wounds ❑ (touch; heal 5 hp).",
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_cleric, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 5 chain mail + 0 dex + 1 light shield
		#SPD 20 (4) should be med armor
		#HP 10 = 1d8 + 2 => con: 14

		#STR: 14 due to atk is 2 = 0 bab (lv 1) + 2 str; dmg will be 1d6+2 ~ 5
		#DEX: 10 due to AC dex mod = 0
		#CON: 14, see HP calculation
		#INT: 08 any
		#WIS: 14 due to 1st level DC: 13 => 10 + 1 lv + 2 mod wis
		#CHA: 08 due to Turn undead 2 times = 3 - 1 mod cha

		utils_npc.npc_abilities_set(npc, [14, 10, 14, 8, 14, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6570) #NPC_6571_m_Jaer
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_PELOR)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.healing)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.strength)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLUE, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MACE_LIGHT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_STEEL_2, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_command, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_cure_light_wounds, toee.stat_level_cleric, 1)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGArcaneArcher(CtrlSkirmisherCG):
	# COMMANDER EFFECT: Followers with ranged attacks gain ranged attack +2, Selective Shot 2.	SPECIAL ABILITIES: Precise Shot; 
	#
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_WOMAN

	@classmethod
	def get_price(cls): return 48

	@classmethod
	def get_title(cls): return "Arcane Archer"

	@classmethod
	def get_commander_level(cls): return 3

	def get_stats(cls): return {
			"Lvl": "8", 
			"Spd": "6", 
			"AC": "17", 
			"HP": "40", 
			"Type": "Humanoid (Elf)",
			"Melee": "+8/+3 (5)",
			"Ranged": " +13/+13/+8 (5 magic)",
			"Commander Effect": "Followers with ranged attacks gain ranged attack +2, Selective Shot 2.",
			"Special Abilities": {
				"Precise Shot": "",
				"Selective Shot": "2",
			}
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_ranger, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 2 leather + 5 dex
		#SPD 30 (6) should be light armor
		#HP 10 = 1d8 + 7(d8 + 1)/2 => con: 10

		#STR: 10 due to atk is 8 = 8 bab (lv 8) + 0 str; dmg will be 1d8+2 = 5.5
		#DEX: 10 due to ranged atk is 15 = 8 bab (lv 8) + 5 dex + 1 wfc + 1 magic; dmg will be 1d8+1 = (2+9)/2=5.5
		#CON: 10, see HP calculation
		#INT: 08 any
		#WIS: 10 any
		#CHA: 08

		utils_npc.npc_abilities_set(npc, [10, 18, 12, 8, 10, 8]) # elf +2 dex -2 con

		npc.obj_set_int(toee.obj_f_critter_portrait, 510) #HUF_0510_b_ranger
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)
		#npc.obj_set_int(toee.obj_f_critter_domain_1, toee.healing)
		#npc.obj_set_int(toee.obj_f_critter_domain_2, toee.strength)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_righteous_warrior)

		npc.feat_add(toee.feat_weapon_focus_longbow, 0)
		npc.feat_add(toee.feat_point_blank_shot, 0)
		npc.feat_add(toee.feat_precise_shot, 0)
		npc.feat_add(toee.feat_rapid_shot, 0)

		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal("Rapid Shot Check") # should go after refresh status, as it will be reset

		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_GREEN, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_1, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGArcaneArcherAsPC(CtrlCGArcaneArcher):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_ELF_WOMAN

class CtrlCGAxeSister(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOMAN

	@classmethod
	def get_price(cls): return 21

	@classmethod
	def get_title(cls): return "Axe Sister"

	def get_stats(cls): return {
			"Lvl": "5", 
			"Spd": "8", 
			"AC": "15", 
			"HP": "50", 
			"Type": "Humanoid (Human)",
			"Melee": "+10 (15)",
			"Special Abilities": {
				"Whirlwind Attack": "on its turn, if this creature moves no more than 1 square, it can make one melee attack against every enemy creature it threatens"
			},
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_barbarian, int(self.get_stats()["Lvl"]))
		#AC 15 = 10 + 4 shirt + 3 dex - 2 rage
		#SPD 30 (6) should be light armor
		#HP 40 = 1d12 + 4(d12 + 1)/2 => con: 10

		#STR: 16 (20) due to atk is 10 = 5 bab (lv 5) + 5 str; dmg will be 1d12+7 = 13.5
		#DEX: 16
		#CON: 10, see HP calculation
		#INT: 08 any
		#WIS: 10 any
		#CHA: 08

		utils_npc.npc_abilities_set(npc, [16, 16, 10, 8, 10, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 7200) #NPC_7201_m_Mandy, NPC_6751_m_ElfNoblewoman
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)
		#npc.obj_set_int(toee.obj_f_critter_domain_1, toee.healing)
		#npc.obj_set_int(toee.obj_f_critter_domain_2, toee.strength)
		npc.obj_set_int(toee.obj_f_critter_strategy, 96)

		npc.feat_add(toee.feat_whirlwind_attack, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT_MASTERWORK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_GREEN, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD, npc))

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGCentaur(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return 14428

	@classmethod
	def get_price(cls): return 20

	@classmethod
	def get_title(cls): return "Centaur"

	def get_stats(cls): return {
			"Lvl": "5", 
			"Spd": "8", 
			"AC": "15", 
			"HP": "25",
			"Type": "Large Monstrous Humanoid",
			"Melee": "+7/+3 (10)",
			"Ranged": "+5 (10)",
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [18, 14, 14, 8, 13, 11])

		npc.obj_set_int(toee.obj_f_critter_portrait, 4400)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 3) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 1)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 4)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 4)

		npc.obj_set_int(toee.obj_f_critter_monster_category, const_toee.mc_type_monstrous_humanoid)
		# bab will be same as HD = 4. this is 1 attack if full action, but we need 2.

		npc.condition_add_with_args("Base_Num_Attack", 2) # should be 2
		npc.condition_add_with_args("Enlarged_Weapons", 1) # should be larger
		npc.condition_add_with_args("Base_Movement", 0, 166) # should be 50 ft

		npc.feat_add(toee.feat_dodge, 0)
		npc.feat_add(toee.feat_martial_weapon_proficiency_longsword, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		#hairStyle = utils_npc.HairStyle.from_npc(npc)
		#hairStyle.style = const_toee.hair_style_shorthair
		#hairStyle.color = const_toee.hair_color_black
		#hairStyle.update_npc(npc)

		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GARB_VILLAGER_GREEN, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_COMPOSITE_16, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlCGClericOfCorellonLarethian(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_MAN

	@classmethod
	def get_price(cls): return 25

	@classmethod
	def get_title(cls): return "Cleric of Corellon Larethian"

	def get_stats(cls): return {
			"Lvl": "4", 
			"Spd": "6", 
			"AC": "16", 
			"HP": "25", 
			"Type": "Humanoid (Elf)",
			"Melee": "+5 (5)",
			"Special Abilities": {
				"Turn Undead": "4",
			},
			"Commander Effect": "Elf followers gain Save +4",
			"Spells": "1st—bless ❑ (your warband; attack +1), magic weapon ❑❑ (touch; attack +1, ignore DR); 2nd—hold person ❑❑ (sight; Humanoids only, Paralysis; DC 14), cure moderate wounds ❑ (touch; heal 10 hp).",
		}


	@classmethod
	def get_commander_level(cls): return 4

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_cleric, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 4 chain shirt + 1 dex + 1 light shield
		#SPD 30 (6) should be light armor
		#HP 25 = 1d8 + 3d8 + con*3 => con: 12

		#STR: 12 due to atk is 5 = 3 bab (lv 4) + 1 str + 1 wf; dmg will be 1d8+1 = (1+9)/2=5
		#DEX: 12 due to AC dex mod = 1
		#CON: 12, see HP calculation
		#INT: 08 any
		#WIS: 14 due to level 2 DC: 14
		#CHA: 12 due to Turn undead 4 times = 3 + 1 mod cha

		utils_npc.npc_abilities_set(npc, [12, 10, 14, 8, 14, 12])# elf +2 dex -2 con

		npc.obj_set_int(toee.obj_f_critter_portrait, 1510) #HEM_1510_b_bard
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.protection)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.war)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_nature_dweller)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_blue
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_CHAINMAIL_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_CHAINMAIL_GLOVES, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_VIOLET, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_STEEL_2, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_bless, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_bless, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_magic_weapon, toee.stat_level_cleric, 1)
		npc.spell_memorized_add(toee.spell_magic_weapon, toee.stat_level_cleric, 1)

		npc.spell_memorized_add(toee.spell_hold_person, toee.stat_level_cleric, 2)
		npc.spell_memorized_add(toee.spell_hold_person, toee.stat_level_cleric, 2)
		npc.spell_memorized_add(toee.spell_cure_moderate_wounds, toee.stat_level_cleric, 2)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGClericOfCorellonLarethianAsPC(CtrlCGClericOfCorellonLarethian):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_ELF_MAN

class CtrlCGCrestedFelldrake(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return 14722

	@classmethod
	def get_price(cls): return 5

	@classmethod
	def get_title(cls): return "Crested Felldrake"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 2, 12, 0)
		utils_npc.npc_abilities_set(npc, [11, 10, 15, 6, 12, 9])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 4400) # todo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 4) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 3)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 3)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 3)

		npc.obj_set_int(toee.obj_f_critter_monster_category, const_toee.mc_type_dragon)
		# bab will be same as HD = 2. But it wont work in actual attacks for monsters...

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_bite)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 2)
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1)
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d8").packed)


		#npc.condition_add_with_args("Base_Num_Attack", 3) # should be 2
		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlCGDevisHalfElfBard(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFELF_MAN

	@classmethod
	def get_price(cls): return 6

	@classmethod
	def get_title(cls): return "Devis, Half-Elf Bard"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_bard, 3)
		#AC 16 = 10 + 3 dex + 3 st leather
		#SPD 30 (6) should be light armor
		#HP 15 = 1d6 + 2d6 + x => con: 12

		#STR: 12 atk 3
		#DEX: 16 due to AC dex mod = 3
		#CON: 12, see HP calculation
		#INT: 10
		#WIS: 12 
		#CHA: 14

		utils_npc.npc_abilities_set(npc, [12, 16, 12, 10, 12, 14])

		npc.obj_set_int(toee.obj_f_critter_portrait, 7140) #NPC_7141_m_Moneir
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_GREEN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc))

		npc.spells_memorized_forget()
		npc.spell_known_add(toee.spell_cure_light_wounds, toee.stat_level_bard, 1)
		#npc.spell_known_add(toee.spell_cure_light_wounds, toee.stat_level_bard, 1)
		npc.spell_known_add(toee.spell_lesser_confusion, toee.stat_level_bard, 1)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGElfArcher(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_MAN

	@classmethod
	def get_price(cls): return 10

	@classmethod
	def get_title(cls): return "Elf Archer"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_ranger, 1)
		#AC 15 = 10 + 2 leather + 3 dex
		#SPD 30 (6) should be light armor
		#HP 10 = 1d8 + x => con: 14

		#STR: 12 due to atk is 2 = 1 bab (lv 1) + 1 str; dmg will be 1d6+1 = 4.5
		#DEX: 16 due to ranged atk is 6 = 1 bab (lv 1) + 3 dex + 1 mkw; dmg will be 1d6+1 = (2+7)/2=4.5
		#CON: 14, see HP calculation
		#INT: 08 any
		#WIS: 10 any
		#CHA: 08

		utils_npc.npc_abilities_set(npc, [12, 14, 16, 8, 10, 8]) # elf +2 dex -2 con

		npc.obj_set_int(toee.obj_f_critter_portrait, 1040) #ELM_1040_b_ranger
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)
		#npc.obj_set_int(toee.obj_f_critter_domain_1, toee.healing)
		#npc.obj_set_int(toee.obj_f_critter_domain_2, toee.strength)

		npc.feat_add(toee.feat_weapon_focus_shortbow, 0)
		npc.feat_add(toee.feat_point_blank_shot, 0)
		#npc.feat_add(toee.feat_precise_shot, 0)
		#npc.feat_add(toee.feat_rapid_shot, 0)

		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal("Rapid Shot Check") # should go after refresh status, as it will be reset

		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_topknot
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CAP_LEATHER, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_GREEN, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW_MASTERWORK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc))

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGElfPyromancer(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_WOMAN

	@classmethod
	def get_price(cls): return 32

	@classmethod
	def get_title(cls): return "Elf Pyromancer"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_wizard, 6)
		#AC 16 = 10 + 3 dex
		#SPD 30 (6)
		#HP 20 = 1d4 + 5d4 + x => con: 12

		#STR: 10 atk 3
		#DEX: 16 due to AC dex mod = 3
		#CON: 12, see HP calculation
		#INT: 14
		#WIS: 12 
		#CHA: 14

		utils_npc.npc_abilities_set(npc, [10, 14, 14, 14, 10, 8]) # elf +2 dex -2 con

		npc.obj_set_int(toee.obj_f_critter_portrait, 1110) #ELF_1110_b_adamo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_BOCCOB)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_longhair
		hairStyle.color = const_toee.hair_color_blonde
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_WHITE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_LONGSWORD, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_magic_missile, toee.stat_level_wizard, 1)
		npc.spell_memorized_add(toee.spell_magic_missile, toee.stat_level_wizard, 1)
		npc.spell_memorized_add(toee.spell_magic_missile, toee.stat_level_wizard, 1)

		npc.spell_memorized_add(toee.spell_resist_elements, toee.stat_level_wizard, 2)
		npc.spell_memorized_add(toee.spell_scorching_ray, toee.stat_level_wizard, 2)
		npc.spell_memorized_add(toee.spell_scorching_ray, toee.stat_level_wizard, 2)

		npc.spell_memorized_add(toee.spell_fireball, toee.stat_level_wizard, 3)
		npc.spell_memorized_add(toee.spell_protection_from_elements, toee.stat_level_wizard, 3)

		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGHumanWanderer(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 13

	@classmethod
	def get_title(cls): return "Human Wanderer"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_ranger, 3)
		#AC 16 = 10 + 2 dex + 3 st leather
		#SPD 30 (6)
		#HP 20 = ...

		#STR: 10 atk 4 = 3 bab + 2 str + 1 wf - 2 twf
		#DEX: 15 due to AC dex mod = 3
		#CON: 12, see HP calculation
		#INT: 8
		#WIS: 10 
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [14, 14, 12, 8, 10, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 7870) #NPC_7871_m_SkoleGoon
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)

		npc.feat_add(toee.feat_two_weapon_fighting_ranger, 0)
		npc.feat_add(toee.feat_weapon_focus_short_sword, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_GREEN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_ORANGE, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlCGKruskHalfOrcBarbarian(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFORC_MAN

	@classmethod
	def get_price(cls): return 16

	@classmethod
	def get_title(cls): return "Krusk, Half-Orc Barbarian"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_barbarian, 3)
		#AC 14 = 10 + 3 dex + 3 st leather - 2 rage
		#SPD 30 (6)
		#HP 35 = 6 rage + 1d12 {=18} + 2d12 {13+18=31} + 1con x 3 {31+3=34}

		#STR: 18 atk 10 = 3 bab + 4 str + 2 str rage + 1 wf, 1d12+9: 10<->21 =>15.5
		#DEX: 16 due to AC dex mod = 3
		#CON: 12, see HP calculation
		#INT: 6
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [16, 16, 12, 8, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 3080) #HOM_3080_b_cabral
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)

		npc.feat_add(toee.feat_weapon_focus_greataxe, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_mohawk
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlCGLiddaHalflingRogue(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFLING_WOMAN

	@classmethod
	def get_price(cls): return 4

	@classmethod
	def get_title(cls): return "Lidda, Halfling Rogue"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_rogue, 1)
		#AC 16 = 10 + 2 leather + 3 dex + small
		#SPD 20 (4)
		#HP 5 = 1d6-1

		#STR: 10 due to atk is 1 = 0 bab + 1 small
		#DEX: 16 due to AC dex mod = 3
		#CON: 8, see HP calculation
		#INT: 08 any
		#WIS: 10
		#CHA: 08 any

		utils_npc.npc_abilities_set(npc, [12, 14, 8, 8, 10, 8]) # -2 STR, +2 DEX

		npc.obj_set_int(toee.obj_f_critter_portrait, 2500) #HAM_2500_b_rogu
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_GREEN, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BROWN, npc)))
		#self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELMET_CHAIN, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_TAN, npc)))

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_BOLT_QUIVER, npc))).obj_set_int(toee.obj_f_ammo_quantity, 100)
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSWORD, npc)))

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLGNebinGnomeIllusionist(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_GNOME_MAN

	@classmethod
	def get_price(cls): return 18

	@classmethod
	def get_title(cls): return "Nebin, Gnome Illusionist"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_wizard, 4)
		#AC 12 = 10 + 1 dex + 4 br
		#HP 20 = 1d4 + 3d4 + 4x => 4 + 8 + 4x = con: 14

		#STR: 10 atk 0
		#DEX: 12 due to AC dex mod = 1
		#CON: 14, see HP calculation
		#INT: 14 wiz
		#WIS: 12 
		#CHA: 8 any

		utils_npc.npc_abilities_set(npc, [12, 12, 12, 14, 12, 8]) # -2 STR, +2 CON

		npc.obj_set_int(toee.obj_f_critter_portrait, 640) #HUM_0640_b_cabral
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_WHITE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_BROWN_TEMPLE_EARTH, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_BRACERS_OF_ARMOR_PLUS_4, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CLUB, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_color_spray, toee.stat_level_wizard, 1)
		npc.spell_memorized_add(toee.spell_color_spray, toee.stat_level_wizard, 1)
		npc.spell_memorized_add(toee.spell_magic_weapon, toee.stat_level_wizard, 1)

		npc.spell_memorized_add(toee.spell_blur, toee.stat_level_wizard, 2)
		npc.spell_memorized_add(toee.spell_blur, toee.stat_level_wizard, 2)
		npc.spell_memorized_add(toee.spell_melfs_acid_arrow, toee.stat_level_wizard, 2)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGVadaniaHalfElfDruid(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFELF_WOMAN

	@classmethod
	def get_price(cls): return 22

	@classmethod
	def get_title(cls): return "Vadania, Half-Elf Druid"

	@classmethod
	def get_commander_level(cls): return 2

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_druid, 3)
		#AC 18 = 10 + 5 breastplate + 2 shield + 1 dex
		#HP 20 = 1d8 + 2d8 + 3x => 8 + 9 + 3x = con: 12

		#STR: 14 atk 4 = 2 bab + 2 str
		#DEX: 12 due to AC dex mod = 1
		#CON: 12, see HP calculation
		#INT: 14 wiz
		#WIS: 12 
		#CHA: 8 any

		utils_npc.npc_abilities_set(npc, [14, 12, 12, 14, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 760) #HUF_0760_b_adamo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvf_charismatic)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_braids
		hairStyle.color = const_toee.hair_color_pink
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BROWN, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_VIOLET, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_BREASTPLATE_LAMELLAR, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_ELVISH, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_SCIMITAR, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_magic_fang, toee.stat_level_druid, 1)
		npc.spell_memorized_add(toee.spell_magic_fang, toee.stat_level_druid, 1)
		npc.spell_memorized_add(toee.spell_produce_flame, toee.stat_level_druid, 1)

		npc.spell_memorized_add(toee.spell_cats_grace, toee.stat_level_druid, 2)
		npc.spell_memorized_add(toee.spell_cats_grace, toee.stat_level_druid, 2)
		#npc.spell_memorized_add(toee.spell_flame_blade, toee.stat_level_druid, 2)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlCGVadaniaHalfElfDruidAsPC(CtrlCGVadaniaHalfElfDruid):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HALFELF_WOMAN

class CtrlCGWildElfBarbarian(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_MAN

	@classmethod
	def get_price(cls): return 13

	@classmethod
	def get_title(cls): return "Wild Elf Barbarian"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_barbarian, 2)
		#AC 12 = 10 + 1 dex + 3 barb - 2 rage
		#SPD 30 (6)
		#HP 25 = 4 rage + 1d12 {=18} + 1d12 {7+18=25}

		#STR: 12 atk 6 = 2 bab + 1 str + 2 str rage + 1 wf, 1d6+3: 4<->9 =>16.5
		#DEX: 12 due to AC dex mod = 1
		#CON: 12, see HP calculation
		#INT: 6
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [12, 12, 12, 8, 12, 8]) # race_wild_elf
		npc.obj_set_int(toee.obj_f_critter_race, toee.race_wild_elf)

		npc.obj_set_int(toee.obj_f_critter_portrait, 1080) #ELM_1080_b_adamo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)

		npc.feat_add(toee.feat_weapon_focus_handaxe, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_mohawk
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_COMBAT, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlCGWoodElfSkirmisher(CtrlSkirmisherCG):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_ELF_WOMAN

	@classmethod
	def get_price(cls): return 18

	@classmethod
	def get_title(cls): return "Wood Elf Skirmisher"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_ranger, 3)
		#AC 13 = 10 + 3 dex
		#SPD 30 (6)
		#HP 20 = 1d8 {=8} + 2d8 {9+8=17}

		#STR: 14 atk 5 = 3 bab + 2 str, 1d6+2: 3<->8 =>5.5
		#DEX: 16 due to AC dex mod = 3
		#CON: 12, see HP calculation
		#INT: 10
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [10, 14, 10, 10, 12, 8]) # race_wood_elf
		npc.obj_set_int(toee.obj_f_critter_race, toee.race_wood_elf)

		npc.obj_set_int(toee.obj_f_critter_portrait, 2560) #HAF_2560_b_adamo
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_CORELLON_LARETHIAN)

		npc.feat_add(toee.feat_weapon_focus_longbow, 0)
		npc.feat_add(toee.feat_point_blank_shot, 0)
		npc.feat_add(toee.feat_precise_shot, 0)
		npc.feat_add(toee.feat_rapid_shot, 0)

		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal("Rapid Shot Check") # should go after refresh status, as it will be reset
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_longhair
		hairStyle.color = const_toee.hair_color_brown
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_RED, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MONK_OUTFIT, npc))
		
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_HANDAXE, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_LONGBOW_MASTERWORK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlSkirmisherLE(CtrlSkirmisher):
	@classmethod
	def get_alignment_group(cls): return toee.ALIGNMENT_LAWFUL_EVIL

class CtrlLEAzerRaider(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_DWARF_MAN # 14638

	@classmethod
	def get_price(cls): return 5

	@classmethod
	def get_title(cls): return "Azer Raider"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 2, 8, 0)
		utils_npc.npc_abilities_set(npc, [13, 13, 13-2, 12, 12, 9+2])

		npc.obj_set_int(toee.obj_f_critter_portrait, 2000) # DWM_2000_b_fighter
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEIRONEOUS)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 2) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 3)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 3)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 3)
		#obj_f_scale

		cat = const_toee.mc_type_outsider + ((toee.mc_subtype_fire & toee.mc_subtype_extraplanar) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)
		# bab will be same as HD = 2. But it wont work in actual attacks for monsters...

		#npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_bite)
		#npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 2)
		#npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1)
		#npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d8").packed)


		#npc.condition_add_with_args("Base_Num_Attack", 3) # should be 2
		#npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add_with_args("Base_Movement", 0, 150) # should be 30 ft, factor: 1.33 = 30/20
		npc.condition_add_with_args("Monster Bonus Damage", toee.D20DT_FIRE, toee.dice_new("1d6").packed)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_longhair
		hairStyle.color = const_toee.hair_color_red
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_RED, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_SCALE_MAIL_FINE, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_WARHAMMER, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_SPIKED, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEHalfOrcMonk(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFORC_MAN

	@classmethod
	def get_price(cls): return 17

	@classmethod
	def get_title(cls): return "Half-Orc Monk"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_monk, 4)
		#AC 14 = 10 + 1 wis + 2 dex + 1 monk
		#SPD 20 (4)
		#HP 25 = 1d8 + 3d8 + 3*x => 

		#STR: 18 due to atk is 7 = 3 bab (lv 4) + 3 str + +1 wndrs + 1 wpn foc + 1 monk - 2 flurry; dmg will be 1d6 + 2 = 8
		#DEX: 14 due to AC dex mod = 2
		#CON: 12, see HP calculation
		#INT: 08 any
		#WIS: 12 due to AC wis bonus = 1
		#CHA: 08 any

		utils_npc.npc_abilities_set(npc, [16, 14, 12, 8, 12, 8]) 

		npc.obj_set_int(toee.obj_f_critter_portrait, 3030) #HOM_3030_b_fighter
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEXTOR)

		# +7/7 (10 magic)
		npc.feat_add(toee.feat_weapon_focus_unarmed_strike_medium_sized_being, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_ponytail
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_MONK, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_ROBES_MONK_ORANGE, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_wondrous.PROTO_WONDROUS_AMULET_OF_MIGHTY_FISTS_PLUS_1, npc))
		
		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLEDireBoar(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14979

	@classmethod
	def get_price(cls): return 23

	@classmethod
	def get_title(cls): return "Dire Boar"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD, toee.ALIGNMENT_CHAOTIC_GOOD, toee.ALIGNMENT_CHAOTIC_EVIL]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 7, 8, 0)
		utils_npc.npc_abilities_set(npc, [10+12*2, 10, 17, 2, 13, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 4780) # MOO_4781_m_Dire_Boar.tga
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 6) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		# +12 (15)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_gore)
		#npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 5) # natural bab
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 0) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1)
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d8").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30

		npc.feat_add(toee.feat_iron_will, 0)
		npc.feat_add(toee.feat_endurance, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLELizardfolk(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14100

	@classmethod
	def get_price(cls): return 5

	@classmethod
	def get_title(cls): return "Lizardfolk"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD, toee.ALIGNMENT_CHAOTIC_GOOD, toee.ALIGNMENT_CHAOTIC_EVIL]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 2, 8, 0)
		utils_npc.npc_abilities_set(npc, [13, 10, 13, 9, 10, 10])

		npc.obj_set_int(toee.obj_f_critter_portrait, 3520) 
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		# +2 (5)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # 2x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d6").packed)

		#npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		#npc.condition_add_with_args("Monster Bonus Damage", toee.D20DT_FIRE, toee.dice_new("1d6").packed)

		npc.feat_add(toee.feat_iron_will, 0)
		npc.feat_add(toee.feat_endurance, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_2, npc))
		self._hide_loot(utils_item.item_create_in_inventory(4008, npc)) # Lizardman Club

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEShamblingMound(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14889

	@classmethod
	def get_price(cls): return 30

	@classmethod
	def get_title(cls): return "Shambling Mound"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD, toee.ALIGNMENT_CHAOTIC_GOOD, toee.ALIGNMENT_CHAOTIC_EVIL]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		#utils_npc.npc_hitdice_set(npc, 2, 8, 0)
		utils_npc.npc_abilities_set(npc, [22, 10, 17, 7, 10, 9])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 3520) 
		#npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL)
		#npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		#npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		#npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		#npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		# +11 (15)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_slam)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 6) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("2d8").packed)

		npc.condition_add_with_args("Base_Movement", 0, 66) # should be 20 ft, factor: 0.66 = 20/30
		#npc.condition_add_with_args("Monster Bonus Damage", toee.D20DT_FIRE, toee.dice_new("1d6").packed)

		#npc.feat_add(toee.feat_weapon_focus_unarmed_strike_medium_sized_being, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_2, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(4008, npc)) # Lizardman Club

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEWolf(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_WOLF

	@classmethod
	def get_price(cls): return 5

	@classmethod
	def get_title(cls): return "Wolf"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_LAWFUL_GOOD, toee.ALIGNMENT_CHAOTIC_GOOD, toee.ALIGNMENT_CHAOTIC_EVIL]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		#utils_npc.npc_hitdice_set(npc, 2, 8, 0)
		utils_npc.npc_abilities_set(npc, [13, 15, 15, 2, 14, 6])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 3520) 
		#npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_NEUTRAL)
		#npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		#npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		#npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		#npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		# +3 (5)
		#npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_slam)
		#npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 6) # natural bab
		#npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # 1x
		#npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("2d6").packed)

		npc.condition_add_with_args("Base_Movement", 0, 166) # should be 50 ft, factor: 1.66 = 50/30
		#npc.condition_add_with_args("Monster Bonus Damage", toee.D20DT_FIRE, toee.dice_new("1d6").packed)

		npc.feat_add(toee.feat_stunning_fist, 0)
		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal("stunning_fist charge", 100)
		self.setup_name(npc, self.get_title())

		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_LARGE_WOODEN_2, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(4008, npc)) # Lizardman Club

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlCEThriKreenRanger(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14100

	@classmethod
	def get_price(cls): return 11

	@classmethod
	def get_title(cls): return "Thri-Kreen Ranger"

	@classmethod
	def get_alignment_groups(cls): return [cls.get_alignment_group(), toee.ALIGNMENT_CHAOTIC_GOOD]

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 4, 8, 0)
		utils_npc.npc_abilities_set(npc, [12, 15, 11, 8, 12, 7])

		npc.obj_set_int(toee.obj_f_critter_portrait, 5310) # MOO_5311_m_scion
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, toee.ALIGNMENT_CHAOTIC_NEUTRAL)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 0)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 3)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 3)

		npc.obj_set_int(toee.obj_f_critter_monster_category, const_toee.mc_type_monstrous_humanoid)

		# +9/+4 (10/5)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 5) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d12").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, -1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d6").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add_with_args("Monster Melee Poison", const_toee.poison_carrion_crawler_brain_juice)
		npc.condition_add("Immunity_Sleep")

		npc.feat_add(toee.feat_deflect_arrows, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLEBarghest(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14897

	@classmethod
	def get_price(cls): return 27

	@classmethod
	def get_title(cls): return "Barghest"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 6, 8, 0)
		utils_npc.npc_abilities_set(npc, [17, 15, 13, 14, 14, 14])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 5310) # MOO_5311_m_scion todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 6) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		cat = const_toee.mc_type_outsider + ((toee.mc_subtype_extraplanar & toee.mc_subtype_evil & toee.mc_subtype_lawful) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		# +9/+4 (10/5)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 9-3) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d12").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, 4-3) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d4").packed)

		#npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add("Immunity_Sleep")

		npc.feat_add(toee.feat_combat_reflexes, 0)
		npc.feat_add(toee.feat_improved_initiative, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLEBeardedDevil(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14639

	@classmethod
	def get_price(cls): return 34

	@classmethod
	def get_title(cls): return "Bearded Devil"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 6, 8, 0)
		utils_npc.npc_abilities_set(npc, [15, 15, 17, 6, 10, 10])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 5310) # MOO_5311_m_scion todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		cat = const_toee.mc_type_outsider + ((toee.mc_subtype_extraplanar & toee.mc_subtype_evil & toee.mc_subtype_lawful & toee.mc_subtype_demon) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		# +11/+6 (10)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 11-2) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d10").packed)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 1, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 1, 11-5-2) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 1, 1) # 1x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 1, toee.dice_new("1d10").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Monster Energy Immunity", toee.D20DT_FIRE)
		#npc.condition_add_with_args("Monster Energy Resistance", 5, toee.D20DT_ACID) todo
		#npc.condition_add_with_args("Monster Energy Resistance", 5, toee.D20DT_COLD)
		npc.condition_add_with_args("Spell Resistance", 10 + 6)
		
		npc.condition_add("Immunity_Sleep")
		npc.condition_add("Immunity_Poison")

		npc.feat_add(toee.feat_power_attack, 0)
		npc.feat_add(toee.feat_improved_initiative, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLEDisplacerBeast(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14640

	@classmethod
	def get_price(cls): return 27

	@classmethod
	def get_title(cls): return "Displacer Beast"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 6, 10, 0)
		utils_npc.npc_abilities_set(npc, [18, 15, 16, 5, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 5050) # MOO_5051_m_Shadow_Mastiff todo
		#npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		cat = const_toee.mc_type_magical_beast
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		#Dmg: +9/+9 (10): d10
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 9-3) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d10").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		
		npc.condition_add("Monster Displacement")

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEGoblinSneak(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14636

	@classmethod
	def get_price(cls): return 6

	@classmethod
	def get_title(cls): return "Goblin Sneak"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		# LVL 1, SPD: 6, AC: 17, HP: 5
		# MELEE: +2 (5)
		# RANGED: +4 (5)
		# TYPE: Small Humanoid (Goblinoid)
		# SPECIAL ABILITIES: Slow Ranged Attack; Sneak Attack +5;

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		#utils_npc.npc_hitdice_set(npc, 1, 8, 0) # MM1
		utils_npc.npc_abilities_set(npc, [10, 14, 14, 10, 9, 6]) # MM1

		npc.make_class(toee.stat_level_rogue, 1)
		#AC 17 = 10 + 2 leather + 2 dex + 1 small
		#SPD 20 (4)
		#HP 5 = 1d6/2 + 1*x => 14 CON

		#STR: 18 due to atk is 2 = 1 bab + 0 str + 1 small; dmg will be 1d6 + 0 = 3.5
		#DEX: 14 due to atk is 4 = 1 bab + 2 dex + 1 small; dmg will be 1d6 + 0 = 3.5
		#CON: 12, see HP calculation
		#INT: 08 any
		#WIS: 12 due to AC wis bonus = 1
		#CHA: 08 any

		#npc.obj_set_int(toee.obj_f_critter_portrait, 5310) # MOO_5311_m_scion todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 2) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 0)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 0)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 0)

		cat = const_toee.mc_type_humanoid + ((toee.mc_subtype_goblinoid) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		# +2 (5)

		#npc.condition_add_with_args("Base_Movement", 0, 150) # should be 30 ft, factor: 1.5 = 30/20
		npc.condition_add_with_args("Base_Attack_Bonus1", 1)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_PADDED_RED, npc))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, npc)))
		#self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, npc)))

		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_MORNINGSTAR, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW, npc)))
		self._lower_weight_small(self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc))).obj_set_int(toee.obj_f_ammo_quantity, 100)

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlCGHalfOrcFighter(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_HALFORC_MAN

	@classmethod
	def get_price(cls): return 21

	@classmethod
	def get_title(cls): return "Half-Orc Fighter"

	@classmethod
	def get_commander_level(cls): return 3

	@classmethod
	def get_stats(cls): return {"Lvl": "2", "Spd": "4", "AC": "18", "HP": "20", "Type": "Humanoid (Orc)", "Commander Effect": "Melee attack +2"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 18 = 10 + 0 dex + 8 plate
		#SPD 20 (4)
		#HP 20 = 1d10 + 1d10 + 2x = {=10} + {6+10=16} + 2con x 2 {16+4=20}

		#STR: 16 atk 10 = 2 bab + 3 str + 1 wf + 1 mkw, =>10
		#DEX: 10 due to AC dex mod = 0
		#CON: 14, see HP calculation
		#INT: 6
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [14, 10, 14, 8, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 3020) #HOM_3020_b_barbarian
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_low_intelligence_berserker)

		npc.feat_add(toee.feat_weapon_focus_greataxe, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_mohawk
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_GILDED_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLACK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_BLACK, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATSWORD_MASTERWORK, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlCGHalfOrcFighterAsPC(CtrlCGHalfOrcFighter):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HALFORC_MAN

class CtrlLEHellHound(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14540

	@classmethod
	def get_price(cls): return 10

	@classmethod
	def get_title(cls): return "Hell Hound"

	@classmethod
	def get_stats(cls): return {"Lvl": "4", "Spd": "8", "AC": "16", "HP": "20", "Type": "Outsider"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [13, 13, 13, 6, 10, 6])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 5050) # MOO_5051_m_Shadow_Mastiff todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 5) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 4)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 4)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 4)

		cat = const_toee.mc_type_outsider + ((toee.mc_subtype_evil & toee.mc_subtype_fire & toee.mc_subtype_extraplanar & toee.mc_subtype_lawful) << 32)
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		#Dmg: +9/+9 (10): d10
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_claw)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 5-1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d8").packed)

		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30
		
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEHumanBlackguard(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_commander_level(cls): return 6

	@classmethod
	def get_price(cls): return 24

	@classmethod
	def get_title(cls): return "Human Blackguard"

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 0, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 1, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 2, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 3, toee.stat_level_fighter)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 4, toee.stat_level_fighter) # lv 5 fighter

		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 5, toee.stat_level_blackguard)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 6, toee.stat_level_blackguard)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 7, toee.stat_level_blackguard)
		npc.obj_set_idx_int(toee.obj_f_critter_level_idx, 8, toee.stat_level_blackguard) # lv 9, Fighter 5, Blackguard 4

		#AC 20 = 10 + 9 full plate + 1 dex
		#SPD 20 (4)
		#HP 70 = 1d10 + 4d10 + 4d10 + 9*x => {10} + {+22=32} + {+22=54} +9x = CON 14?

		#Dmg: +14/+9 (10 magic)
		#STR: 16 due to atk is 14 = 9 bab + 3 str + 1 magic + 1 wf; ~9.5
		#DEX: 12 due to AC dex mod = 1
		#CON: 14, see HP calculation
		#INT: 08 any
		#WIS: 12 due to 1st level DC: 13 => 10 + 1 lv + 1 mod wis
		#CHA: 14

		utils_npc.npc_abilities_set(npc, [16, 12, 14, 10, 12, 14])

		npc.obj_set_int(toee.obj_f_critter_portrait, 1060) #ELM_1060_b_paladin
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_arrogant)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_HEXTOR)
		npc.obj_set_int(toee.obj_f_critter_domain_1, toee.evil)
		npc.obj_set_int(toee.obj_f_critter_domain_2, toee.destruction)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_lawful)

		npc.obj_set_idx_int(toee.obj_f_critter_skill_idx, toee.skill_concentration, 5 + 4*2)

		npc.feat_add(toee.feat_power_attack, 0)
		npc.feat_add(toee.feat_cleave, 0)
		npc.feat_add(toee.feat_sunder, 0)
		npc.feat_add(toee.feat_exotic_weapon_proficiency_bastard_sword, 0)
		npc.feat_add(toee.feat_weapon_focus_bastard_sword, 0)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_shorthair
		hairStyle.color = const_toee.hair_color_white
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_GILDED_BOOTS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_GILDED_GLOVES, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_FULL_PLATE_PLUS_1_BLACK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_CIRCLET_HOODLESS, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_RED, npc))

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1, npc))

		npc.spells_memorized_forget()
		npc.spell_memorized_add(toee.spell_doom, toee.stat_level_blackguard, 1)
		npc.spell_memorized_add(toee.spell_cure_moderate_wounds, toee.stat_level_blackguard, 2)
		npc.spells_pending_to_memorized()

		utils_npc.npc_generate_hp_avg_first(npc)
		npc.item_wield_best_all()
		return

class CtrlLEHumanBlackguardAsPC(CtrlLEHumanBlackguard):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_PC_HUMAN_MAN

class CtrlLEHumanExecutioner(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 15

	@classmethod
	def get_title(cls): return "Human Executioner"

	@classmethod
	def get_stats(cls): return {"Lvl": "4", "Spd": "6", "AC": "13", "HP": "30", "Type": "Humanoid (Human)"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 13 = 10 + 1 dex + 2 leather
		#SPD 30 (6)
		#HP 30 = 1d10 + 3d10 + 3x = {=10} + {10+15+2=27} + 3*1  {27+3=30}

		#STR: 18 atk 10 = 4 bab + 5 str - 1pwr, => 8<>19 ~14
		#DEX: 12 due to AC dex mod = 1
		#CON: 12, see HP calculation
		#INT: 6
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [20, 12, 12, 8, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 7350) #NPC_7351_m_Turnkey.tga
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_low_intelligence_berserker)

		npc.feat_add(toee.feat_power_attack, 0)

		npc.feat_add(toee.feat_alertness, 1)
		npc.d20_send_signal(toee.S_SetPowerAttack, 1) # should go after refresh status, as it will be reset
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_bald
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLACK, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MASK_DROW, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BLACK, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_GREATAXE, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLEHumanThug(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return const_proto_npc.PROTO_NPC_MAN

	@classmethod
	def get_price(cls): return 4

	@classmethod
	def get_title(cls): return "Human Thug"

	@classmethod
	def get_stats(cls): return {"Lvl": "2", "Spd": "4", "AC": "16", "HP": "15", "Type": "Humanoid (Human)"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, 0, 0, 0)
		npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 16 = 10 + 0 dex + 5 chainmail + 1 small shield
		#SPD 40 (6)
		#HP 30 = 1d10 + 1d10 + 2x = {=10} + {10+5+1=16} + 2*0

		#STR: 14 atk 4 = 2 bab + 2 str, => 3<>7 ~5.5
		#DEX: 12 due to AC dex mod = 1
		#CON: 10, see HP calculation
		#INT: 6
		#WIS: 12
		#CHA: 8

		utils_npc.npc_abilities_set(npc, [14, 10, 10, 8, 12, 8])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6730) #NPC_6731_m_Raimol NPC_9311_m_panathaes
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)
		npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcvm_low_intelligence_berserker)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		hairStyle = utils_npc.HairStyle.from_npc(npc)
		hairStyle.style = const_toee.hair_style_bald
		hairStyle.color = const_toee.hair_color_black
		hairStyle.update_npc(npc)

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MASK_DROW, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_CHAINMAIL, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_CLUB, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 1)
		npc.item_wield_best_all()
		return

class CtrlLEKoboldWarrior(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14641

	@classmethod
	def get_price(cls): return 3

	@classmethod
	def get_title(cls): return "Kobold Warrior"

	@classmethod
	def get_stats(cls): return {"Lvl": "2", "Spd": "6", "AC": "15", "HP": "5", "Type": "Small Humanoid (Reptilian)"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		#npc.make_class(toee.stat_level_fighter, int(self.get_stats()["Lvl"]))
		#AC 15 = 10 + 1 dex + 2 leather + 1 small + 1 natural

		utils_npc.npc_abilities_set(npc, [9, 13, 10, 10, 9, 8])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 6730) #NPC_6731_m_Raimol NPC_9311_m_panathaes
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		#npc.obj_set_int(toee.obj_f_critter_deity, toee.DEITY_KORD)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_low_intelligence_berserker)
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 1) # natural ac

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		#hairStyle = utils_npc.HairStyle.from_npc(npc)
		#hairStyle.style = const_toee.hair_style_bald
		#hairStyle.color = const_toee.hair_color_black
		#hairStyle.update_npc(npc)

		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_GLOVES_LEATHER_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOAK_BLACK, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_MASK_DROW, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_cloth.PROTO_CLOTH_HELM_BARBARIAN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_GREY, npc))
		#self._hide_loot(utils_item.item_create_in_inventory(const_proto_armor.PROTO_SHIELD_SMALL_WOODEN, npc))
		
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTSPEAR, npc))

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEMedusa(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14280

	@classmethod
	def get_price(cls): return 62

	@classmethod
	def get_title(cls): return "Medusa"

	@classmethod
	def get_stats(cls): return {"Lvl": "6", "Spd": "6", "AC": "15", "HP": "35", "Type": "Monstrous Humanoid"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [10, 15, 12, 12, 13, 15])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6160) # NPC_6161_m_Zuggtmoy_D todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 3) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 5)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 5)

		cat = const_toee.mc_type_monstrous_humanoid
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		#Melee: +5/+3 (5/5 + Poison)
		#Ranged: +9/+4 (5)

		#npc.condition_add_with_args("Base_Attack_Bonus1", 6)

		npc.feat_add(toee.feat_martial_weapon_proficiency_shortbow, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_SHORTBOW, npc))
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_AMMO_ARROW_QUIVER, npc)).obj_set_int(toee.obj_f_ammo_quantity, 100)
		self._hide_loot(utils_item.item_create_in_inventory(const_proto_weapon.PROTO_WEAPON_DAGGER, npc))


		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEMindFlayer(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14290

	@classmethod
	def get_price(cls): return 35

	@classmethod
	def get_title(cls): return "Mind Flayer"

	@classmethod
	def get_stats(cls): return {"Lvl": "8", "Spd": "6", "AC": "15", "HP": "45", "Type": "Aberration"}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 8, 0)
		utils_npc.npc_abilities_set(npc, [12, 14, 12, 19, 17, 17])

		npc.obj_set_int(toee.obj_f_critter_portrait, 6420) # NPC_6421_m_Crone todo
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 3) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 6)

		cat = const_toee.mc_type_aberration
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		#Melee: +8/+8 (5)
		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_slap)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 8-1) # natural bab
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 2) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d4").packed)

		#npc.condition_add_with_args("Base_Attack_Bonus1", 6)

		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return

class CtrlLEMummy(CtrlSkirmisherLE):
	@classmethod
	def get_proto_id(cls): return 14137

	@classmethod
	def get_price(cls): return 36

	@classmethod
	def get_title(cls): return "Mummy"

	@classmethod
	def get_stats(cls): return {
			"Lvl": "8", 
			"Spd": "4", 
			"AC": "20", 
			"HP": "55", 
			"Type": "Undead",
			"Difficult": "5",
			"Melee": "+11 (15)"
		}

	def after_created(self, npc):
		assert isinstance(npc, toee.PyObjHandle)

		utils_npc.npc_hitdice_set(npc, int(self.get_stats()["Lvl"]), 12, 0)
		utils_npc.npc_abilities_set(npc, [24, 10, 10, 6, 14, 15])

		#npc.obj_set_int(toee.obj_f_critter_portrait, 6420) # NPC_6421_m_Crone todo 
		npc.obj_set_int(toee.obj_f_critter_gender, toee.gender_male)
		#npc.obj_set_int(toee.obj_f_pc_voice_idx, const_toee.pcv_lawful)
		npc.obj_set_int(toee.obj_f_critter_alignment, self.get_alignment_group())
		npc.obj_set_int(toee.obj_f_npc_ac_bonus, 10) # natural ac
		npc.obj_set_int(toee.obj_f_npc_save_fortitude_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_reflexes_bonus, 2)
		npc.obj_set_int(toee.obj_f_npc_save_willpower_bonus, 6)

		cat = const_toee.mc_type_undead
		npc.obj_set_int64(toee.obj_f_critter_monster_category, cat)

		npc.obj_set_idx_int(toee.obj_f_attack_types_idx, 0, const_toee.nwt_slam)
		npc.obj_set_idx_int(toee.obj_f_attack_bonus_idx, 0, 4) # natural bab: +4
		npc.obj_set_idx_int(toee.obj_f_critter_attacks_idx, 0, 1) # x
		npc.obj_set_idx_int(toee.obj_f_critter_damage_idx, 0, toee.dice_new("1d6").packed)

		npc.condition_add("Monster_Two_Handed")
		npc.condition_add("Monster Undead")
		npc.condition_add_with_args("Monster DR Magic", 5)
		npc.condition_add_with_args("Vulnurability_Energy", toee.D20DT_COLD)
		npc.condition_add_with_args("Base_Movement", 0, 133) # should be 40 ft, factor: 1.33 = 40/30

		npc.feat_add("Aura of Despair") #todo Aura of Fear 2
		npc.feat_add(toee.feat_great_fortitude, 0)
		npc.feat_add(toee.feat_toughness, 0)
		npc.feat_add(toee.feat_alertness, 1)
		self.setup_name(npc, self.get_title())

		utils_npc.npc_generate_hp_avg_first(npc, 0)
		npc.item_wield_best_all()
		return
