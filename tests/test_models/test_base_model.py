#!/usr/bin/python3
"""
Defines unittests for base_model.py
"""

import unittest
from models.base_model import BaseModel


class TestBaseModelInstatioation(unittest.TestCase):
	"""
	Tests for BaseModel class instantiation

	A subclass of unittest.TestCase or inherits from unittest.TestCase
	"""
        
	def test_instance_id_is_unique(self):
		bm1 = BaseModel()
		bm2 = BaseModel()

		self.assertNotEqual(bm1.id, bm2.id)

	def test_instance_creation_from_dict_repsentation(self):
		bm1 = BaseModel()
		bm2 = BaseModel(**bm1.to_dict())

		self.assertEqual(bm1.id, bm2.id)
