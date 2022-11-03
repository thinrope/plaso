#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the SkyDriveLog log parser."""

import unittest

from plaso.parsers import skydrivelog

from tests.parsers import test_lib


class SkyDriveLogUnitTest(test_lib.ParserTestCase):
  """Tests for the SkyDrive log parser."""

  def testParseErrorLog(self):
    """Tests the Parse function or error log."""
    parser = skydrivelog.SkyDriveLog2Parser()
    storage_writer = self._ParseFile(['skydriveerr.log'], parser)

    number_of_event_data = storage_writer.GetNumberOfAttributeContainers(
        'event_data')
    self.assertEqual(number_of_event_data, 19)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 19)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    # Check parsing of a header line.
    expected_event_values = {
        'added_time': '2013-07-25T16:03:23.291+00:00',
        'data_type': 'skydrive:log:line',
        'detail': (
            'Logging started. Version= 17.0.2011.0627 StartLocalTime: '
            '2013-07-25-180323.291 PID=0x8f4 TID=0x718 ContinuedFrom=')}

    event_data = storage_writer.GetAttributeContainerByIndex('event_data', 0)
    self.CheckEventData(event_data, expected_event_values)

    # Check parsing of a log line.
    expected_event_values = {
        'added_time': '2013-07-25T16:03:24.649+00:00',
        'data_type': 'skydrive:log:line',
        'detail': 'Sign in failed : DRX_E_AUTH_NO_VALID_CREDENTIALS,',
        'log_level': 'ERR',
        'module': 'AUTH',
        'source_code': 'authapi.cpp(280)'}

    event_data = storage_writer.GetAttributeContainerByIndex('event_data', 1)
    self.CheckEventData(event_data, expected_event_values)

  def testParseErrorLogUnicode(self):
    """Tests the Parse function on Unicode error log."""
    parser = skydrivelog.SkyDriveLog2Parser()
    storage_writer = self._ParseFile(['skydriveerr-unicode.log'], parser)

    number_of_event_data = storage_writer.GetNumberOfAttributeContainers(
        'event_data')
    self.assertEqual(number_of_event_data, 19)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 19)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    expected_event_values = {
        'added_time': '2013-07-25T16:04:02.669+00:00',
        'data_type': 'skydrive:log:line',
        'detail': (
            'No node found named Passport-Jméno-člena, no user name '
            'available,')}

    event_data = storage_writer.GetAttributeContainerByIndex('event_data', 3)
    self.CheckEventData(event_data, expected_event_values)

  def testParseLog(self):
    """Tests the Parse function on normal log."""
    parser = skydrivelog.SkyDriveLog2Parser()
    storage_writer = self._ParseFile(['skydrive.log'], parser)

    number_of_event_data = storage_writer.GetNumberOfAttributeContainers(
        'event_data')
    self.assertEqual(number_of_event_data, 17)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 17)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    expected_event_values = {
        'added_time': '2013-08-12T02:52:32.976+00:00',
        'data_type': 'skydrive:log:line',
        'detail': (
            'Received data from server,dwID=0x0;dwSize=0x15a;pbData=GET 5 '
            'WNS 331 Context: 2891  <channel-response><id>1;'
            '13714367258539257282</id><exp>2013-09-11T02:52:37Z</exp><url>'
            'https://bn1.notify.windows.com/?token=AgYAAAAdkHjSxiNH1mbF0Rp'
            '5TIv0Kz317BKYIAfBNO6szULCOEE2393owBINnPC5xoika5SJlNtXZ%2bwzaR'
            'VsPRcP1p64XFn90vGwr07DGZxfna%2bxBpBBplzZhLV9y%2fNV%2bBPxNmTI5'
            'sRgaZ%2foGvYCIj6MdeU1</url></channel-response>'),
        'log_level': 'VRB',
        'module': 'WNS',
        'source_code': 'absconn.cpp(177)'}

    event_data = storage_writer.GetAttributeContainerByIndex('event_data', 11)
    self.CheckEventData(event_data, expected_event_values)


if __name__ == '__main__':
  unittest.main()
