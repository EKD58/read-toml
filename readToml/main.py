#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
read toml sample code
"""

import toml


TOMLFILE = './sampleData/sample.toml'


# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	file = open(TOMLFILE)
	buf = file.read()
	file.close()

	conf = toml.loads(buf)
	print(conf)

	return
