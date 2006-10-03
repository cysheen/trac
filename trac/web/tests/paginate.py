# -*- coding: utf-8 -*-
#
# Copyright (C) 2006 Edgewall Software
# Copyright (C) 2006 Christopher Lenz <cmlenz@gmx.de>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://trac.edgewall.org/log/.

import doctest
import unittest

from trac.web import paginate


def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(paginate))
    return suite

if __name__ == '__main__':
    unittest.main()
