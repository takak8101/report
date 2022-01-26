#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalcUpdate (unittest.TestCase):

   # 以下は修正前に実行したときの結果を示す

         # A<Bの場合 = 21 → TRUE
         def test_sampleUpdate001 (self):
            self.assertEqual (21, calc(3,7))

         # A>Bの場合 = 21 → FAIL
         def test_sampleUpdate002 (self):
            self.assertEqual (21, calc(7,3))

         # A=Bの場合 = 25 → FAIL
         def test_sampleUpdate003 (self):
            self.assertEqual (25, calc(5,5))

         # Aが領域外,Bが領域内 = -1　→ TRUE
         def test_sampleUpdate004 (self):
            self.assertEqual (-1, calc(0,1))
         
         # Aが領域内,Bが領域外 = -1　→ TRUE
         def test_sampleUpdate005 (self):
            self.assertEqual (-1, calc(1,1000))
         
         # Aが領域外,Bが領域内外= -1　→ TRUE
         def test_sampleUpdate004 (self):
            self.assertEqual (-1, calc(0,1000))

         # A,Bが文字列 = -1 → TRUE
         def test_sampleUpdate005 (self):
            self.assertEqual (-1, calc('a','b'))

         # Aが文字列,Bが数値 = -1 → ERROR
         def test_sampleUpdate006 (self):
            self.assertEqual (-1, calc('a',100))

         # Aが数値,Bが文字列 = -1 → ERROR
         def test_sampleUpdate007 (self):
            self.assertEqual (-1, calc(100,'b'))

         # Aに数値と文字を含む場合 = -1 → ERROR
         def test_sampleUpdate008  (self):
            self.assertEqual (-1, calc("1z",200))

         # Bに数値と文字を含む場合 = -1 → ERROR
         def test_sampleUpdate009  (self):
            self.assertEqual (-1, calc(200,"1z"))

         # A,Bに数値と文字を含む場合 = -1 → ERROR
         def test_sampleUpdate010  (self):
            self.assertEqual (-1, calc("1z","2y"))
         