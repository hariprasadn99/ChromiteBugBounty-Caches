from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import * 
import re
import os
from random import *

class uatg_cache_dcache_fill(IPlugin):
	def __init__(self):
		super().__init__()
		
	def execute(self, core_yaml, isa_yaml):
		_dcache_dict = core_yaml['dcache_configuration']
		_dcache_en = _dcache_dict['instantiate']
		self._sets = _dcache_dict['sets']
		self._word_size = _dcache_dict['word_size']
		self._block_size = _dcache_dict['block_size']
		self._ways = _dcache_dict['ways']
	
	def generate_asm(self) -> List[Dict[str, str]]:
		
		asm += f'\tfence\n'
		asm += f'\tli t0, -10\n'
		asm += f'\tli t1, 20\n'
		asm += f'\taddi t0, t1, t2\n'
		asm += f'\tfence.i\n'
		
		compile_macros = []

		return [{
			'asm_code': asm,
			'asm_data': asm_data,
			'asm_sig': '',
			'compile_macros': compile_macros
		}]	
	
	def check_log(self, log_file_path, reports_dir) -> bool:
		return False

	def generate_covergroups(self, config_file) -> str:
		sv = ""
		return sv
