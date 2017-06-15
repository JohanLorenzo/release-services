# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

'''
Common constants and utilities for releng_notification_* services
'''


CHANNELS = [
    'EMAIL',
]

URGENCY_LEVELS = [
    'LOW', 'NORMAL', 'HIGH', 'DO_YESTERDAY',
]