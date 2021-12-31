from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import * 
import re
import os
from random import *

class uatg_cache_dcache_fill(IPlugin):
	""" Constructor to specify self variables required for test. """
	def __init__(self):
		super().__init__()
		
	""" Selects the parameters to make the test valid to be run on the DUT. """
	def execute(self, core_yaml, isa_yaml):
		_dcache_dict = core_yaml['dcache_configuration']
		_dcache_en = _dcache_dict['instantiate']
		self._sets = _dcache_dict['sets']
		self._word_size = _dcache_dict['word_size']
		self._block_size = _dcache_dict['block_size']
		self._ways = _dcache_dict['ways']
	
	""" Returns a string of the asm file which is to be generated. """
	def generate_asm(self) -> List[Dict[str, str]]:
		asm = str()
		# Loading 100 words of 4 bytes each into the register x10.
		for i in range(0,392,4) :
			asm += f'\tlw x10,' + str(i) + '(x13)\n'
		
		compile_macros = []
		asm_data = str()

		return [{
			'asm_code': asm,
			'asm_data': asm_data,
			'asm_sig': '',
			'compile_macros': compile_macros
		}]	
	
	""" Returns false based on patterns required in the DUT logs. """
	def check_log(self, log_file_path, reports_dir) -> bool:
		return False

	""" Returns a formatted string (converted to System Verilog) containing all coverpoints/assertions/covergroups necessary for test. """
	def generate_covergroups(self, config_file) -> str:
		sv = ""
		return sv
