# Launchpad95 fix for colour blind users

import Live
from Launchpad95.Launchpad import Launchpad
from Launchpad95.SubSelectorComponent import *

class LaunchpadColour(Launchpad):

	def __init__(self, c_instance):
		Launchpad.__init__(self, c_instance)
		self.set_colours()
		
	def set_colours(self):
	
		#instrument controller
		self._selector._instrument_controller._normal_feedback_velocity = AMBER_FULL
		self._selector._instrument_controller._recordind_feedback_velocity = RED_FULL
		self._selector._instrument_controller._scales.base_note_color = AMBER_THIRD
		self._selector._instrument_controller._scales.scale_note_color = GREEN_THIRD
		
		#stepseq
		self._selector._stepseq._scale_selector.base_note_color = RED_THIRD
		self._selector._stepseq._scale_selector.scale_note_color = AMBER_THIRD
		self._selector._stepseq._note_editor.metronome_color = AMBER_FULL
		#Velocity colour map. this must remain of lengh 3.
		self._selector._stepseq._note_editor.velocity_color_map = [GREEN_THIRD,GREEN_HALF,RED_FULL]
		self._selector._stepseq._note_editor.muted_note_color = AMBER_THIRD
		self._selector._stepseq._note_editor.playing_note_color = GREEN_FULL
		
		#session
		for scene_index in range(self._selector._matrix.height()):
			scene = self._selector._session.scene(scene_index)
			scene.set_triggered_value(GREEN_BLINK)
			for track_index in range(self._selector._matrix.width()):
				clip_slot = scene.clip_slot(track_index)
				clip_slot.set_triggered_to_play_value(AMBER_BLINK)
				clip_slot.set_triggered_to_record_value(RED_BLINK)
				clip_slot.set_stopped_value(GREEN_FULL)
				clip_slot.set_started_value(GREEN_BLINK)
				clip_slot.set_recording_value(RED_FULL)
